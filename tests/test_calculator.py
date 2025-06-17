import pytest

from tdcalc.calculator import calculate_simple_interest, calculate_compound_interest, calculate_final_balance
from tdcalc.__main__ import validate_inputs


@pytest.mark.parametrize(
    "deposit, interest_rate, months, expected_result", [
        pytest.param(10_000, 0.011, 36, 330.0),
        pytest.param(25_500, 0.034, 8, 578.0)
    ]
)
def test_calculate_simple_interest(deposit, interest_rate, months, expected_result):
    result = calculate_simple_interest(deposit, interest_rate, months)

    assert result == expected_result


@pytest.mark.parametrize(
    "deposit, interest_rate, months, num_compounds_per_year, expected_result", [
        pytest.param(10_000, 0.011, 36, 4, 335.04),
        pytest.param(55_125, 0.034, 8, 12, 1261.96),
    ]
)
def test_calculate_compound_interest(deposit, interest_rate, months, num_compounds_per_year, expected_result):
    result = calculate_compound_interest(deposit, interest_rate, months, num_compounds_per_year)

    assert result == expected_result


def test_calculate_final_balance_simple_interest():
    result = calculate_final_balance(10_000, 1.1, 36, "maturity")

    assert result == 10_330


@pytest.mark.parametrize(
    "deposit, interest_rate, months, paid_at, expected_result", [
        pytest.param(55_125, 3.4, 8, "monthly", 56_386.96),
    ]
)
def test_calculate_final_balance_compound_interest_valid_paid_at_interval(deposit, interest_rate, months, paid_at, expected_result):
    result = calculate_final_balance(deposit, interest_rate, months, paid_at)

    assert result == expected_result


def test_validate_inputs():
    with pytest.raises(SystemExit):
        validate_inputs(8, "annually")
