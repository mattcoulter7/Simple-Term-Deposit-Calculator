import typer
from typing import List

from simple_term_deposit_calculator.calculator.simple import SimpleTermDepositCalculator
from simple_term_deposit_calculator.schemas.interest_paid import InterestPaid
from simple_term_deposit_calculator.schemas.projected_savings import ProjectedSavingsIteration


# Create the Typer app instance
main = typer.Typer()


def echo_projected_savings(
    projected_savings: List[ProjectedSavingsIteration],
) -> None:
    def echo_projected_savings_iteration(
        iteration: ProjectedSavingsIteration,
    ):
        readable_interest_rate = iteration.interest_rate * 100
        # Month	| Extra deposits | Interest Rate | Interest earned | Balance
        typer.echo(
            f"{iteration.month} " + 
            f" | {iteration.extra_deposits:.2f}" + 
            f" | {readable_interest_rate}%" + 
            f" | ${iteration.interest_earned:.2f}" + 
            f" | ${iteration.balance:.2f}"
        )

    typer.echo(
        f"Month	| Extra deposits | Interest Rate | Interest earned | Balance"
    )
    for iteration in projected_savings:
        echo_projected_savings_iteration(iteration)

    return None


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

    # perform the calculation for final balance
    final_balance = calculator.calculate_final_balance(
        deposit_amount=deposit_amount,
        interest_rate=interest_rate / 100,  # normalise percentage between 0 and 1
        investment_term=investment_term,
        interest_paid=interest_paid,
    )
    # output the final balance
    typer.echo(f"Final balance after {investment_term} months: ${final_balance:.2f}")

    # perform the calculation for projected balance
    projected_savings = calculator.calculate_projected_savings(
        deposit_amount=deposit_amount,
        interest_rate=interest_rate / 100,  # normalise percentage between 0 and 1
        investment_term=investment_term,
        interest_paid=interest_paid,
    )
    # output the projected savings
    echo_projected_savings(projected_savings)

    # simple approach to prevent the window from closing immediately
    typer.prompt("Press Enter to exit...", default="", show_default=False)

# Entry point for the CLI app
if __name__ == "__main__":
    main()
