import pytest

from tdcalc.validation import validate_inputs


def test_validate_inputs():
    with pytest.raises(SystemExit):
        validate_inputs(8, "annually")
