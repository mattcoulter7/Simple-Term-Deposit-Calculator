from enum import Enum


class InterestPaid(Enum):
    MONTHLY = "MONTHLY"
    QUARTERLY = "QUARTERLY"
    ANNUALLY = "ANNUALLY"
    AT_MATURITY = "AT_MATURITY"
