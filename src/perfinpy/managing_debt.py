"""Functions from the Managing Debt chapter."""

from __future__ import annotations

from typing import Any

import numpy as np
from numpy.typing import ArrayLike

from ._checks import Numeric, _as_numeric, _as_positive, _as_scalar, _out
from .major_purchases import mortgage_payment


def apr_to_apy(apr: ArrayLike, periods_per_year: ArrayLike = 365) -> Numeric:
    """Convert an APR to an annual percentage yield (APY).

    From the [Managing Debt](https://mjfrigaard.github.io/fm-finance/managing_debt.html)
    chapter.

    Parameters
    ----------
    apr
        Annual percentage rate, as a decimal.
    periods_per_year
        Compounding periods per year. Defaults to 365 (daily). Must be
        greater than 0.

    Returns
    -------
    float or numpy.ndarray
        APYs, as decimals.

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values, or `periods_per_year` is not
        greater than 0.

    Examples
    --------
    >>> from perfinpy import apr_to_apy
    >>> # 24% APR compounded daily
    >>> apr_to_apy(apr=0.24)
    0.27114
    """
    apr = _as_numeric(apr, "apr")
    periods_per_year = _as_positive(periods_per_year, "periods_per_year")
    return (1 + apr / periods_per_year) ** periods_per_year - 1


def months_to_payoff(
    balance: ArrayLike, monthly_payment: ArrayLike, apr: ArrayLike
) -> Numeric:
    """Months to pay off a balance with a fixed payment.

    Interest compounds monthly at `apr / 12`. The result is not rounded; the
    last payment is a partial one. From the
    [Managing Debt](https://mjfrigaard.github.io/fm-finance/managing_debt.html)
    chapter.

    Parameters
    ----------
    balance
        Current balance. Must be greater than 0.
    monthly_payment
        Fixed monthly payment. Must be greater than 0.
    apr
        Annual percentage rate, as a decimal.

    Returns
    -------
    float or numpy.ndarray
        Months.

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values, `balance` or
        `monthly_payment` is not greater than 0, or the payment does not
        cover the first month's interest (the balance would never be paid
        off).

    Examples
    --------
    >>> from perfinpy import months_to_payoff
    >>> # $5,000 balance, $100/month, 22% APR
    >>> months_to_payoff(balance=5000, monthly_payment=100, apr=0.22)
    136.779
    """
    balance = _as_positive(balance, "balance")
    monthly_payment = _as_positive(monthly_payment, "monthly_payment")
    apr = _as_numeric(apr, "apr")
    if np.any(np.asarray(monthly_payment <= balance * apr / 12)):
        raise ValueError(
            "`monthly_payment` must be larger than the monthly interest "
            "(`balance * apr / 12`)."
        )
    r = np.asarray(apr / 12)
    ratio = np.asarray(balance / monthly_payment)
    with np.errstate(divide="ignore", invalid="ignore"):
        out = -np.log1p(-r * ratio) / np.log1p(r)
    return _out(np.where(r == 0, ratio, out))


def total_interest(
    monthly_payment: ArrayLike, n_months: ArrayLike, principal: ArrayLike
) -> Numeric:
    """Total interest paid over the life of a loan.

    All payments minus the amount borrowed. From the
    [Managing Debt](https://mjfrigaard.github.io/fm-finance/managing_debt.html)
    chapter.

    Parameters
    ----------
    monthly_payment
        Fixed monthly payment.
    n_months
        Number of payments.
    principal
        Amount borrowed.

    Returns
    -------
    float or numpy.ndarray
        Interest paid.

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values.

    Examples
    --------
    >>> from perfinpy import total_interest
    >>> # 6-year vs. 4-year car loan, $20,000 at 7%
    >>> total_interest(monthly_payment=[340.98, 478.92], n_months=[72, 48],
    ...                principal=20000)
    array([4550.56, 2988.16])
    """
    monthly_payment = _as_numeric(monthly_payment, "monthly_payment")
    n_months = _as_numeric(n_months, "n_months")
    principal = _as_numeric(principal, "principal")
    return (monthly_payment * n_months) - principal


def loan_income_ratio(loan_total: ArrayLike, expected_salary: ArrayLike) -> Numeric:
    """Total student loans as a multiple of expected starting salary.

    A ratio at or below 1 means you borrow no more than your first year's
    salary. From the
    [Managing Debt](https://mjfrigaard.github.io/fm-finance/managing_debt.html)
    chapter.

    Parameters
    ----------
    loan_total
        Total amount borrowed.
    expected_salary
        Expected yearly starting salary. Must be greater than 0.

    Returns
    -------
    float or numpy.ndarray
        Ratios (`1.07` is 107% of salary).

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values, or `expected_salary` is not
        greater than 0.

    Examples
    --------
    >>> from perfinpy import loan_income_ratio
    >>> loan_income_ratio(loan_total=45000, expected_salary=42000)
    1.0714
    """
    loan_total = _as_numeric(loan_total, "loan_total")
    expected_salary = _as_positive(expected_salary, "expected_salary")
    return loan_total / expected_salary


