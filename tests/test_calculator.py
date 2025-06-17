import pytest

from tdcalc.calculator import calculate_simple_interest, calculate_compound_interest


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
