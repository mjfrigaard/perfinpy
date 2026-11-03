import math

import numpy as np
import pytest

from perfinpy import (
    apr_to_apy,
    credit_utilization,
    dti_ratio,
    idr_monthly_payment,
    loan_income_ratio,
    monthly_standard_payment,
    months_to_payoff,
    mortgage_payment,
    order_avalanche,
    order_snowball,
    payoff_vs_invest,
    total_interest,
)

debts = [
    {"name": "Card A", "balance": 1000, "apr": 0.18},
    {"name": "Card B", "balance": 5000, "apr": 0.24},
    {"name": "Card C", "balance": 2000, "apr": 0.15},
]


def test_apr_to_apy():
    assert apr_to_apy(0.24) == pytest.approx((1 + 0.24 / 365) ** 365 - 1)
    assert apr_to_apy(0.12, 12) == pytest.approx(1.01**12 - 1)
    with pytest.raises(ValueError, match="`periods_per_year` must be greater than 0"):
        apr_to_apy(0.24, 0)


def test_months_to_payoff():
    r = 0.22 / 12
    expected = -math.log(1 - r * 50) / math.log(1 + r)
    assert months_to_payoff(5000, 100, 0.22) == pytest.approx(expected)
    assert months_to_payoff(5000, 100, 0) == pytest.approx(50)
    np.testing.assert_allclose(months_to_payoff(5000, 100, [0, 0.22]), [50, expected])


def test_months_to_payoff_payment_too_small():
    with pytest.raises(ValueError, match="larger than the monthly interest"):
        months_to_payoff(5000, 50, 0.22)


def test_total_interest():
    assert total_interest(340.98, 72, 20000) == pytest.approx(4550.56)
    assert total_interest(478.92, 48, 20000) == pytest.approx(2988.16)


def test_loan_income_ratio():
    assert loan_income_ratio(45000, 42000) == pytest.approx(45 / 42)
    with pytest.raises(ValueError, match="`expected_salary` must be greater than 0"):
        loan_income_ratio(45000, 0)


def test_monthly_standard_payment():
    r = 0.065 / 12
    expected = 45000 * r * (1 + r) ** 120 / ((1 + r) ** 120 - 1)
    assert monthly_standard_payment(45000) == pytest.approx(expected)
    assert monthly_standard_payment(45000) == mortgage_payment(45000, 0.065, 10)


def test_idr_monthly_payment():
    assert idr_monthly_payment(50000) == 217.17
    assert idr_monthly_payment(50000, payment_rate=0.15) == 325.75
    np.testing.assert_array_equal(idr_monthly_payment([20000, 50000]), [0, 217.17])


def test_dti_ratio():
    assert dti_ratio(1061, 3750) == pytest.approx(106100 / 3750)
    with pytest.raises(ValueError, match="`gross_monthly_income`"):
        dti_ratio(1061, -1)


def test_payoff_vs_invest():
    assert payoff_vs_invest(0.05, 0.07) == "Invest the difference"
    assert payoff_vs_invest(0.22, 0.07) == "Pay off the debt"
    assert payoff_vs_invest(0.07, 0.07) == "Roughly a wash; do both"
    with pytest.raises(ValueError, match="`loan_rate` must be a single number"):
        payoff_vs_invest([0.05, 0.08], 0.07)


def test_order_avalanche():
    assert [d["name"] for d in order_avalanche(debts)] == ["Card B", "Card A", "Card C"]
    assert [d["name"] for d in debts] == ["Card A", "Card B", "Card C"]
    assert order_avalanche([]) == []


def test_order_snowball():
    assert [d["name"] for d in order_snowball(debts)] == ["Card A", "Card C", "Card B"]


def test_order_bad_inputs():
    with pytest.raises(ValueError, match="`apr` key"):
        order_avalanche([{"balance": 1}])
    with pytest.raises(TypeError, match="list of dicts"):
        order_snowball({"balance": 1})
    with pytest.raises(TypeError, match="`balance` must be numeric"):
        order_snowball([{"balance": "1000"}])


def test_credit_utilization():
    assert credit_utilization(900, 3000) == pytest.approx(30)
    np.testing.assert_allclose(credit_utilization([300, 900], 3000), [10, 30])
    with pytest.raises(ValueError, match="`credit_limit` must be greater than 0"):
        credit_utilization(900, 0)


def test_idr_monthly_payment_rounds_like_python():
    assert idr_monthly_payment(24021) == round((24021 - 23940) * 0.1 / 12, 2)