def monthly_standard_payment(
    principal: ArrayLike, annual_rate: ArrayLike = 0.065, years: ArrayLike = 10
) -> Numeric:
    """Monthly payment on a standard student loan repayment plan.

    The same amortization formula as `mortgage_payment()`, with student loan
    defaults (6.5% over 10 years). From the
    [Managing Debt](https://mjfrigaard.github.io/fm-finance/managing_debt.html)
    chapter.

    Parameters
    ----------
    principal
        Amount borrowed.
    annual_rate
        Yearly interest rate, as a decimal. Defaults to 0.065.
    years
        Repayment term in years. Defaults to 10. Must be greater than 0.

    Returns
    -------
    float or numpy.ndarray
        Monthly payments.

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values, or `years` is not greater
        than 0.

    See Also
    --------
    mortgage_payment : The general amortization formula.

    Examples
    --------
    >>> from perfinpy import monthly_standard_payment
    >>> monthly_standard_payment(principal=45000)
    510.96
    """
    return mortgage_payment(principal, annual_rate, years)


def idr_monthly_payment(
    agi: ArrayLike,
    poverty_guideline: ArrayLike = 15960,
    threshold_pct: ArrayLike = 1.5,
    payment_rate: ArrayLike = 0.10,
) -> Numeric:
    """Income driven repayment (IDR) monthly payment.

    Discretionary income is adjusted gross income (AGI) above
    `threshold_pct` times the poverty guideline. The yearly payment is
    `payment_rate` of that, split into 12 months and rounded to cents. From
    the [Managing Debt](https://mjfrigaard.github.io/fm-finance/managing_debt.html)
    chapter.

    Parameters
    ----------
    agi
        Adjusted gross income.
    poverty_guideline
        Federal poverty guideline for the household size. Defaults to 15960
        (one person).
    threshold_pct
        Multiple of the poverty guideline that is protected. Defaults to 1.5
        (150%).
    payment_rate
        Share of discretionary income paid each year. Defaults to 0.10.

    Returns
    -------
    float or numpy.ndarray
        Monthly payments.

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values.

    Examples
    --------
    >>> from perfinpy import idr_monthly_payment
    >>> # IBR: $50,000 AGI, 150% threshold, 10% rate
    >>> idr_monthly_payment(agi=50000)
    217.17
    >>> # IBR for loans before July 2014: 15% rate
    >>> idr_monthly_payment(agi=50000, payment_rate=0.15)
    325.75
    """
    agi = _as_numeric(agi, "agi")
    poverty_guideline = _as_numeric(poverty_guideline, "poverty_guideline")
    threshold_pct = _as_numeric(threshold_pct, "threshold_pct")
    payment_rate = _as_numeric(payment_rate, "payment_rate")
    discretionary = np.maximum(0, agi - poverty_guideline * threshold_pct)
    monthly = np.asarray((discretionary * payment_rate) / 12)
    # python round() per value, as the book does (np.round differs on ties)
    rounded = [round(float(v), 2) for v in monthly.ravel()]
    return _out(np.reshape(rounded, monthly.shape))


def dti_ratio(
    monthly_debt_payments: ArrayLike, gross_monthly_income: ArrayLike
) -> Numeric:
    """Debt to income ratio.

    Monthly debt payments as a percent of gross monthly income. From the
    [Managing Debt](https://mjfrigaard.github.io/fm-finance/managing_debt.html)
    chapter.

    Parameters
    ----------
    monthly_debt_payments
        Total monthly debt payments.
    gross_monthly_income
        Monthly income before taxes. Must be greater than 0.

    Returns
    -------
    float or numpy.ndarray
        Percentages (`28.3` is 28.3%).

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values, or `gross_monthly_income` is
        not greater than 0.

    Examples
    --------
    >>> from perfinpy import dti_ratio
    >>> dti_ratio(monthly_debt_payments=1061, gross_monthly_income=3750)
    28.29
    """
    monthly_debt_payments = _as_numeric(monthly_debt_payments, "monthly_debt_payments")
    gross_monthly_income = _as_positive(gross_monthly_income, "gross_monthly_income")
    return (monthly_debt_payments / gross_monthly_income) * 100


