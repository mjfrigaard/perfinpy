"""Functions from the Tracking Spending chapter."""

from __future__ import annotations

import polars as pl
from numpy.typing import ArrayLike

from ._checks import Numeric, _annuity_factor, _as_numeric


def apply_rules(df: pl.DataFrame, rules: pl.DataFrame) -> pl.DataFrame:
    """Categorize transactions with keyword rules.

    Each row of `rules` holds a regular expression (`Pattern`) and the
    `Category` it assigns. Rules are tried in order and the first match wins;
    matching ignores case. Descriptions that match no rule get `"Other"`.
    From the [Tracking Spending](https://mjfrigaard.github.io/fm-finance/tracking_spending.html)
    chapter.

    Parameters
    ----------
    df
        Transactions with a string `Description` column.
    rules
        Rules with string `Pattern` and `Category` columns.

    Returns
    -------
    polars.DataFrame
        `df` with a `Category` column added (or replaced).

    Raises
    ------
    TypeError
        If `df` or `rules` is not a polars DataFrame.
    ValueError
        If a required column is missing.

    Examples
    --------
    >>> import polars as pl
    >>> from perfinpy import apply_rules
    >>> transactions = pl.DataFrame(
    ...     {"Description": ["SAFEWAY #123", "NETFLIX.COM", "ATM FEE"]}
    ... )
    >>> rules = pl.DataFrame(
    ...     {"Pattern": ["safeway", "netflix"],
    ...      "Category": ["Groceries", "Subscriptions"]}
    ... )
    >>> apply_rules(transactions, rules)["Category"].to_list()
    ['Groceries', 'Subscriptions', 'Other']
    """
    if not isinstance(df, pl.DataFrame):
        raise TypeError("`df` must be a polars DataFrame.")
    if not isinstance(rules, pl.DataFrame):
        raise TypeError("`rules` must be a polars DataFrame.")
    if "Description" not in df.columns:
        raise ValueError("`df` must have a `Description` column.")
    if not {"Pattern", "Category"} <= set(rules.columns):
        raise ValueError("`rules` must have `Pattern` and `Category` columns.")
    category = pl.lit("Other")
    for row in reversed(list(rules.iter_rows(named=True))):
        hit = pl.col("Description").str.contains("(?i)" + row["Pattern"])
        category = pl.when(hit).then(pl.lit(row["Category"])).otherwise(category)
    return df.with_columns(category.alias("Category"))


def subscription_opportunity_cost(
    monthly_cost: ArrayLike, years: ArrayLike, rate: ArrayLike = 0.07
) -> Numeric:
    """What a subscription would grow to if invested instead.

    Treats the yearly cost (`monthly_cost * 12`) as a contribution made at
    the end of each year and grows it at `rate`. From the
    [Tracking Spending](https://mjfrigaard.github.io/fm-finance/tracking_spending.html)
    chapter.

    Parameters
    ----------
    monthly_cost
        Monthly subscription price.
    years
        Number of years.
    rate
        Yearly return, as a decimal. Defaults to 0.07.

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
    >>> from perfinpy import subscription_opportunity_cost
    >>> # $15/month for 30 years at 7%
    >>> subscription_opportunity_cost(monthly_cost=15, years=30)
    17002.94
    """
    monthly_cost = _as_numeric(monthly_cost, "monthly_cost")
    years = _as_numeric(years, "years")
    rate = _as_numeric(rate, "rate")
    return monthly_cost * 12 * _annuity_factor(rate, years)
