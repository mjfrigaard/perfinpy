import numpy as np
import pytest

from perfinpy import fixed_cost_ratio, raise_invested_value, wealth_formula


def test_wealth_formula():
    expected = 9000 * (1.07**30 - 1) / 0.07
    assert wealth_formula(45000, 0.20, 0.07, 30) == pytest.approx(expected)
    assert wealth_formula(45000, 0.20, 0, 30) == pytest.approx(270000)
    np.testing.assert_allclose(wealth_formula(45000, 0.20, [0, 0.07], 1), [9000, 9000])


def test_fixed_cost_ratio():
    assert fixed_cost_ratio(1800, 3200) == pytest.approx(56.25)
    np.testing.assert_allclose(fixed_cost_ratio([800, 1600], 3200), [25, 50])
    with pytest.raises(ValueError, match="`take_home` must be greater than 0"):
        fixed_cost_ratio(1800, 0)


def test_raise_invested_value():
    r = 0.07 / 12
    expected = 100 * ((1 + r) ** 360 - 1) / r
    assert raise_invested_value(200, 0.5, 0.07, 30) == pytest.approx(expected)
    assert raise_invested_value(200, 0.5, 0, 30) == pytest.approx(36000)
    with pytest.raises(TypeError, match="`rate` must be numeric"):
        raise_invested_value(200, 0.5, "7%", 30)
