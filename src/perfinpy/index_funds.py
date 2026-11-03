"""Functions from the Index Funds chapter."""

from __future__ import annotations

from numpy.typing import ArrayLike

from ._checks import Numeric, _annuity_factor, _as_numeric


def yearly_fee(balance: ArrayLike, expense_ratio: ArrayLike) -> Numeric:
    """Yearly fund fee from an expense ratio.

    From the [Index Funds](https://mjfrigaard.github.io/fm-finance/index_funds.html)
    chapter.

    Parameters
    ----------
    balance
        Amount invested.
    expense_ratio
        Yearly expense ratio, as a decimal (`0.0004` is 0.04%).

    Returns
    -------
    float or numpy.ndarray
        Yearly fees.

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values.

    Examples
    --------
    >>> from perfinpy import yearly_fee
    >>> # $10,000 in an index fund vs. an active fund
    >>> yearly_fee(balance=10000, expense_ratio=[0.0004, 0.01])
    array([  4., 100.])
    """
    balance = _as_numeric(balance, "balance")
    expense_ratio = _as_numeric(expense_ratio, "expense_ratio")
    return balance * expense_ratio


def future_value_after_fees(
    contribution: ArrayLike,
    annual_return: ArrayLike,
    expense_ratio: ArrayLike,
    years: ArrayLike,
) -> Numeric:
    """Future value of monthly contributions after fund fees.

    Subtracts the expense ratio from the yearly return, then compounds
    monthly contributions. From the
    [Index Funds](https://mjfrigaard.github.io/fm-finance/index_funds.html)
    chapter.

    Parameters
    ----------
    contribution
        Amount contributed each month.
    annual_return
        Yearly return before fees, as a decimal.
    expense_ratio
        Yearly expense ratio, as a decimal.
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
    >>> from perfinpy import future_value_after_fees
    >>> # $300/month for 40 years at 7%, index fund vs. active fund
    >>> future_value_after_fees(300, 0.07, [0.0004, 0.01], 40)
    array([778654.71, 597447.22])
    """
    contribution = _as_numeric(contribution, "contribution")
    annual_return = _as_numeric(annual_return, "annual_return")
    expense_ratio = _as_numeric(expense_ratio, "expense_ratio")
    years = _as_numeric(years, "years")
    rate = (annual_return - expense_ratio) / 12
    return contribution * _annuity_factor(rate, years * 12)
