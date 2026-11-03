"""Functions from the Emergency Fund chapter."""

from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike

from ._checks import Numeric, Whole, _as_numeric, _as_positive, _ceil


def emergency_fund_target(
    monthly_expenses: ArrayLike, months: ArrayLike = 3
) -> Numeric:
    """Emergency fund target.

    Essential monthly expenses times the number of months to cover. From the
    [Emergency Fund](https://mjfrigaard.github.io/fm-finance/emergency_fund.html)
    chapter.

    Parameters
    ----------
    monthly_expenses
        Essential monthly expenses.
    months
        Months of expenses to cover. Defaults to 3.

    Returns
    -------
    float or numpy.ndarray
        Target balances.

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values.

    Examples
    --------
    >>> from perfinpy import emergency_fund_target
    >>> # 3-month and 6-month targets on $2,400/month
    >>> emergency_fund_target(monthly_expenses=2400, months=[3, 6])
    array([ 7200., 14400.])
    """
    monthly_expenses = _as_numeric(monthly_expenses, "monthly_expenses")
    months = _as_numeric(months, "months")
    return monthly_expenses * months


def months_to_ef_goal(
    target: ArrayLike, current_balance: ArrayLike, monthly_contribution: ArrayLike
) -> Whole:
    """Months to reach an emergency fund target.

    Rounded up to whole months. Returns 0 when the fund is already at or
    above the target. From the
    [Emergency Fund](https://mjfrigaard.github.io/fm-finance/emergency_fund.html)
    chapter.

    Parameters
    ----------
    target
        Target balance.
    current_balance
        Amount already saved.
    monthly_contribution
        Amount added each month. Must be greater than 0.

    Returns
    -------
    int or numpy.ndarray
        Whole months.

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values, or `monthly_contribution` is
        not greater than 0.

    See Also
    --------
    monthly_contribution_needed : Solve for the contribution instead.

    Examples
    --------
    >>> from perfinpy import months_to_ef_goal
    >>> months_to_ef_goal(target=9600, current_balance=1200,
    ...                   monthly_contribution=400)
    21
    """
    target = _as_numeric(target, "target")
    current_balance = _as_numeric(current_balance, "current_balance")
    monthly_contribution = _as_positive(monthly_contribution, "monthly_contribution")
    remaining = np.maximum(0, target - current_balance)
    return _ceil(remaining / monthly_contribution)


def monthly_contribution_needed(
    target: ArrayLike, current_balance: ArrayLike, months: ArrayLike
) -> Whole:
    """Monthly contribution needed to reach an emergency fund target.

    Rounded up to whole dollars. Returns 0 when the fund is already at or
    above the target. From the
    [Emergency Fund](https://mjfrigaard.github.io/fm-finance/emergency_fund.html)
    chapter.

    Parameters
    ----------
    target
        Target balance.
    current_balance
        Amount already saved.
    months
        Months to reach the target. Must be greater than 0.

    Returns
    -------
    int or numpy.ndarray
        Whole dollars per month.

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values, or `months` is not greater
        than 0.

    See Also
    --------
    months_to_ef_goal : Solve for the months instead.

    Examples
    --------
    >>> from perfinpy import monthly_contribution_needed
    >>> monthly_contribution_needed(target=9600, current_balance=1200, months=18)
    467
    """
    target = _as_numeric(target, "target")
    current_balance = _as_numeric(current_balance, "current_balance")
    months = _as_positive(months, "months")
    remaining = np.maximum(0, target - current_balance)
    return _ceil(remaining / months)


def ef_growth(balance: ArrayLike, apy: ArrayLike, months: ArrayLike) -> Numeric:
    """Emergency fund balance after earning interest.

    Grows `balance` at `apy` for `months / 12` years. From the
    [Emergency Fund](https://mjfrigaard.github.io/fm-finance/emergency_fund.html)
    chapter.

    Parameters
    ----------
    balance
        Starting balance.
    apy
        Annual percentage yield, as a decimal.
    months
        Number of months.

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

    Examples
    --------
    >>> from perfinpy import ef_growth
    >>> ef_growth(balance=9600, apy=0.04, months=12)
    9984.0
    """
    balance = _as_numeric(balance, "balance")
    apy = _as_numeric(apy, "apy")
    months = _as_numeric(months, "months")
    return balance * (1 + apy) ** (months / 12)
