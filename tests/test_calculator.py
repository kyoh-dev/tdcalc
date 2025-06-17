from tdcalc.calculator import calculate_compound_interest

def test_calculate_compound_interest():
    result = calculate_compound_interest()

    assert result == 330
