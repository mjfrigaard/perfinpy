"""Functions from the Taxes chapter."""

from __future__ import annotations

import numpy as np

from ._checks import _as_scalar


def income_tax(income: float, deduction: float = 16100) -> float:
    """Federal income tax for a single filer (2026 brackets).

    Subtracts the deduction, then taxes each slice of taxable income at its
    bracket's rate. Uses the 2026 single filer brackets and standard
    deduction. From the
    [Taxes](https://mjfrigaard.github.io/fm-finance/taxes.html) chapter.

    Parameters
    ----------
    income
        Yearly gross income. A single number.
    deduction
        Deduction subtracted before tax. Defaults to 16100 (the 2026
        standard deduction). A single number.

    Returns
    -------
    float
        Tax owed.

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values or is not a single number.

    See Also
    --------
    raise_kept : How much of a raise you keep after tax.

    Examples
    --------
    >>> from perfinpy import income_tax
    >>> income_tax(income=45000)
    3220.0
    >>> # effective rate
    >>> income_tax(income=45000) / 45000
    0.0715
    """
    income = _as_scalar(income, "income")
    deduction = _as_scalar(deduction, "deduction")
    taxable = max(income - deduction, 0)
    lower = np.array([0, 12400, 50400, 105700, 201775, 256225, 640600])
    upper = np.append(lower[1:], np.inf)
    rate = np.array([0.10, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37])
    return float(np.sum(rate * np.clip(np.minimum(taxable, upper) - lower, 0, None)))


def raise_kept(old_income: float, raise_amount: float) -> float:
    """How much of a raise you keep after federal income tax.

    The raise minus the extra tax it adds, using `income_tax()`. From the
    [Taxes](https://mjfrigaard.github.io/fm-finance/taxes.html) chapter.

    Parameters
    ----------
    old_income
        Yearly gross income before the raise. A single number.
    raise_amount
        Size of the raise. A single number.

    Returns
    -------
    float
        Amount of the raise kept after tax.

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values or is not a single number.

    See Also
    --------
    income_tax : The tax calculation used here.

    Examples
    --------
    >>> from perfinpy import raise_kept
    >>> # $2,000 raise on a $66,000 salary
    >>> raise_kept(old_income=66000, raise_amount=2000)
    1610.0
    """
    old_income = _as_scalar(old_income, "old_income")
    raise_amount = _as_scalar(raise_amount, "raise_amount")
    extra_tax = income_tax(old_income + raise_amount) - income_tax(old_income)
    return raise_amount - extra_tax
