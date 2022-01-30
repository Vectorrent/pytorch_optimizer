from typing import List

import pytest
import torch
from torch import nn

from pytorch_optimizer import SAM, Lookahead, load_optimizers


class Example(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(1, 1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.fc1(x)


OPTIMIZER_NAMES: List[str] = [
    'adamp',
    'sgdp',
    'madgrad',
    'ranger',
    'ranger21',
    'radam',
    'adabound',
    'adahessian',
    'adabelief',
    'diffgrad',
    'diffrgrad',
    'lamb',
    'ralamb',
]

BETA_OPTIMIZER_NAMES: List[str] = [
    'adabelief',
    'adabound',
    'adahessian',
    'adamp',
    'diffgrad',
    'diffrgrad',
    'lamb',
    'radam',
    'ranger',
    'ranger21',
    'ralamb',
]


@pytest.mark.parametrize('optimizer_names', OPTIMIZER_NAMES)
def test_learning_rate(optimizer_names):
    with pytest.raises(ValueError):
        optimizer = load_optimizers(optimizer_names)
        optimizer(None, lr=-1e-2)


@pytest.mark.parametrize('optimizer_names', OPTIMIZER_NAMES)
def test_epsilon(optimizer_names):
    with pytest.raises(ValueError):
        optimizer = load_optimizers(optimizer_names)
        optimizer(None, eps=-1e-6)


@pytest.mark.parametrize('optimizer_names', OPTIMIZER_NAMES)
def test_weight_decay(optimizer_names):
    with pytest.raises(ValueError):
        optimizer = load_optimizers(optimizer_names)
        optimizer(None, weight_decay=-1e-3)


@pytest.mark.parametrize('optimizer_names', BETA_OPTIMIZER_NAMES)
def test_betas(optimizer_names):
    optimizer = load_optimizers(optimizer_names)

    with pytest.raises(ValueError):
        optimizer(None, betas=(-0.1, 0.1))

    with pytest.raises(ValueError):
        optimizer(None, betas=(0.1, -0.1))


def test_sam_parameters():
    with pytest.raises(ValueError):
        SAM(None, load_optimizers('adamp'), rho=-0.1)


def test_lookahead_parameters():
    model: nn.Module = Example()
    parameters = model.parameters()
    optimizer = load_optimizers('adamp')(parameters)

    Lookahead(optimizer, pullback_momentum='reset')
    Lookahead(optimizer, pullback_momentum='pullback')

    with pytest.raises(ValueError):
        Lookahead(optimizer, k=0)

    with pytest.raises(ValueError):
        Lookahead(optimizer, alpha=0)

    with pytest.raises(ValueError):
        Lookahead(optimizer, pullback_momentum='invalid')
