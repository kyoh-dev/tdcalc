import pytest

from tdcalc.calculator import calculate_simple_interest


@pytest.mark.parametrize(
    "deposit, interest_rate, months, expected_result", [
        pytest.param(10_000, 0.011, 36, 330.0),
        pytest.param(25_500, 0.034, 8, 578.0)
    ]
)
def test_calculate_simple_interest(deposit, interest_rate, months, expected_result):
    result = calculate_simple_interest(deposit, interest_rate, months)

    assert result == expected_result
