"""Functions from the High-Yield Savings Accounts chapter."""

from __future__ import annotations

from numpy.typing import ArrayLike

from ._checks import Numeric, _as_numeric


def hysa_balance(
    principal: ArrayLike, annual_apy: ArrayLike, years: ArrayLike = 1
) -> Numeric:
    """High-yield savings account balance.

    Grows `principal` at `annual_apy` for `years`. From the
    [High-Yield Savings Accounts](https://mjfrigaard.github.io/fm-finance/high_yield_accounts.html)
    chapter.

    Parameters
    ----------
    principal
        Starting balance.
    annual_apy
        Annual percentage yield, as a decimal.
    years
        Number of years. Defaults to 1.

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
    >>> from perfinpy import hysa_balance
    >>> # $9,600 at 4% APY after 1 and 5 years
    >>> hysa_balance(principal=9600, annual_apy=0.04, years=[1, 5])
    array([ 9984.        , 11679.86786304])
    """
    principal = _as_numeric(principal, "principal")
    annual_apy = _as_numeric(annual_apy, "annual_apy")
    years = _as_numeric(years, "years")
    return principal * (1 + annual_apy) ** years
