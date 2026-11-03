"""Functions from the Savings Strategies chapter."""

from __future__ import annotations

from numpy.typing import ArrayLike

from ._checks import Numeric, _as_numeric, _as_positive


def savings_rate(income: ArrayLike, spending: ArrayLike) -> Numeric:
    """Savings rate: the percent of income not spent.

    From the [Savings Strategies](https://mjfrigaard.github.io/fm-finance/savings_strategies.html)
    chapter.

    Parameters
    ----------
    income
        Income for the period. Must be greater than 0.
    spending
        Spending for the same period.

    Returns
    -------
    float or numpy.ndarray
        Percentages (`15` is 15%). Negative when spending exceeds income.

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values, or `income` is not greater
        than 0.

    Examples
    --------
    >>> from perfinpy import savings_rate
    >>> savings_rate(income=3200, spending=2720)
    15.0
    """
    income = _as_positive(income, "income")
    spending = _as_numeric(spending, "spending")
    return ((income - spending) / income) * 100
