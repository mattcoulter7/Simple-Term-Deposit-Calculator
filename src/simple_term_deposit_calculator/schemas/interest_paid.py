from typing import (
    List
)
from abc import ABC, abstractmethod
from dataclasses import dataclass
from werkzeug.exceptions import NotFound


@dataclass
class BaseInterestPaidRule(ABC):
    label: str

    @abstractmethod
    def calculate_interest(
        self,
        deposit_amount: float,
        interest_rate: float,
        investment_term_in_years: float,
    ) -> float:
        raise NotImplementedError()

@dataclass
class SimpleInterestPaidRule(BaseInterestPaidRule):
    def calculate_interest(
        self,
        deposit_amount: float,
        interest_rate: float,
        investment_term_in_years: float,
    ) -> float:
        return deposit_amount * (1 + (interest_rate * investment_term_in_years))

@dataclass
class CompoundingInterestPaidRule(BaseInterestPaidRule):
    compounding_frequency_in_months: int

    def calculate_interest(
        self,
        deposit_amount: float,
        interest_rate: float,
        investment_term_in_years: float,
    ) -> float:
        return deposit_amount * ((1 + (interest_rate / self.compounding_frequency_in_months)) ** (self.compounding_frequency_in_months * investment_term_in_years))


INTEREST_PAID_RULES: List[BaseInterestPaidRule] = [
    CompoundingInterestPaidRule(
        label="MONTHLY",
        compounding_frequency_in_months=1,
    ),
    CompoundingInterestPaidRule(
        label="QUARTERLY",
        compounding_frequency_in_months=4,
    ),
    CompoundingInterestPaidRule(
        label="ANNUALLY",
        compounding_frequency_in_months=12,
    ),
    SimpleInterestPaidRule(
        label="AT_MATURITY",
    )
]
INTEREST_PAID_RULES_INDEX = {
    rule.label: rule
    for rule in INTEREST_PAID_RULES
}

def get_interest_paid_labels() -> List[str]:
    return list(INTEREST_PAID_RULES_INDEX.keys())

def get_interest_paid_rule(
    label: str,
) -> BaseInterestPaidRule:
    try:
        return INTEREST_PAID_RULES_INDEX[label]
    except KeyError:
        raise NotFound(
            f"No Interest Paid Rule found for label `{label}`"
        )
