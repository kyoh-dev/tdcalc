from tdcalc.calculator import calculate_simple_interest

def test_calculate_simple_interest():
    result = calculate_simple_interest(10_000, 0.011, 3)

    assert result == 330.0
