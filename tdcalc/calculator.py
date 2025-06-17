from typing import Literal

COMPOUNDS_PER_YEAR = {
    "monthly": 12,
    "quarterly": 4,
    "annually": 1,
}


def calculate_simple_interest(deposit: float, interest_rate: float, months: int) -> float:
    interest = deposit * interest_rate * (months / 12)

    return round(interest, 2)


def calculate_compound_interest(deposit: float, interest_rate: float, months: int, num_compounds_per_year: int) -> float:
    total = deposit * (1 + interest_rate / num_compounds_per_year) ** (num_compounds_per_year * (months / 12))

    return round(total - deposit, 2)


def calculate_final_balance(
    deposit: float,
    interest_rate_percent: float,
    months: int,
    paid_at: Literal["monthly", "quarterly", "annually", "maturity"],
) -> float:
    interest_rate = interest_rate_percent / 100

    if paid_at == "maturity":
        interest = calculate_simple_interest(deposit, interest_rate, months)
    else:
        interest = calculate_compound_interest(deposit, interest_rate, months, num_compounds_per_year=COMPOUNDS_PER_YEAR[paid_at])

    return deposit + interest
