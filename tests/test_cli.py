import pytest
import re

from typer.testing import CliRunner

from simple_term_deposit_calculator.application.cli import main  # Adjust based on your actual module name

runner = CliRunner()


@pytest.mark.parametrize(
    "deposit_amount, interest_rate, investment_term, interest_paid, expected_final_balance",
    [
        ("10000", "1.1", "36", "MONTHLY", "10330.00"),  # example given from requirements.pdf, but in cli format
    ]
)
def test_cli(
    deposit_amount: str,
    interest_rate: str,
    investment_term: str,
    interest_paid: str,
    expected_final_balance: str,
):
    # Run the CLI command with the given parameters
    result = runner.invoke(
        main,
        [
            "--deposit-amount", deposit_amount,
            "--interest-rate", interest_rate,
            "--investment-term", investment_term,
            "--interest-paid", interest_paid,
        ]
    )

    assert result.exit_code == 0
    assert f"Final balance after {investment_term} months: ${expected_final_balance}" in result.output, f"Unexpected output: {result.output}"
