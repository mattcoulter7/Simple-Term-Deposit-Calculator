import pytest

from simple_term_deposit_calculator.schemas.interest_paid import get_interest_paid_rule
from simple_term_deposit_calculator.calculator.simple import SimpleTermDepositCalculator


@pytest.mark.parametrize(
    "deposit_amount, interest_rate, investment_term, interest_paid, expected_final_balance",
    [
        (10_000, 0.011, 36, "AT_MATURITY", 10_330),  # example given from requirements.pdf
        (10_000, 0.011, 36, "MONTHLY", 10_335),
        (10_000, 0.011, 36, "QUARTERLY", 10_335),
        (10_000, 0.011, 36, "ANNUALLY", 10_334),
    ]
)
def test_simple_term_deposit_calculator(
    deposit_amount: float,
    interest_rate: float,
    investment_term: int,
    interest_paid: str,
    expected_final_balance: float,
):
    calculator = SimpleTermDepositCalculator()

    actual_final_balance = calculator.calculate_final_balance(
        deposit_amount=deposit_amount,
        interest_rate=interest_rate,
        investment_term=investment_term,
        interest_paid_rule=get_interest_paid_rule(interest_paid),
    )

    # for decimal comparison, we will use an approximation
    assert expected_final_balance == pytest.approx(expected_final_balance, rel=1e-2), \
        f"Incorrect calculation for {interest_paid}, expected {expected_final_balance}, calculated {actual_final_balance}"
