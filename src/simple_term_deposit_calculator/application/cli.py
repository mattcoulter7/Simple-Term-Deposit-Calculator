import typer

from simple_term_deposit_calculator.calculator import SimpleTermDepositCalculator
from simple_term_deposit_calculator.schemas.interest_paid import InterestPaid


# Create the Typer app instance
main = typer.Typer()

# Function to calculate the term deposit using named parameters or prompts
@main.command()
def calculate_term_deposit(
    deposit_amount: float = typer.Option(
        ...,
        prompt="The initial deposit amount (e.g., 10000 for $10,000)",
        help="The initial deposit amount (e.g., 10000 for $10,000)",
        min=1_000.,
        max=1_500_000.,
    ),
    interest_rate: float = typer.Option(
        ...,
        prompt="The interest rate as a decimal (e.g., 1.1 for 1.1%)",
        help="The interest rate as a decimal (e.g., 1.1 for 1.1%)",
        min=0.,
        max=15.,
    ),
    investment_term: int = typer.Option(
        ...,
        prompt="The investment term in months (e.g., 36 for 3 years)",
        help="The investment term in months (e.g., 36 for 3 years)",
        min=3,
        max=60,
    ),
    interest_paid: InterestPaid = typer.Option(
        ...,
        prompt=f"How the interest is paid",
        help=f"How the interest is paid",
        show_choices=True,
    ),
):
    # create the calculator
    calculator = SimpleTermDepositCalculator()

    # perform the calculation
    final_balance = calculator.calculate(
        deposit_amount=deposit_amount,
        interest_rate=interest_rate / 100,  # normalise percentage between 0 and 1
        investment_term=investment_term,
        interest_paid=interest_paid,
    )

    # output the result
    typer.echo(f"Final balance after {investment_term} months: ${final_balance:.2f}")

    # simple approach to prevent the window from closing immediately
    typer.prompt("Press Enter to exit...", default="", show_default=False)

# Entry point for the CLI app
if __name__ == "__main__":
    main()
