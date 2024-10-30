from dataclasses import dataclass, field


@dataclass
class ProjectedSavingsIteration():
    month: int
    interest_rate: float
    interest_earned: float
    balance: float
    extra_deposits: float = field(default=0.)
