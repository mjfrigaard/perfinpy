"""Functions from the Investing Basics chapter."""

from __future__ import annotations

from numpy.typing import ArrayLike

from ._checks import Numeric, _annuity_factor, _as_numeric, _as_positive


def future_value(
    present_value: ArrayLike, rate: ArrayLike, years: ArrayLike
) -> Numeric:
    """Future value of a single amount with yearly compounding.

    From the [Investing Basics](https://mjfrigaard.github.io/fm-finance/investing_basics.html)
    chapter.

    Parameters
    ----------
    present_value
        Amount invested today.
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

    See Also
    --------
    future_value_series : Future value of regular contributions.

    Examples
    --------
    >>> from perfinpy import future_value
    >>> # $10,000 at 7% for 10 years
    >>> future_value(present_value=10000, rate=0.07, years=10)
    19671.51
    >>> # several horizons in one call
    >>> future_value(present_value=10000, rate=0.07, years=[5, 10, 20, 30])
    array([14025.517307  , 19671.5135729 , 38696.84462486, 76122.55042662])
    """
    present_value = _as_numeric(present_value, "present_value")
    rate = _as_numeric(rate, "rate")
    years = _as_numeric(years, "years")
    return present_value * (1 + rate) ** years


def rule_of_72(annual_return_pct: ArrayLike) -> Numeric:
    """Years for money to double, by the rule of 72.

    The one function in the package that takes a percent rather than a
    decimal (`7`, not `0.07`). From the
    [Investing Basics](https://mjfrigaard.github.io/fm-finance/investing_basics.html)
    chapter.

    Parameters
    ----------
    annual_return_pct
        Yearly return, as a percent. Must be greater than 0.

    Returns
    -------
    float or numpy.ndarray
        Years to double.

    Raises
    ------
    TypeError
        If `annual_return_pct` is not numeric.
    ValueError
        If `annual_return_pct` contains missing values or is not greater
        than 0.

    Examples
    --------
    >>> from perfinpy import rule_of_72
    >>> rule_of_72(annual_return_pct=7)
    10.28
    """
    annual_return_pct = _as_positive(annual_return_pct, "annual_return_pct")
    return 72 / annual_return_pct


def future_value_series(
    contribution: ArrayLike, rate: ArrayLike, periods: ArrayLike
) -> Numeric:
    """Future value of a fixed contribution made every period.

    Contributions are made at the end of each period. `rate` is the rate per
    period, so a monthly series uses `annual_rate / 12`. A 0% rate gives the
    sum of the contributions. From the
    [Investing Basics](https://mjfrigaard.github.io/fm-finance/investing_basics.html)
    chapter.

    Parameters
    ----------
    contribution
        Amount contributed each period.
    rate
        Return per period, as a decimal.
    periods
        Number of periods.

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

    See Also
    --------
    future_value : Future value of a single amount.

    Examples
    --------
    >>> from perfinpy import future_value_series
    >>> # $500/month for 30 years at 7% a year
    >>> future_value_series(contribution=500, rate=0.07 / 12, periods=30 * 12)
    609985.49
    """
    contribution = _as_numeric(contribution, "contribution")
    rate = _as_numeric(rate, "rate")
    periods = _as_numeric(periods, "periods")
    return contribution * _annuity_factor(rate, periods)


def real_return(nominal: ArrayLike, inflation: ArrayLike) -> Numeric:
    """Real (inflation adjusted) return.

    From the [Investing Basics](https://mjfrigaard.github.io/fm-finance/investing_basics.html)
    chapter.

    Parameters
    ----------
    nominal
        Nominal yearly return, as a decimal.
    inflation
        Yearly inflation rate, as a decimal.

    Returns
    -------
    float or numpy.ndarray
        Real returns, as decimals.

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values.

    Examples
    --------
    >>> from perfinpy import real_return
    >>> real_return(nominal=0.07, inflation=0.03)
    0.03883
    """
    nominal = _as_numeric(nominal, "nominal")
    inflation = _as_numeric(inflation, "inflation")
    return (1 + nominal) / (1 + inflation) - 1
