import numpy as np
import pytest

from perfinpy import (
    ef_growth,
    emergency_fund_target,
    monthly_contribution_needed,
    months_to_ef_goal,
)


def test_emergency_fund_target():
    assert emergency_fund_target(2400) == 7200
    np.testing.assert_array_equal(emergency_fund_target(2400, [3, 6]), [7200, 14400])


def test_months_to_ef_goal():
    out = months_to_ef_goal(9600, 1200, 400)
    assert out == 21
    assert isinstance(out, int)
    assert months_to_ef_goal(9600, 10000, 400) == 0
    np.testing.assert_array_equal(months_to_ef_goal(9600, [1200, 9500], 400), [21, 1])
    with pytest.raises(ValueError, match="`monthly_contribution` must be greater"):
        months_to_ef_goal(9600, 1200, 0)


def test_monthly_contribution_needed():
    assert monthly_contribution_needed(9600, 1200, 18) == 467
    assert monthly_contribution_needed(9600, 9600, 18) == 0
    with pytest.raises(ValueError, match="`months` must be greater than 0"):
        monthly_contribution_needed(9600, 1200, 0)


def test_ef_growth():
    assert ef_growth(9600, 0.04, 12) == pytest.approx(9984)
    assert ef_growth(9600, 0.04, 0) == 9600
    assert ef_growth(9600, 0.04, 6) == pytest.approx(9600 * 1.04**0.5)
