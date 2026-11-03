import numpy as np
import polars as pl
import pytest

from perfinpy import (
    after_tax_value,
    employer_match,
    future_value,
    future_value_after_fees,
    future_value_series,
    portfolio_return,
    real_return,
    rebalance_amount,
    rule_of_72,
    yearly_fee,
)


def test_future_value():
    assert future_value(10000, 0.07, 10) == pytest.approx(19671.51, abs=0.01)
    out = future_value(10000, 0.07, np.array([5, 10, 20, 30]))
    np.testing.assert_allclose(out, 10000 * 1.07 ** np.array([5, 10, 20, 30]))


def test_rule_of_72():
    assert rule_of_72(7) == pytest.approx(72 / 7)
    with pytest.raises(ValueError, match="`annual_return_pct` must be greater"):
        rule_of_72(0)


def test_future_value_series():
    r = 0.07 / 12
    expected = 500 * ((1 + r) ** 360 - 1) / r
    assert future_value_series(500, r, 360) == pytest.approx(expected)
    assert future_value_series(500, 0, 360) == pytest.approx(180000)


def test_real_return():
    assert real_return(0.07, 0.03) == pytest.approx(1.07 / 1.03 - 1)
    assert real_return(0.03, 0.03) == pytest.approx(0)


def test_employer_match():
    assert employer_match(45000, 0.06, 0.06, 0.50) == pytest.approx(1350)
    assert employer_match(45000, 0.03, 0.06, 0.50) == pytest.approx(675)
    assert employer_match(45000, 0.10, 0.06, 0.50) == pytest.approx(1350)


def test_after_tax_value():
    assert after_tax_value(1000, 0.12, 0.07, 40) == pytest.approx(880 * 1.07**40)
    assert after_tax_value(1000, 0.22, 0.07, 0) == pytest.approx(780)


def test_yearly_fee():
    np.testing.assert_allclose(yearly_fee(10000, np.array([0.0004, 0.01])), [4, 100])


def test_future_value_after_fees():
    r = (0.07 - 0.0004) / 12
    expected = 300 * ((1 + r) ** 480 - 1) / r
    assert future_value_after_fees(300, 0.07, 0.0004, 40) == pytest.approx(expected)
    assert future_value_after_fees(300, 0.01, 0.01, 40) == pytest.approx(144000)


def test_portfolio_return():
    assert portfolio_return(0.8, 0.10, 0.04) == pytest.approx(0.088)
    np.testing.assert_allclose(portfolio_return([1, 0.6], -0.40, 0), [-0.40, -0.24])


def test_portfolio_return_polars_expression():
    out = pl.DataFrame({"stocks": [1.0, 0.8, 0.6]}).with_columns(
        average=portfolio_return(pl.col("stocks"), 0.10, 0.04),
    )
    np.testing.assert_allclose(out["average"].to_numpy(), [0.10, 0.088, 0.076])


def test_rebalance_amount():
    assert rebalance_amount(0.80, 7600, 5600) == pytest.approx(480)
    assert rebalance_amount(0.20, 7600, 2000) == pytest.approx(-480)
    with pytest.raises(ValueError, match="missing values"):
        rebalance_amount(0.80, float("nan"), 5600)
