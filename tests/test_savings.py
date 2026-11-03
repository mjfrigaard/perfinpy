import numpy as np
import pytest

from perfinpy import hysa_balance, monthly_savings, savings_rate


def test_savings_rate():
    assert savings_rate(3200, 2720) == pytest.approx(15)
    assert savings_rate(3200, 3520) == pytest.approx(-10)
    with pytest.raises(ValueError, match="`income` must be greater than 0"):
        savings_rate(0, 100)


def test_hysa_balance():
    assert hysa_balance(9600, 0.04) == pytest.approx(9984)
    assert hysa_balance(9600, 0.04, 5) == pytest.approx(11679.87, abs=0.01)
    np.testing.assert_allclose(hysa_balance(9600, [0, 0.04]), [9600, 9984])


def test_monthly_savings():
    assert monthly_savings(4000, 0.20) == pytest.approx(800)
    with pytest.raises(TypeError, match="`savings_rate` must be numeric"):
        monthly_savings(4000, "20%")
