import logging
from dataclasses import dataclass
from argparse import ArgumentParser
from typing import Literal

from .calculator import calculate_final_balance


@dataclass
class ProgramArgs:
    deposit: int
    interest_rate: float
    term_months: int
    paid_at: Literal["monthly", "quarterly", "annually", "maturity"]


def parse_args() -> ProgramArgs:
    parser = ArgumentParser(
        prog=f"python -m {__package__}",
        description="Calculate interest on a term deposit",
    )
    parser.add_argument(
        "--deposit",
        "-d",
        type=int,
        required=True,
        help="Amount of the initial deposit",
    )
    parser.add_argument(
        "--interest-rate",
        "-i",
        type=float,
        required=True,
        help="Interest rate as percentage, e.g. 1.1",
    )
    parser.add_argument(
        "--term-months",
        "-t",
        type=int,
        required=True,
        help="Term of the deposit in months",
    )
    parser.add_argument(
        "--paid-at",
        "-p",
        type=str,
        required=True,
        choices=("monthly", "quarterly", "annually", "maturity"),
        help="When the interest will be paid",
    )

    return ProgramArgs(**parser.parse_args().__dict__)


def main(deposit: int, interest_rate_percent: float, term_months: int, paid_at: Literal["monthly", "quarterly", "annually", "maturity"]) -> None:
    print("Term deposit calculator")
    print("---------------------------------------------")
    print(f"Deposit: {deposit}")
    print(f"Interest rate: {interest_rate_percent}%")
    print(f"Term: {term_months} months")
    print(f"Paid at: {paid_at}\n")

    final_balance = calculate_final_balance(
        deposit,
        interest_rate_percent,
        term_months,
        paid_at,
    )

    print("---------------------------------------------")
    print(f"Final balance: {final_balance}")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s:%(levelname)s:%(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    args = parse_args()
    main(
        args.deposit,
        args.interest_rate,
        args.term_months,
        args.paid_at
    )
