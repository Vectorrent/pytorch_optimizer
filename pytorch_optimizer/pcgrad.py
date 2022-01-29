import random
from copy import deepcopy
from typing import Iterable, List, Tuple

import numpy as np
import torch
from torch import nn
from torch.optim.optimizer import Optimizer


class PCGrad:
    """
    Reference : https://github.com/WeiChengTseng/Pytorch-PCGrad
    Example :
        from pytorch_optimizer import AdamP, PCGrad
        ...
        model = YourModel()
        optimizer = PCGrad(AdamP(model.parameters()))

        loss_1, loss_2 = nn.L1Loss(), nn.MSELoss()
        ...
        for input, output in data:
          optimizer.zero_grad()
          loss1, loss2 = loss1_fn(y_pred, output), loss2_fn(y_pred, output)
          optimizer.pc_backward([loss1, loss2])
          optimizer.step()
    """

    def __init__(self, optimizer: Optimizer, reduction: str = 'mean'):
        self.optimizer = optimizer
        self.reduction = reduction

    def check_valid_parameters(self):
        if self.reduction not in ('mean', 'sum'):
            raise ValueError(f'invalid reduction : {self.reduction}')

    @staticmethod
    def flatten_grad(grads: List[torch.Tensor]) -> torch.Tensor:
        return torch.cat([g.flatten() for g in grads])

    @staticmethod
    def un_flatten_grad(grads: torch.Tensor, shapes: List[int]) -> List[torch.Tensor]:
        idx: int = 0
        un_flatten_grad: List[torch.Tensor] = []
        for shape in shapes:
            length = np.prod(shape)
            un_flatten_grad.append(grads[idx : idx + length].view(shape).clone())
            idx += length
        return un_flatten_grad

    def zero_grad(self):
        return self.optimizer.zero_grad(set_to_none=True)

    def step(self):
        return self.optimizer.step()

    def set_grad(self, grads: List[torch.Tensor]):
        idx: int = 0
        for group in self.optimizer.param_groups:
            for p in group['params']:
                p.grad = grads[idx]
                idx += 1

    def retrieve_grad(self) -> Tuple[List[torch.Tensor], List[int], List[torch.Tensor]]:
        """get the gradient of the parameters of the network with specific objective"""
        grad, shape, has_grad = [], [], []
        for group in self.optimizer.param_groups:
            for p in group['params']:
                if p.grad is None:
                    shape.append(p.shape)
                    grad.append(torch.zeros_like(p, device=p.device))
                    has_grad.append(torch.zeros_like(p, device=p.device))
                    continue

                shape.append(p.grad.shape)
                grad.append(p.grad.clone())
                has_grad.append(torch.ones_like(p, device=p.device))

        return grad, shape, has_grad

    def pack_grad(self, objectives: Iterable) -> Tuple[List[torch.Tensor], List[List[int]], List[torch.Tensor]]:
        """pack the gradient of the parameters of the network for each objective
        :param objectives: Iterable[nn.Module]. a list of objectives
        :return:
        """
        grads, shapes, has_grads = [], [], []
        for objective in objectives:
            self.optimizer.zero_grad(set_to_none=True)
            objective.backward(retain_graph=True)

            grad, shape, has_grad = self.retrieve_grad()

            grads.append(self.flatten_grad(grad))
            has_grads.append(self.flatten_grad(has_grad))
            shapes.append(shape)

        return grads, shapes, has_grads

    def project_conflicting(self, grads, has_grads) -> torch.Tensor:
        """project conflicting
        :param grads: a list of the gradient of the parameters
        :param has_grads: a list of mask represent whether the parameter has gradient
        :return:
        """
        shared = torch.stack(has_grads).prod(0).bool()

        pc_grad = deepcopy(grads)
        for g_i in pc_grad:
            random.shuffle(grads)
            for g_j in grads:
                g_i_g_j = torch.dot(g_i, g_j)
                if g_i_g_j < 0:
                    g_i -= g_i_g_j * g_j / (g_j.norm() ** 2)

        merged_grad = torch.zeros_like(grads[0]).to(grads[0].device)
        if self.reduction == 'mean':
            merged_grad[shared] = torch.stack([g[shared] for g in pc_grad]).mean(dim=0)
        else:
            merged_grad[shared] = torch.stack([g[shared] for g in pc_grad]).sum(dim=0)

        merged_grad[~shared] = torch.stack([g[~shared] for g in pc_grad]).sum(dim=0)

        return merged_grad

    def pc_backward(self, objectives: Iterable[nn.Module]):
        """calculate the gradient of the parameters
        :param objectives: Iterable[nn.Module]. a list of objectives
        :return:
        """
        grads, shapes, has_grads = self.pack_grad(objectives)
        pc_grad = self.project_conflicting(grads, has_grads)
        pc_grad = self.un_flatten_grad(pc_grad, shapes[0])

        self.set_grad(pc_grad)
