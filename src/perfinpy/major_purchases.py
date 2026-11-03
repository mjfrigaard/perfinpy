"""Functions from the Major Purchases chapter."""

from __future__ import annotations

from numpy.typing import ArrayLike

from ._checks import Numeric, _annuity_factor, _as_numeric, _as_positive, _as_scalar


def rent_buy_threshold(
    home_value: ArrayLike, unrecoverable_rate: ArrayLike = 0.05
) -> Numeric:
    """Monthly rent that matches the unrecoverable cost of owning.

    The 5% rule: property tax, maintenance, and the cost of capital come to
    about 5% of the home's value each year. Rent below this monthly amount
    favors renting. From the
    [Major Purchases](https://mjfrigaard.github.io/fm-finance/major_purchases.html)
    chapter.

    Parameters
    ----------
    home_value
        Price of the home.
    unrecoverable_rate
        Yearly unrecoverable cost, as a decimal. Defaults to 0.05.

    Returns
    -------
    float or numpy.ndarray
        Monthly rent thresholds.

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values.

    Examples
    --------
    >>> from perfinpy import rent_buy_threshold
    >>> rent_buy_threshold(home_value=500000)
    2083.33
    """
    home_value = _as_numeric(home_value, "home_value")
    unrecoverable_rate = _as_numeric(unrecoverable_rate, "unrecoverable_rate")
    return (home_value * unrecoverable_rate) / 12


def mortgage_payment(
    principal: ArrayLike, annual_rate: ArrayLike, years: ArrayLike
) -> Numeric:
    """Monthly payment on a fixed rate loan.

    The standard amortization formula with monthly compounding. A 0% rate
    gives `principal / (years * 12)`. From the
    [Major Purchases](https://mjfrigaard.github.io/fm-finance/major_purchases.html)
    chapter.

    Parameters
    ----------
    principal
        Amount borrowed.
    annual_rate
        Yearly interest rate, as a decimal.
    years
        Loan term in years. Must be greater than 0.

    Returns
    -------
    float or numpy.ndarray
        Monthly payments (principal and interest only).

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values, or `years` is not greater
        than 0.

    See Also
    --------
    first_payment_split : Interest and principal in the first payment.
    monthly_standard_payment : Student loan defaults.

    Examples
    --------
    >>> from perfinpy import mortgage_payment
    >>> # $480,000 loan at 6% over 30 years
    >>> mortgage_payment(principal=480000, annual_rate=0.06, years=30)
    2877.84
    """
    principal = _as_numeric(principal, "principal")
    annual_rate = _as_numeric(annual_rate, "annual_rate")
    years = _as_positive(years, "years")
    r = annual_rate / 12
    n = years * 12
    return principal * (1 + r) ** n / _annuity_factor(r, n)


def first_payment_split(
    principal: float, annual_rate: float, years: float
) -> dict[str, float]:
    """Interest and principal in a loan's first monthly payment.

    From the [Major Purchases](https://mjfrigaard.github.io/fm-finance/major_purchases.html)
    chapter.

    Parameters
    ----------
    principal
        Amount borrowed. A single number.
    annual_rate
        Yearly interest rate, as a decimal. A single number.
    years
        Loan term in years. A single number greater than 0.

    Returns
    -------
    dict
        Keys `payment`, `interest`, `principal`, and `pct_interest` (the
        share of the payment that is interest, as a percent).

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values or is not a single number, or
        `years` is not greater than 0.

    See Also
    --------
    mortgage_payment : The payment formula used here.

    Examples
    --------
    >>> from perfinpy import first_payment_split
    >>> split = first_payment_split(principal=480000, annual_rate=0.06, years=30)
    >>> {k: round(v, 2) for k, v in split.items()}
    {'payment': 2877.84, 'interest': 2400.0, 'principal': 477.84, 'pct_interest': 83.4}
    """
    principal = _as_scalar(principal, "principal")
    annual_rate = _as_scalar(annual_rate, "annual_rate")
    years = _as_scalar(years, "years")
    payment = float(mortgage_payment(principal, annual_rate, years))
    interest = principal * (annual_rate / 12)
    return {
        "payment": payment,
        "interest": interest,
        "principal": payment - interest,
        "pct_interest": (interest / payment) * 100,
    }
