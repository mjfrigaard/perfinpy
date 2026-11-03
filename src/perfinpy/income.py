"""Functions from the Income chapter."""

from __future__ import annotations

from numpy.typing import ArrayLike

from ._checks import Numeric, _annuity_factor, _as_numeric, _as_positive


def wealth_formula(
    median_income: ArrayLike,
    savings_rate: ArrayLike,
    annual_return: ArrayLike,
    years: ArrayLike,
) -> Numeric:
    """Wealth from saving part of an income every year.

    The future value of saving `median_income * savings_rate` at the end of
    each year (contributions plus growth). From the
    [Income](https://mjfrigaard.github.io/fm-finance/income.html) chapter.

    Parameters
    ----------
    median_income
        Yearly income.
    savings_rate
        Share of income saved, as a decimal.
    annual_return
        Yearly return, as a decimal. A 0% return gives the sum of the
        contributions.
    years
        Number of years.

    Returns
    -------
    float or numpy.ndarray
        Ending balances.

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values.

    See Also
    --------
    raise_invested_value : Monthly version for investing part of a raise.

    Examples
    --------
    >>> from perfinpy import wealth_formula
    >>> # $45,000 income, 20% saved, 7% return, 30 years
    >>> wealth_formula(45000, savings_rate=0.20, annual_return=0.07, years=30)
    850147.07
    """
    median_income = _as_numeric(median_income, "median_income")
    savings_rate = _as_numeric(savings_rate, "savings_rate")
    annual_return = _as_numeric(annual_return, "annual_return")
    years = _as_numeric(years, "years")
    annual_savings = median_income * savings_rate
    return annual_savings * _annuity_factor(annual_return, years)


def fixed_cost_ratio(fixed_costs: ArrayLike, take_home: ArrayLike) -> Numeric:
    """Fixed costs as a percent of take home pay.

    From the [Income](https://mjfrigaard.github.io/fm-finance/income.html)
    chapter.

    Parameters
    ----------
    fixed_costs
        Monthly fixed costs (rent, insurance, loan payments).
    take_home
        Monthly take home pay. Must be greater than 0.

    Returns
    -------
    float or numpy.ndarray
        Percentages (`56.25` is 56.25%).

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values, or `take_home` is not
        greater than 0.

    Examples
    --------
    >>> from perfinpy import fixed_cost_ratio
    >>> fixed_cost_ratio(fixed_costs=1800, take_home=3200)
    56.25
    """
    fixed_costs = _as_numeric(fixed_costs, "fixed_costs")
    take_home = _as_positive(take_home, "take_home")
    return (fixed_costs / take_home) * 100


def raise_invested_value(
    monthly_raise: ArrayLike,
    invest_share: ArrayLike,
    rate: ArrayLike,
    years: ArrayLike,
) -> Numeric:
    """Future value of investing part of a raise.

    Invests `monthly_raise * invest_share` every month, compounded monthly.
    From the [Income](https://mjfrigaard.github.io/fm-finance/income.html)
    chapter.

    Parameters
    ----------
    monthly_raise
        Monthly increase in take home pay.
    invest_share
        Share of the raise invested, as a decimal.
    rate
        Yearly return, as a decimal.
    years
        Number of years.

    Returns
    -------
    float or numpy.ndarray
        Ending balances.

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values.

    See Also
    --------
    wealth_formula : Yearly version for saving part of an income.

    Examples
    --------
    >>> from perfinpy import raise_invested_value
    >>> # invest half of a $200/month raise at 7% for 30 years
    >>> raise_invested_value(200, invest_share=0.5, rate=0.07, years=30)
    121997.09
    """
    monthly_raise = _as_numeric(monthly_raise, "monthly_raise")
    invest_share = _as_numeric(invest_share, "invest_share")
    rate = _as_numeric(rate, "rate")
    years = _as_numeric(years, "years")
    contribution = monthly_raise * invest_share
    return contribution * _annuity_factor(rate / 12, years * 12)
