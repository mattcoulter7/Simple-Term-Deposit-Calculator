import pytest

from simple_term_deposit_calculator.schemas.interest_paid import InterestPaid


@pytest.mark.parametrize(
    "deposit_amount, interest_rate, investment_term, interest_paid, expected_final_balance",
    [
        (10_000, 0.011, 36, InterestPaid.AT_MATURITY, 10_330),  # example given from requirements.pdf
    ]
)
def test_simple_term_deposit_calculator(
    deposit_amount: float,
    interest_rate: float,
    investment_term: int,
    interest_paid: InterestPaid,
    expected_final_balance: float,
):
    raise NotImplementedError()
