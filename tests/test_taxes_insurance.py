import numpy as np
import pytest

from perfinpy import break_even_years, income_tax, plan_cost, raise_kept


def test_income_tax():
    assert income_tax(45000) == pytest.approx(1240 + 16500 * 0.12)
    assert income_tax(10000) == 0
    assert income_tax(16100 + 12400) == pytest.approx(1240)
    assert income_tax(45000, deduction=0) == pytest.approx(1240 + 32600 * 0.12)


def test_income_tax_is_scalar():
    with pytest.raises(ValueError, match="`income` must be a single number"):
        income_tax([45000, 50000])


def test_raise_kept():
    assert raise_kept(66000, 2000) == pytest.approx(2000 - (6130 - 5740))
    assert raise_kept(10000, 2000) == pytest.approx(2000)


def test_break_even_years():
    assert break_even_years(1000, 500, 150) == pytest.approx(10 / 3)
    with pytest.raises(ValueError, match="`yearly_savings` must be greater than 0"):
        break_even_years(1000, 500, 0)


def test_plan_cost():
    assert plan_cost(100, 300, 3000) == pytest.approx(1500)
    assert plan_cost(40, 300, 5000, employer_hsa=500) == pytest.approx(280)
    np.testing.assert_allclose(plan_cost(100, [300, float("inf")], 3000), [1500, 4200])
