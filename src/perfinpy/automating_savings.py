"""Functions from the Automating Savings chapter."""

from __future__ import annotations

from numpy.typing import ArrayLike

from ._checks import Numeric, _as_numeric


def monthly_savings(
    gross_monthly_income: ArrayLike, savings_rate: ArrayLike
) -> Numeric:
    """Monthly amount to pay yourself first.

    From the [Automating Savings](https://mjfrigaard.github.io/fm-finance/automating_savings.html)
    chapter.

    Parameters
    ----------
    gross_monthly_income
        Monthly income before taxes.
    savings_rate
        Share of income saved, as a decimal.

    Returns
    -------
    float or numpy.ndarray
        Monthly savings.

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values.

    Examples
    --------
    >>> from perfinpy import monthly_savings
    >>> monthly_savings(gross_monthly_income=4000, savings_rate=0.20)
    800.0
    """
    gross_monthly_income = _as_numeric(gross_monthly_income, "gross_monthly_income")
    savings_rate = _as_numeric(savings_rate, "savings_rate")
    return gross_monthly_income * savings_rate
