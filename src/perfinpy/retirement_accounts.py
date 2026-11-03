"""Functions from the Retirement Accounts chapter."""

from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike

from ._checks import Numeric, _as_numeric, _out


def employer_match(
    salary: ArrayLike,
    contribution_pct: ArrayLike,
    match_limit_pct: ArrayLike,
    match_rate: ArrayLike,
) -> Numeric:
    """Yearly employer match on retirement contributions.

    The employer matches `match_rate` of your contributions, up to
    `match_limit_pct` of salary. From the
    [Retirement Accounts](https://mjfrigaard.github.io/fm-finance/retirement_accounts.html)
    chapter.

    Parameters
    ----------
    salary
        Yearly salary.
    contribution_pct
        Share of salary you contribute, as a decimal.
    match_limit_pct
        Share of salary the employer matches up to, as a decimal.
    match_rate
        Share of each matched dollar the employer adds, as a decimal.

    Returns
    -------
    float or numpy.ndarray
        Yearly employer contributions.

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values.

    Examples
    --------
    >>> from perfinpy import employer_match
    >>> # $45,000 salary, 50% match on the first 6%, contributing 6% or 3%
    >>> employer_match(salary=45000, contribution_pct=[0.06, 0.03],
    ...                match_limit_pct=0.06, match_rate=0.50)
    array([1350.,  675.])
    """
    salary = _as_numeric(salary, "salary")
    contribution_pct = _as_numeric(contribution_pct, "contribution_pct")
    match_limit_pct = _as_numeric(match_limit_pct, "match_limit_pct")
    match_rate = _as_numeric(match_rate, "match_rate")
    return _out(salary * np.minimum(contribution_pct, match_limit_pct) * match_rate)


def after_tax_value(
    contribution: ArrayLike, tax_rate: ArrayLike, rate: ArrayLike, years: ArrayLike
) -> Numeric:
    """After tax value of a retirement contribution.

    Taxes the contribution once at `tax_rate`, then grows it. With the same
    rate and return, it doesn't matter whether the tax comes first (Roth) or
    last (Traditional); only the tax rate does. From the
    [Retirement Accounts](https://mjfrigaard.github.io/fm-finance/retirement_accounts.html)
    chapter.

    Parameters
    ----------
    contribution
        Amount contributed.
    tax_rate
        Tax rate applied, as a decimal.
    rate
        Yearly return, as a decimal.
    years
        Number of years.

    Returns
    -------
    float or numpy.ndarray
        After tax values.

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values.

    Examples
    --------
    >>> from perfinpy import after_tax_value
    >>> # Roth at 12% today vs. Traditional at 22% in retirement
    >>> after_tax_value(contribution=1000, tax_rate=[0.12, 0.22], rate=0.07,
    ...                 years=40)
    array([13177.5228985 , 11680.07711458])
    """
    contribution = _as_numeric(contribution, "contribution")
    tax_rate = _as_numeric(tax_rate, "tax_rate")
    rate = _as_numeric(rate, "rate")
    years = _as_numeric(years, "years")
    return contribution * (1 - tax_rate) * (1 + rate) ** years
