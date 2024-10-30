from enum import Enum


class InterestPaid(Enum):
    MONTHLY = "MONTHLY"
    QUARTERLY = "QUARTERLY"
    ANNUALLY = "ANNUALLY"
    AT_MATURITY = "AT_MATURITY"


COMPOUNDING_FREQUENCIES = {
    InterestPaid.MONTHLY: 12,
    InterestPaid.QUARTERLY: 4,
    InterestPaid.ANNUALLY: 1,
}


class InterestPaidRule:
    label: str
    frequency: int
