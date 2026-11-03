import numpy as np
import pytest

from perfinpy import (
    months_to_break_even,
    opportunity_cost,
    percent_of_income,
    to_annual,
    to_monthly,
)


def test_percent_of_income():
    assert percent_of_income(1500, 5000) == pytest.approx(30)
    assert percent_of_income(960, 3200) == pytest.approx(30)
    np.testing.assert_allclose(percent_of_income([500, 1000], 5000), [10, 20])
    with pytest.raises(ValueError, match="`income` must be greater than 0"):
        percent_of_income(1500, 0)


def test_to_annual():
    assert to_annual(5) == 1825
    assert to_annual(100, "weekly") == 5200
    assert to_annual(100, "monthly") == 1200
    with pytest.raises(ValueError, match="`period` must be one of"):
        to_annual(5, "hourly")


def test_to_monthly():
    assert to_monthly(5) == pytest.approx(152.2)
    assert to_monthly(150, "weekly") == pytest.approx(649.5)
    assert to_monthly(1200, "annual") == pytest.approx(100)
    np.testing.assert_allclose(to_monthly([1, 2], "weekly"), [4.33, 8.66])


def test_opportunity_cost():
    assert opportunity_cost(25000, 0.07, 30) == pytest.approx(25000 * 1.07**30)
    assert opportunity_cost(25000, 0.07, 0) == 25000


def test_months_to_break_even():
    assert months_to_break_even(500, 60) == pytest.approx(25 / 3)
    with pytest.raises(ValueError, match="`monthly_savings` must be greater than 0"):
        months_to_break_even(500, 0)
