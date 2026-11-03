"""Functions from the Financial Goals chapter."""

from __future__ import annotations

from numpy.typing import ArrayLike

from ._checks import Numeric, Whole, _annuity_factor, _as_numeric, _as_positive, _ceil


def monthly_for_goal(
    goal: ArrayLike, annual_rate: ArrayLike, months: ArrayLike
) -> Numeric:
    """Monthly saving needed to reach a goal.

    Solves the future value of a series for the contribution, compounding
    monthly at `annual_rate / 12`. A 0% rate gives `goal / months`. From the
    [Financial Goals](https://mjfrigaard.github.io/fm-finance/financial_goals.html)
    chapter.

    Parameters
    ----------
    goal
        Amount needed.
    annual_rate
        Yearly return on savings, as a decimal.
    months
        Months until the goal. Must be greater than 0.

    Returns
    -------
    float or numpy.ndarray
        Monthly contributions.

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values, or `months` is not greater
        than 0.

    Examples
    --------
    >>> from perfinpy import monthly_for_goal
    >>> # $15,000 in 5 years at 4%, compared to no interest
    >>> monthly_for_goal(goal=15000, annual_rate=[0.04, 0], months=60)
    array([226.24783083, 250.        ])
    """
    goal = _as_numeric(goal, "goal")
    annual_rate = _as_numeric(annual_rate, "annual_rate")
    months = _as_positive(months, "months")
    return goal / _annuity_factor(annual_rate / 12, months)


def months_to_fund(goal: ArrayLike, monthly: ArrayLike) -> Whole:
    """Whole months to fund a goal with no interest.

    From the [Financial Goals](https://mjfrigaard.github.io/fm-finance/financial_goals.html)
    chapter.

    Parameters
    ----------
    goal
        Amount needed.
    monthly
        Amount saved each month. Must be greater than 0.

    Returns
    -------
    int or numpy.ndarray
        Whole months, rounded up.

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values, or `monthly` is not greater
        than 0.

    Examples
    --------
    >>> from perfinpy import months_to_fund
    >>> # one at a time: a $3,000 trip, then a $9,000 car, at $600/month
    >>> months_to_fund(3000, 600), months_to_fund(3000 + 9000, 600)
    (5, 20)
    """
    goal = _as_numeric(goal, "goal")
    monthly = _as_positive(monthly, "monthly")
    return _ceil(goal / monthly)
