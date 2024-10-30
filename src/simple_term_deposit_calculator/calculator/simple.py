from typing import (
    List,
)

from simple_term_deposit_calculator.schemas.interest_paid import (
    InterestPaid,
    COMPOUNDING_FREQUENCIES,
)
from simple_term_deposit_calculator.schemas.projected_savings import (
    ProjectedSavingsIteration,
)


class SimpleTermDepositCalculator(object):
    """
    A calculator for term deposit interest calculations based on the deposit amount, interest rate, investment term, 
    and how the interest is paid (monthly or at maturity).
    """

    def calculate_final_balance(
        self,
        deposit_amount: float,
        interest_rate: float,
        investment_term: int,  # in months
        interest_paid: InterestPaid,
    ) -> float:
        """
        Calculate the total interest earned on a term deposit.

        Args:
            deposit_amount (float): The initial amount of money deposited.
            interest_rate (float): The annual interest rate as a percentage (e.g., 5.0 for 5%).
            investment_term (int): The duration of the investment in months.
            interest_paid (InterestPaid): Enum or type representing how interest is paid (e.g., monthly or at maturity).

        Returns:
            float: The total interest earned over the investment term.
        """
        investment_term_in_years = investment_term / 12

        # handle non-frequency cases
        if interest_paid is InterestPaid.AT_MATURITY:
            # apply simple interest formula for maturity
            return deposit_amount * (1 + (interest_rate * investment_term_in_years))

        # handle frequency cases
        # determine the frequency
        compounding_frequency = COMPOUNDING_FREQUENCIES.get(interest_paid)
        if compounding_frequency is None:
            raise ValueError(
                f"Invalid value for interest_paid, expected one of {list(InterestPaid)}, found {repr(deposit_amount)}"
            )

        # apply compound interest formula
        return deposit_amount * ((1 + (interest_rate / compounding_frequency)) ** (compounding_frequency * investment_term_in_years))

    def calculate_projected_savings(
        self,
        deposit_amount: float,
        interest_rate: float,
        investment_term: int,  # in months
        interest_paid: InterestPaid,
    ) -> List[ProjectedSavingsIteration]:
        iterations = []

        for month in range(investment_term):
            monthly_balance = self.calculate_final_balance(
                deposit_amount=deposit_amount,
                interest_rate=interest_rate,
                investment_term=month + 1,
                interest_paid=interest_paid,
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
