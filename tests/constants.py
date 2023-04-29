from typing import Any, Dict, List, Tuple, Union

from pytorch_optimizer import (
    ASGD,
    LARS,
    MADGRAD,
    MSVAG,
    OPTIMIZERS,
    PNM,
    QHM,
    SGDP,
    SGDW,
    SM3,
    A2Grad,
    AccSGD,
    AdaBelief,
    AdaBound,
    AdaFactor,
    Adai,
    AdaMod,
    AdamP,
    AdamS,
    Adan,
    AdaNorm,
    AdaPNM,
    AggMo,
    AliG,
    Apollo,
    DAdaptAdaGrad,
    DAdaptAdam,
    DAdaptAdan,
    DAdaptSGD,
    DiffGrad,
    Fromage,
    Lamb,
    Lion,
    Nero,
    NovoGrad,
    QHAdam,
    RAdam,
    Ranger,
    Ranger21,
    ScalableShampoo,
    Shampoo,
    Yogi,
)
from tests.utils import build_lookahead

ADAPTIVE_FLAGS: List[bool] = [True, False]
PULLBACK_MOMENTUM: List[str] = ['none', 'reset', 'pullback']

VALID_OPTIMIZER_NAMES: List[str] = list(OPTIMIZERS.keys())
INVALID_OPTIMIZER_NAMES: List[str] = [
    'asam',
    'sam',
    'gsam',
    'pcgrad',
    'adamd',
    'lookahead',
]

SPARSE_OPTIMIZERS: List[str] = ['madgrad', 'dadaptadagrad', 'sm3']
NO_SPARSE_OPTIMIZERS: List[str] = [
    optimizer for optimizer in VALID_OPTIMIZER_NAMES if optimizer not in SPARSE_OPTIMIZERS
]

BETA_OPTIMIZER_NAMES: List[str] = [
    'adabelief',
    'adabound',
    'adamp',
    'diffgrad',
    'lamb',
    'radam',
    'ranger',
    'ranger21',
    'pnm',
    'adapnm',
    'adan',
    'adai',
    'scalableshampoo',
    'dadaptadam',
    'dadaptadan',
    'adams',
    'adafactor',
    'novograd',
    'lion',
    'adanorm',
    'yogi',
    'swats',
    'adamod',
    'aggmo',
    'qhadam',
]

VALID_LR_SCHEDULER_NAMES: List[str] = [
    'CosineAnnealingWarmupRestarts',
    'ConstantLR',
    'CosineAnnealingLR',
    'CosineAnnealingWarmRestarts',
    'CyclicLR',
    'OneCycleLR',
]
INVALID_LR_SCHEDULER_NAMES: List[str] = ['dummy']

