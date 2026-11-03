"""Functions from the Budgeting chapter."""

from __future__ import annotations

from typing import Literal

from numpy.typing import ArrayLike

from ._checks import Numeric, _as_numeric, _as_positive


def percent_of_income(expense: ArrayLike, income: ArrayLike) -> Numeric:
    """An expense as a percent of income.

    `expense` and `income` must cover the same period. From the
    [Budgeting](https://mjfrigaard.github.io/fm-finance/budgeting.html)
    chapter.

    Parameters
    ----------
    expense
        Amount spent.
    income
        Income for the same period. Must be greater than 0.

    Returns
    -------
    float or numpy.ndarray
        Percentages (`30` is 30%).

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values, or `income` is not greater
        than 0.

    Examples
    --------
    >>> from perfinpy import percent_of_income
    >>> percent_of_income(expense=1500, income=5000)
    30.0
    """
    expense = _as_numeric(expense, "expense")
    income = _as_positive(income, "income")
    return (expense / income) * 100


def to_annual(
    amount: ArrayLike, period: Literal["daily", "weekly", "monthly"] = "daily"
) -> Numeric:
    """Convert a daily, weekly, or monthly amount to a yearly amount.

    Uses 365 days, 52 weeks, and 12 months per year. From the
    [Budgeting](https://mjfrigaard.github.io/fm-finance/budgeting.html)
    chapter.

    Parameters
    ----------
    amount
        Amount per `period`.
    period
        One of `"daily"`, `"weekly"`, or `"monthly"`.

    Returns
    -------
    float or numpy.ndarray
        Yearly amounts.

    Raises
    ------
    TypeError
        If `amount` is not numeric.
    ValueError
        If `amount` contains missing values, or `period` is not one of the
        choices.

    See Also
    --------
    to_monthly : Convert to a monthly amount.

    Examples
    --------
    >>> from perfinpy import to_annual
    >>> # $5 a day coffee
    >>> to_annual(amount=5, period="daily")
    1825.0
    """
    factors = {"daily": 365, "weekly": 52, "monthly": 12}
    if period not in factors:
        raise ValueError("`period` must be one of 'daily', 'weekly', 'monthly'.")
    return _as_numeric(amount, "amount") * factors[period]


def to_monthly(
    amount: ArrayLike, period: Literal["daily", "weekly", "annual"] = "daily"
) -> Numeric:
    """Convert a daily, weekly, or yearly amount to a monthly amount.

    Uses the book's rounded factors: 30.44 days and 4.33 weeks per month, so
    a round trip through `to_annual()` drifts slightly. From the
    [Budgeting](https://mjfrigaard.github.io/fm-finance/budgeting.html)
    chapter.

    Parameters
    ----------
    amount
        Amount per `period`.
    period
        One of `"daily"`, `"weekly"`, or `"annual"`.

    Returns
    -------
    float or numpy.ndarray
        Monthly amounts.

    Raises
    ------
    TypeError
        If `amount` is not numeric.
    ValueError
        If `amount` contains missing values, or `period` is not one of the
        choices.

    See Also
    --------
    to_annual : Convert to a yearly amount.

    Examples
    --------
    >>> from perfinpy import to_monthly
    >>> # $150 a week in groceries
    >>> to_monthly(amount=150, period="weekly")
    649.5
    """
    factors = {"daily": 30.44, "weekly": 4.33, "annual": 1 / 12}
    if period not in factors:
        raise ValueError("`period` must be one of 'daily', 'weekly', 'annual'.")
    return _as_numeric(amount, "amount") * factors[period]


def opportunity_cost(amount: ArrayLike, rate: ArrayLike, years: ArrayLike) -> Numeric:
    """What an amount could grow to if invested instead of spent.

    Compounds `amount` once a year at `rate`. From the
    [Budgeting](https://mjfrigaard.github.io/fm-finance/budgeting.html)
    chapter.

    Parameters
    ----------
    amount
        Amount spent today.
    rate
        Yearly return, as a decimal.
    years
        Number of years.

    Returns
    -------
    float or numpy.ndarray
        Future values.

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values.

    Examples
    --------
    >>> from perfinpy import opportunity_cost
    >>> # $25,000 saved on a car, invested at 7% for 30 years
    >>> opportunity_cost(amount=25000, rate=0.07, years=30)
    190306.37
    """
    amount = _as_numeric(amount, "amount")
    rate = _as_numeric(rate, "rate")
    years = _as_numeric(years, "years")
    return amount * (1 + rate) ** years


def months_to_break_even(
    upfront_cost: ArrayLike, monthly_savings: ArrayLike
) -> Numeric:
    """Months until monthly savings cover an upfront cost.

    The result is not rounded. From the
    [Budgeting](https://mjfrigaard.github.io/fm-finance/budgeting.html)
    chapter.

    Parameters
    ----------
    upfront_cost
        Cost paid today.
    monthly_savings
        Amount saved each month. Must be greater than 0.

    Returns
    -------
    float or numpy.ndarray
        Months.

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values, or `monthly_savings` is not
        greater than 0.

    Examples
    --------
    >>> from perfinpy import months_to_break_even
    >>> # $500 membership that saves $60 a month
    >>> months_to_break_even(upfront_cost=500, monthly_savings=60)
    8.33
    """
    upfront_cost = _as_numeric(upfront_cost, "upfront_cost")
    monthly_savings = _as_positive(monthly_savings, "monthly_savings")
    return upfront_cost / monthly_savings
