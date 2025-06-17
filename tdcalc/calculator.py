def calculate_simple_interest(deposit: float, interest_rate: float, months: int) -> float:
    return deposit * interest_rate * (months / 12)


def calculate_compound_interest(deposit: float, interest_rate: float, months: int, num_compounds_per_year: int) -> float:
    ...