def payoff_vs_invest(loan_rate: float, expected_return: float) -> str:
    """Pay off a debt or invest the difference.

    Compares a loan's interest rate with an expected investment return. From
    the [Managing Debt](https://mjfrigaard.github.io/fm-finance/managing_debt.html)
    chapter.

    Parameters
    ----------
    loan_rate
        The loan's yearly interest rate, as a decimal. A single number.
    expected_return
        Expected yearly investment return, as a decimal. A single number.

    Returns
    -------
    str
        `"Pay off the debt"`, `"Invest the difference"`, or
        `"Roughly a wash; do both"`.

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values or is not a single number.

    Examples
    --------
    >>> from perfinpy import payoff_vs_invest
    >>> payoff_vs_invest(loan_rate=0.05, expected_return=0.07)
    'Invest the difference'
    """
    loan_rate = _as_scalar(loan_rate, "loan_rate")
    expected_return = _as_scalar(expected_return, "expected_return")
    if loan_rate > expected_return:
        return "Pay off the debt"
    if loan_rate < expected_return:
        return "Invest the difference"
    return "Roughly a wash; do both"


def _check_debts(debts: list[dict[str, Any]], key: str) -> None:
    if not isinstance(debts, list) or not all(isinstance(d, dict) for d in debts):
        raise TypeError("`debts` must be a list of dicts.")
    if not all(key in d for d in debts):
        raise ValueError(f"every debt must have an `{key}` key.")
    _as_numeric([d[key] for d in debts], key)


def order_avalanche(debts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Order debts for the avalanche method (highest APR first).

    From the [Managing Debt](https://mjfrigaard.github.io/fm-finance/managing_debt.html)
    chapter.

    Parameters
    ----------
    debts
        A list of dicts, each with a numeric `apr` key.

    Returns
    -------
    list of dict
        A new list, sorted by `apr` from highest to lowest. Ties keep their
        original order.

    Raises
    ------
    TypeError
        If `debts` is not a list of dicts, or an `apr` is not numeric.
    ValueError
        If a debt has no `apr` key, or an `apr` is missing.

    See Also
    --------
    order_snowball : Smallest balance first.

    Examples
    --------
    >>> from perfinpy import order_avalanche
    >>> debts = [
    ...     {"name": "Card A", "balance": 1000, "apr": 0.18},
    ...     {"name": "Card B", "balance": 5000, "apr": 0.24},
    ...     {"name": "Card C", "balance": 2000, "apr": 0.15},
    ... ]
    >>> [d["name"] for d in order_avalanche(debts)]
    ['Card B', 'Card A', 'Card C']
    """
    _check_debts(debts, "apr")
    return sorted(debts, key=lambda d: d["apr"], reverse=True)


def order_snowball(debts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Order debts for the snowball method (smallest balance first).

    From the [Managing Debt](https://mjfrigaard.github.io/fm-finance/managing_debt.html)
    chapter.

    Parameters
    ----------
    debts
        A list of dicts, each with a numeric `balance` key.

    Returns
    -------
    list of dict
        A new list, sorted by `balance` from smallest to largest. Ties keep
        their original order.

    Raises
    ------
    TypeError
        If `debts` is not a list of dicts, or a `balance` is not numeric.
    ValueError
        If a debt has no `balance` key, or a `balance` is missing.

    See Also
    --------
    order_avalanche : Highest APR first.

    Examples
    --------
    >>> from perfinpy import order_snowball
    >>> debts = [
    ...     {"name": "Card A", "balance": 1000, "apr": 0.18},
    ...     {"name": "Card B", "balance": 5000, "apr": 0.24},
    ...     {"name": "Card C", "balance": 2000, "apr": 0.15},
    ... ]
    >>> [d["name"] for d in order_snowball(debts)]
    ['Card A', 'Card C', 'Card B']
    """
    _check_debts(debts, "balance")
    return sorted(debts, key=lambda d: d["balance"])


def credit_utilization(balance: ArrayLike, credit_limit: ArrayLike) -> Numeric:
    """Credit utilization: a card balance as a percent of its limit.

    From the [Managing Debt](https://mjfrigaard.github.io/fm-finance/managing_debt.html)
    chapter.

    Parameters
    ----------
    balance
        Card balance.
    credit_limit
        Credit limit. Must be greater than 0.

    Returns
    -------
    float or numpy.ndarray
        Percentages (`30` is 30%).

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values, or `credit_limit` is not
        greater than 0.

    Examples
    --------
    >>> from perfinpy import credit_utilization
    >>> credit_utilization(balance=900, credit_limit=3000)
    30.0
    """
    balance = _as_numeric(balance, "balance")
    credit_limit = _as_positive(credit_limit, "credit_limit")
    return (balance / credit_limit) * 100
