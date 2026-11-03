"""Functions from the Insurance chapter."""

from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike

from ._checks import Numeric, _as_numeric, _as_positive, _out


def break_even_years(
    high_deductible: ArrayLike, low_deductible: ArrayLike, yearly_savings: ArrayLike
) -> Numeric:
    """Years of premium savings to cover a higher deductible.

    If you go longer than this between claims, the higher deductible comes
    out ahead. From the
    [Insurance](https://mjfrigaard.github.io/fm-finance/insurance.html)
    chapter.

    Parameters
    ----------
    high_deductible
        The higher deductible.
    low_deductible
        The lower deductible.
    yearly_savings
        Yearly premium saved by choosing the higher deductible. Must be
        greater than 0.

    Returns
    -------
    float or numpy.ndarray
        Years.

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values, or `yearly_savings` is not
        greater than 0.

    Examples
    --------
    >>> from perfinpy import break_even_years
    >>> break_even_years(high_deductible=1000, low_deductible=500,
    ...                  yearly_savings=150)
    3.33
    """
    high_deductible = _as_numeric(high_deductible, "high_deductible")
    low_deductible = _as_numeric(low_deductible, "low_deductible")
    yearly_savings = _as_positive(yearly_savings, "yearly_savings")
    return (high_deductible - low_deductible) / yearly_savings


def plan_cost(
    monthly_premium: ArrayLike,
    medical_cost: ArrayLike,
    oop_max: ArrayLike,
    employer_hsa: ArrayLike = 0,
) -> Numeric:
    """Yearly cost of a health plan.

    Twelve premiums plus what you pay for care (capped at the out of pocket
    maximum), minus any employer HSA contribution. Use `float("inf")` for
    `medical_cost` to get the worst case year. From the
    [Insurance](https://mjfrigaard.github.io/fm-finance/insurance.html)
    chapter.

    Parameters
    ----------
    monthly_premium
        Monthly premium.
    medical_cost
        Medical costs for the year.
    oop_max
        Out of pocket maximum.
    employer_hsa
        Employer HSA contribution. Defaults to 0.

    Returns
    -------
    float or numpy.ndarray
        Yearly costs.

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values.

    Examples
    --------
    >>> from perfinpy import plan_cost
    >>> # Plan A in a healthy year ($300 of care) and the worst year
    >>> plan_cost(100, [300, float("inf")], oop_max=3000)
    array([1500., 4200.])
    >>> # Plan B, with a $500 employer HSA contribution
    >>> plan_cost(40, [300, float("inf")], oop_max=5000, employer_hsa=500)
    array([ 280., 4980.])
    """
    monthly_premium = _as_numeric(monthly_premium, "monthly_premium")
    medical_cost = _as_numeric(medical_cost, "medical_cost")
    oop_max = _as_numeric(oop_max, "oop_max")
    employer_hsa = _as_numeric(employer_hsa, "employer_hsa")
    return _out(monthly_premium * 12 + np.minimum(medical_cost, oop_max) - employer_hsa)
