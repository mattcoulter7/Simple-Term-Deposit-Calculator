from typing import (
    List,
)

from simple_term_deposit_calculator.schemas.interest_paid import (
    BaseInterestPaidRule,
)
from simple_term_deposit_calculator.schemas.projected_savings import (
    ProjectedSavingsIteration,
)


class SimpleTermDepositCalculator:
    """
    A calculator for term deposit interest calculations based on the deposit amount, interest rate, investment term, 
    and how the interest is paid (monthly or at maturity).
    """

    def calculate_final_balance(
        self,
        deposit_amount: float,
        interest_rate: float,
        investment_term: int,  # in months
        interest_paid_rule: BaseInterestPaidRule,
    ) -> float:
        """
        Calculate the total interest earned on a term deposit.

        Args:
            deposit_amount (float): The initial amount of money deposited.
            interest_rate (float): The annual interest rate as a percentage (e.g., 5.0 for 5%).
            investment_term (int): The duration of the investment in months.
            interest_paid_rule (BaseInterestPaidRule): rule definition for how interest is paid (e.g., MONTHLY or AT_MATURITY).

        Returns:
            float: The total interest earned over the investment term.
        """
        return interest_paid_rule.calculate_interest(
            deposit_amount=deposit_amount,
            interest_rate=interest_rate,
            investment_term_in_years=investment_term / 12,
        )

    def calculate_projected_savings(
        self,
        deposit_amount: float,
        interest_rate: float,
        investment_term: int,  # in months
        interest_paid_rule: BaseInterestPaidRule,
    ) -> List[ProjectedSavingsIteration]:
        """
        Calculate the balance at every month on a term deposit.

        Args:
            deposit_amount (float): The initial amount of money deposited.
            interest_rate (float): The annual interest rate as a percentage (e.g., 5.0 for 5%).
            investment_term (int): The duration of the investment in months.
            interest_paid_rule (BaseInterestPaidRule): rule definition for how interest is paid (e.g., MONTHLY or AT_MATURITY).

        Returns:
            List[ProjectedSavingsIteration]: month balances from 1 -> investment_term.
        """
        iterations = []

        for month in range(investment_term):
            monthly_balance = self.calculate_final_balance(
                deposit_amount=deposit_amount,
                interest_rate=interest_rate,
                investment_term=month + 1,
                interest_paid_rule=interest_paid_rule,
            )

            interst_earned = monthly_balance - deposit_amount

            iterations.append(
                ProjectedSavingsIteration(
                    month=month + 1,
                    interest_rate=interest_rate,
                    interest_earned=interst_earned,
                    balance=monthly_balance,
                )
            )

        return iterations
