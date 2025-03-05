import pytest

from pytorch_optimizer.optimizer import create_optimizer, load_optimizer
from tests.constants import VALID_OPTIMIZER_NAMES
from tests.utils import LogisticRegression


@pytest.mark.parametrize('use_lookahead', [True, False])
@pytest.mark.parametrize('use_orthograd', [True, False])
@pytest.mark.parametrize('optimizer_name', VALID_OPTIMIZER_NAMES)
def test_create_optimizer(use_lookahead, use_orthograd, optimizer_name):
    if optimizer_name in ('adamw', 'adam', 'sgd', 'demo'):
        pytest.skip(f'skip {optimizer_name}')

    if optimizer_name in ('ranger', 'ranger21', 'ranger25') and use_lookahead:
        pytest.skip(f'skip {optimizer_name}  w/ lookahead')

    if use_lookahead and use_orthograd:
        pytest.skip()

    kwargs = {'eps': 1e-8, 'k': 7}
    if optimizer_name == 'ranger21':
        kwargs.update({'num_iterations': 1})
    elif optimizer_name == 'bsam':
        kwargs.update({'num_data': 1})
    elif optimizer_name == 'demo':
        kwargs = {}

    create_optimizer(
        LogisticRegression(),
        optimizer_name=optimizer_name,
        use_lookahead=use_lookahead,
        use_orthograd=use_orthograd,
        **kwargs,
    )


def test_bnb_optimizer():
    with pytest.raises(ImportError):
        load_optimizer('bnb_adamw8bit')


def test_q_galore_optimizer():
    with pytest.raises(ImportError):
        load_optimizer('q_galore_adamw8bit')


def test_torchao_optimizer():
    with pytest.raises(ImportError):
        load_optimizer('torchao_adamw4bit')
