import torch
from torch import nn


def get_cosine_similarity(x1: torch.Tensor, x2: torch.Tensor, eps: float = 1e-6) -> torch.Tensor:
    p12 = (x1 * x2).sum(-1)
    p1 = torch.sqrt((x1 * x1).sum(-1))
    p2 = torch.sqrt((x2 * x2).sum(-1))
    return p12 / (p1 * p2 + eps)


class SoftF1Loss(nn.Module):
    r"""soft-F1 loss.

    :param beta: float. f-beta.
    :param eps: float. epsilon.
    """

    def __init__(self, beta: float = 1.0, eps: float = 1e-6):
        super().__init__()
        self.beta = beta
        self.eps = eps

    def forward(self, y_pred: torch.Tensor, y_true: torch.Tensor) -> torch.Tensor:
        tp = (y_true * y_pred).sum().float()
        fn = ((1 - y_true) * y_pred).sum().float()
        fp = (y_true * (1 - y_pred)).sum().float()

        p = tp / (tp + fp + self.eps)
        r = tp / (tp + fn + self.eps)

        f1 = (1 + self.beta ** 2) * (p * r) / ((self.beta ** 2) * p + r + self.eps)  # fmt: skip
        f1 = torch.where(torch.isnan(f1), torch.zeros_like(f1), f1)

        return 1.0 - f1.mean()
