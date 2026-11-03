import numpy as np
import pytest

from perfinpy import (
    beneficiary_share,
    first_payment_split,
    monthly_for_goal,
    months_to_fund,
    mortgage_payment,
    net_worth,
    rent_buy_threshold,
)


def test_monthly_for_goal():
    r = 0.04 / 12
    expected = 15000 * r / ((1 + r) ** 60 - 1)
    assert monthly_for_goal(15000, 0.04, 60) == pytest.approx(expected)
    assert monthly_for_goal(15000, 0, 60) == pytest.approx(250)
    with pytest.raises(ValueError, match="`months` must be greater than 0"):
        monthly_for_goal(15000, 0.04, 0)


def test_months_to_fund():
    assert (months_to_fund(3000, 600), months_to_fund(12000, 600)) == (5, 20)
    assert months_to_fund(3000, 700) == 5
    np.testing.assert_array_equal(months_to_fund([3000, 12000], 600), [5, 20])


def test_rent_buy_threshold():
    assert rent_buy_threshold(500000) == pytest.approx(25000 / 12)


def test_mortgage_payment():
    r = 0.005
    expected = 480000 * r * (1 + r) ** 360 / ((1 + r) ** 360 - 1)
    assert mortgage_payment(480000, 0.06, 30) == pytest.approx(expected)
    assert mortgage_payment(120000, 0, 30) == pytest.approx(120000 / 360)
    with pytest.raises(ValueError, match="`years` must be greater than 0"):
        mortgage_payment(480000, 0.06, 0)


def test_first_payment_split():
    out = first_payment_split(480000, 0.06, 30)
    assert out["interest"] == pytest.approx(2400)
    assert out["payment"] == pytest.approx(mortgage_payment(480000, 0.06, 30))
    assert out["principal"] == pytest.approx(out["payment"] - 2400)
    assert out["pct_interest"] == pytest.approx(2400 / out["payment"] * 100)
    with pytest.raises(ValueError, match="`years` must be a single number"):
        first_payment_split(480000, 0.06, [15, 30])


def test_net_worth():
    assets = {"401k": 12000, "roth_ira": 6000, "savings": 8000, "car": 9000}
    debts = {"car_loan": 6000, "credit_card": 1000}
    assert net_worth(assets, debts) == 28000
    assert net_worth([100, 200], []) == 300
    with pytest.raises(TypeError, match="`assets` must be numeric"):
        net_worth({"car": "9000"}, {})


def test_beneficiary_share():
    named = {"401k": 12000, "roth_ira": 6000, "life_insurance": 45000, "pod": 8000}
    assert beneficiary_share(named, {"car": 9000}) == pytest.approx(71 / 80)
    with pytest.raises(ValueError, match="Total assets must be greater than 0"):
        beneficiary_share({}, {})