OPTIMIZERS: List[Tuple[Any, Dict[str, Union[float, bool, int]], int]] = [
    (build_lookahead, {'lr': 5e-1, 'weight_decay': 1e-3}, 10),
    (AdaBelief, {'lr': 5e-1, 'weight_decay': 1e-3}, 10),
    (AdaBelief, {'lr': 5e-1, 'weight_decay': 1e-3, 'amsgrad': True}, 10),
    (AdaBelief, {'lr': 5e-1, 'weight_decay': 1e-3, 'weight_decouple': False}, 10),
    (AdaBelief, {'lr': 5e-1, 'weight_decay': 1e-3, 'fixed_decay': True}, 10),
    (AdaBelief, {'lr': 5e-1, 'weight_decay': 1e-3, 'rectify': False}, 10),
    (AdaBound, {'lr': 5e-1, 'gamma': 0.1, 'weight_decay': 1e-3}, 50),
    (AdaBound, {'lr': 5e-1, 'gamma': 0.1, 'weight_decay': 1e-3, 'fixed_decay': True}, 50),
    (AdaBound, {'lr': 5e-1, 'gamma': 0.1, 'weight_decay': 1e-3, 'weight_decouple': False}, 50),
    (AdaBound, {'lr': 5e-1, 'gamma': 0.1, 'weight_decay': 1e-3, 'amsbound': True}, 50),
    (Adai, {'lr': 5e-1, 'weight_decay': 0.0}, 5),
    (Adai, {'lr': 5e-1, 'weight_decay': 0.0, 'use_gc': True}, 50),
    (Adai, {'lr': 5e-1, 'weight_decay': 0.0, 'dampening': 0.9}, 5),
    (Adai, {'lr': 5e-1, 'weight_decay': 1e-4, 'weight_decouple': False}, 5),
    (Adai, {'lr': 5e-1, 'weight_decay': 1e-4, 'weight_decouple': True}, 5),
    (Adai, {'lr': 5e-1, 'weight_decay': 1e-4, 'weight_decouple': False, 'stable_weight_decay': True}, 5),
    (Adai, {'lr': 5e-1, 'weight_decay': 1e-4, 'weight_decouple': True, 'stable_weight_decay': True}, 5),
    (AdamP, {'lr': 5e-1, 'weight_decay': 1e-3}, 5),
    (AdamP, {'lr': 5e-1, 'weight_decay': 1e-3, 'use_gc': True}, 10),
    (AdamP, {'lr': 5e-1, 'weight_decay': 1e-3, 'nesterov': True}, 5),
    (DiffGrad, {'lr': 5e-2, 'weight_decay': 1e-3}, 10),
    (DiffGrad, {'lr': 5e-2, 'weight_decay': 1e-3, 'amsgrad': True}, 10),
    (DiffGrad, {'lr': 5e-1, 'weight_decay': 1e-3, 'rectify': True}, 20),
    (Lamb, {'lr': 5e-1, 'weight_decay': 1e-3}, 20),
    (Lamb, {'lr': 5e-1, 'weight_decay': 1e-3, 'pre_norm': True, 'max_grad_norm': 0.0}, 20),
    (Lamb, {'lr': 5e-1, 'weight_decay': 1e-3, 'grad_averaging': False}, 20),
    (Lamb, {'lr': 5e-1, 'weight_decay': 1e-3, 'adam': True, 'eps': 1e-8}, 10),
    (Lamb, {'lr': 5e-1, 'weight_decay': 1e-3, 'pre_norm': True, 'eps': 1e-8}, 20),
    (Lamb, {'lr': 5e-1, 'weight_decay': 1e-3, 'rectify': True, 'degenerated_to_sgd': True}, 10),
    (LARS, {'lr': 5e-1, 'weight_decay': 1e-3}, 20),
    (LARS, {'lr': 5e-1, 'nesterov': True}, 20),
    (MADGRAD, {'lr': 5e-2, 'weight_decay': 1e-3}, 20),
    (MADGRAD, {'lr': 5e-2, 'weight_decay': 1e-3, 'eps': 0.0}, 20),
    (MADGRAD, {'lr': 1e-2, 'weight_decay': 1e-3, 'momentum': 0.0}, 20),
    (MADGRAD, {'lr': 5e-2, 'weight_decay': 1e-3, 'decouple_decay': True}, 20),
    (RAdam, {'lr': 5e-1, 'weight_decay': 1e-3}, 20),
    (RAdam, {'lr': 5e-1, 'weight_decay': 1e-3, 'degenerated_to_sgd': True}, 10),
    (SGDP, {'lr': 5e-1, 'weight_decay': 1e-4}, 10),
    (SGDP, {'lr': 5e-1, 'weight_decay': 1e-4, 'nesterov': True}, 10),
    (Ranger, {'lr': 5e-1, 'weight_decay': 1e-3}, 100),
    (Ranger, {'lr': 5e-1, 'weight_decay': 1e-3, 'degenerated_to_sgd': True}, 50),
    (Ranger21, {'lr': 5e-1, 'weight_decay': 1e-3, 'num_iterations': 100}, 100),
    (Shampoo, {'lr': 5e-1, 'weight_decay': 1e-3, 'momentum': 0.1}, 10),
    (
        ScalableShampoo,
        {
            'lr': 1e-1,
            'weight_decay': 1e-3,
            'start_preconditioning_step': 9,
            'preconditioning_compute_steps': 9,
            'graft_type': 0,
        },
        10,
    ),
    (
        ScalableShampoo,
        {
            'lr': 1e-1,
            'weight_decay': 1e-3,
            'start_preconditioning_step': 9,
            'preconditioning_compute_steps': 10,
            'graft_type': 1,
        },
        10,
    ),
    (
        ScalableShampoo,
        {
            'lr': 1e-1,
            'weight_decay': 1e-3,
            'start_preconditioning_step': 9,
            'preconditioning_compute_steps': 10,
            'graft_type': 2,
        },
        10,
    ),
    (
        ScalableShampoo,
        {
            'lr': 1e-2,
            'weight_decay': 1e-3,
            'start_preconditioning_step': 9,
            'preconditioning_compute_steps': 10,
            'graft_type': 3,
        },
        10,
    ),
    (
        ScalableShampoo,
        {
            'lr': 1e-1,
            'weight_decay': 1e-3,
            'start_preconditioning_step': 9,
            'preconditioning_compute_steps': 10,
            'graft_type': 4,
        },
        10,
    ),
    (
        ScalableShampoo,
        {
            'lr': 1e-1,
            'weight_decay': 1e-3,
            'start_preconditioning_step': 9,
            'preconditioning_compute_steps': 10,
            'pre_conditioner_type': 0,
        },
        10,
    ),
    (
        ScalableShampoo,
        {
            'lr': 1e-1,
            'weight_decay': 1e-3,
            'start_preconditioning_step': 9,
            'preconditioning_compute_steps': 10,
            'pre_conditioner_type': 1,
        },
        10,
    ),
    (
        ScalableShampoo,
        {
            'lr': 1e-1,
            'weight_decay': 1e-3,
            'start_preconditioning_step': 9,
            'preconditioning_compute_steps': 10,
            'pre_conditioner_type': 2,
        },
        10,
    ),
    (
        ScalableShampoo,
        {
            'lr': 1e-1,
            'weight_decay': 1e-3,
            'start_preconditioning_step': 9,
            'preconditioning_compute_steps': 10,
            'inverse_exponent_override': 1,
        },
        10,
    ),
    (
        ScalableShampoo,
        {
            'lr': 1e-1,
            'weight_decay': 1e-3,
            'start_preconditioning_step': 9,
            'preconditioning_compute_steps': 10,
            'nesterov': False,
        },
        10,
    ),
    (
        ScalableShampoo,
        {
            'lr': 1e-1,
            'weight_decay': 1e-3,
            'start_preconditioning_step': 9,
            'preconditioning_compute_steps': 10,
            'decoupled_weight_decay': True,
        },
        10,
    ),
    (
        ScalableShampoo,
        {
            'lr': 1e-0,
            'weight_decay': 1e-3,
            'start_preconditioning_step': 9,
            'preconditioning_compute_steps': 10,
            'decoupled_learning_rate': False,
        },
        10,
    ),
    (
        ScalableShampoo,
        {
            'lr': 1e-1,
            'weight_decay': 1e-3,
            'start_preconditioning_step': 9,
            'preconditioning_compute_steps': 10,
            'moving_average_for_momentum': True,
        },
        10,
    ),
    (PNM, {'lr': 5e-1}, 25),
    (PNM, {'lr': 5e-1, 'weight_decouple': False}, 25),
    (AdaPNM, {'lr': 5e-1, 'weight_decay': 1e-3}, 10),
    (AdaPNM, {'lr': 5e-1, 'weight_decay': 1e-3, 'weight_decouple': False}, 10),
    (AdaPNM, {'lr': 5e-1, 'weight_decay': 1e-3, 'amsgrad': False}, 10),
    (Nero, {'lr': 5e-1}, 25),
    (Nero, {'lr': 5e-1, 'constraints': False}, 25),
    (Adan, {'lr': 5e-1}, 5),
    (Adan, {'lr': 5e-1, 'max_grad_norm': 1.0}, 5),
    (Adan, {'lr': 5e-1, 'weight_decay': 1e-3, 'use_gc': True}, 5),
    (Adan, {'lr': 5e-1, 'weight_decay': 1e-3, 'weight_decouple': True}, 5),
    (DAdaptAdaGrad, {'lr': 2.0, 'weight_decay': 1e-3}, 50),
    (DAdaptAdaGrad, {'lr': 2.0, 'weight_decay': 1e-3, 'momentum': 0.1}, 50),
    (DAdaptAdam, {'lr': 2.0, 'weight_decay': 1e-3}, 25),
    (DAdaptAdam, {'lr': 1.0, 'weight_decay': 1e-3, 'weight_decouple': True}, 50),
    (DAdaptSGD, {'lr': 2.0, 'weight_decay': 1e-2}, 25),
    (DAdaptSGD, {'lr': 2.0, 'momentum': 0.9, 'weight_decay': 1e-3}, 25),
    (DAdaptAdan, {'lr': 1.0, 'weight_decay': 1e-2}, 25),
    (DAdaptAdan, {'lr': 1.0, 'weight_decay': 1e-2, 'weight_decouple': True}, 50),
    (AdamS, {'lr': 1.0, 'weight_decay': 1e-3}, 10),
    (AdamS, {'lr': 1.0, 'weight_decay': 1e-3, 'amsgrad': True}, 20),
    (AdaFactor, {'lr': 7.5e-1, 'weight_decay': 1e-3, 'scale_parameter': False}, 100),
    (AdaFactor, {'lr': 7.5e-1, 'weight_decay': 1e-3, 'amsgrad': True}, 125),
    (Apollo, {'lr': 5e-1, 'weight_decay': 1e-3}, 10),
    (Apollo, {'lr': 5e-1, 'weight_decay': 1e-3, 'rebound': 'belief'}, 10),
    (Apollo, {'lr': 5e-1, 'weight_decay': 1e-3, 'weight_decay_type': 'stable', 'warmup_steps': 0}, 50),
    (NovoGrad, {'lr': 5e-1, 'weight_decay': 1e-3, 'grad_averaging': True}, 50),
    (Lion, {'lr': 5e-1, 'weight_decay': 1e-3}, 5),
    (Lion, {'lr': 5e-1, 'weight_decay': 1e-3, 'weight_decouple': False}, 5),
    (Lion, {'lr': 5e-1, 'weight_decay': 1e-3, 'use_gc': True}, 10),
    (AliG, {'max_lr': 5e-1, 'momentum': 0.9}, 5),
    (AliG, {'max_lr': 5e-1, 'momentum': 0.9, 'adjusted_momentum': True}, 5),
    (SM3, {'lr': 5e-1, 'momentum': 0.9, 'beta': 0.9}, 5),
    (AdaNorm, {'lr': 5e-1, 'weight_decay': 1e-3}, 5),
    (AdaNorm, {'lr': 5e-1, 'weight_decay': 1e-3, 'fixed_decay': True}, 5),
    (AdaNorm, {'lr': 5e-1, 'weight_decay': 1e-3, 'weight_decouple': False}, 5),
    (AdaNorm, {'lr': 5e-1, 'weight_decay': 1e-3, 'amsgrad': True}, 5),
    (A2Grad, {'variant': 'uni', 'beta': 1.0, 'lips': 1.0}, 5),
    (A2Grad, {'variant': 'inc', 'beta': 1.0, 'lips': 1.0}, 5),
    (A2Grad, {'variant': 'exp', 'beta': 1.0, 'lips': 1.0, 'rho': 0.9}, 5),
    (AccSGD, {'lr': 1e-0, 'weight_decay': 1e-3}, 5),
    (SGDW, {'lr': 5e-1, 'momentum': 0.9, 'weight_decay': 1e-3}, 5),
    (SGDW, {'lr': 5e-1, 'momentum': 0.9, 'weight_decay': 1e-3, 'weight_decouple': False}, 5),
    (SGDW, {'lr': 5e-1, 'momentum': 0.9, 'weight_decay': 1e-3, 'nesterov': True}, 5),
    (ASGD, {'lr': 5e-1, 'weight_decay': 1e-3}, 5),
    (ASGD, {'lr': 5e-1, 'weight_decay': 1e-3, 'weight_decouple': False}, 5),
    (Yogi, {'lr': 5e-1, 'weight_decay': 1e-3}, 5),
    (Fromage, {'lr': 5e-1, 'p_bound': 2.0}, 5),
    (MSVAG, {'lr': 5e-1}, 10),
    (AdaMod, {'lr': 5e1, 'weight_decay': 1e-3}, 10),
    (AdaMod, {'lr': 5e1, 'weight_decay': 1e-3, 'weight_decouple': False}, 10),
    (AggMo, {'lr': 5e0, 'weight_decay': 1e-3}, 5),
    (AggMo, {'lr': 5e0, 'weight_decay': 1e-3, 'weight_decouple': True}, 5),
    (QHAdam, {'lr': 1e0, 'nus': (0.9, 0.9), 'weight_decay': 1e-3}, 5),
    (QHAdam, {'lr': 1e0, 'weight_decay': 1e-3, 'weight_decouple': True}, 5),
    (QHM, {'lr': 1e0, 'weight_decay': 1e-3}, 5),
    (QHM, {'lr': 1e0, 'weight_decay': 1e-3, 'weight_decouple': True}, 5),
]
ADANORM_SUPPORTED_OPTIMIZERS: List[Tuple[Any, Dict[str, Union[float, bool, int]], int]] = [
    (AdaBelief, {'lr': 5e-1, 'weight_decay': 1e-3, 'adanorm': True}, 10),
    (AdamP, {'lr': 5e-1, 'weight_decay': 1e-3, 'adanorm': True}, 5),
    (AdamS, {'lr': 7.5e-1, 'weight_decay': 1e-3, 'adanorm': True}, 5),
    (AdaPNM, {'lr': 5e-1, 'weight_decay': 1e-3, 'adanorm': True}, 5),
    (DiffGrad, {'lr': 5e-2, 'weight_decay': 1e-3, 'adanorm': True}, 5),
    (Lamb, {'lr': 5e-1, 'adanorm': True}, 15),
    (RAdam, {'lr': 5e0, 'weight_decay': 1e-3, 'adanorm': True}, 25),
    (Ranger, {'lr': 5e-1, 'weight_decay': 1e-3, 'adanorm': True}, 100),
    (Adan, {'lr': 5e-1, 'weight_decay': 1e-3, 'adanorm': True}, 5),
    (Lion, {'lr': 5e-1, 'weight_decay': 1e-3, 'adanorm': True}, 5),
    (Yogi, {'lr': 5e-1, 'weight_decay': 1e-3, 'adanorm': True}, 5),
]
ADAMD_SUPPORTED_OPTIMIZERS: List[Tuple[Any, Dict[str, Union[float, bool, int]], int]] = [
    (AdaBelief, {'lr': 1e1, 'weight_decay': 1e-3, 'adam_debias': True}, 5),
    (AdaBelief, {'lr': 1e1, 'weight_decay': 1e-3, 'rectify': True, 'adam_debias': True}, 5),
    (AdaBound, {'lr': 1e0, 'gamma': 0.1, 'weight_decay': 1e-3, 'adam_debias': True}, 35),
    (AdamP, {'lr': 1e0, 'weight_decay': 1e-3, 'adam_debias': True}, 5),
    (AdamS, {'lr': 2e1, 'weight_decay': 1e-3, 'adam_debias': True}, 5),
    (DiffGrad, {'lr': 1e0, 'weight_decay': 1e-3, 'adam_debias': True}, 25),
    (DiffGrad, {'lr': 1e0, 'weight_decay': 1e-3, 'rectify': True, 'adam_debias': True}, 25),
    (Lamb, {'lr': 1e1, 'weight_decay': 1e-3, 'rectify': True, 'adam_debias': True}, 30),
    (RAdam, {'lr': 1e0, 'weight_decay': 1e-3, 'adam_debias': True}, 25),
    (Ranger, {'lr': 1e1, 'weight_decay': 1e-3, 'adam_debias': True}, 35),
    (Ranger21, {'lr': 1e0, 'weight_decay': 1e-3, 'adam_debias': True, 'num_iterations': 125}, 125),
    (AdaPNM, {'lr': 1e0, 'weight_decay': 1e-3, 'adam_debias': True}, 10),
    (NovoGrad, {'lr': 1e0, 'weight_decay': 1e-3, 'adam_debias': True}, 5),
    (AdaNorm, {'lr': 1e0, 'weight_decay': 1e-3, 'adam_debias': True}, 5),
    (Yogi, {'lr': 1e0, 'weight_decay': 1e-3, 'adam_debias': True}, 5),
    (AdaMod, {'lr': 1e2, 'weight_decay': 1e-3, 'adam_debias': True}, 20),
]
