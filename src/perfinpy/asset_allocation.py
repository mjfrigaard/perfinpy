"""Functions from the Asset Allocation chapter."""

from __future__ import annotations

from typing import Any

import polars as pl
from numpy.typing import ArrayLike

from ._checks import Numeric, _as_numeric


def portfolio_return(
    stock_pct: ArrayLike | pl.Expr,
    stock_return: ArrayLike | pl.Expr,
    bond_return: ArrayLike | pl.Expr,
) -> Any:
    """Return on a two fund (stock and bond) portfolio.

    A weighted average of the two returns. Also accepts polars expressions,
    so it works inside `with_columns()`. From the
    [Asset Allocation](https://mjfrigaard.github.io/fm-finance/asset_allocation.html)
    chapter.

    Parameters
    ----------
    stock_pct
        Share of the portfolio in stocks, as a decimal.
    stock_return
        Yearly stock return, as a decimal.
    bond_return
        Yearly bond return, as a decimal.

    Returns
    -------
    float, numpy.ndarray, or polars.Expr
        Portfolio returns, as decimals. A polars expression when any input is
        one.

    Raises
    ------
    TypeError
        If an argument is not numeric (or a polars expression).
    ValueError
        If an argument contains missing values.

    Examples
    --------
    >>> import polars as pl
    >>> from perfinpy import portfolio_return
    >>> # an 80/20 portfolio in an average year
    >>> portfolio_return(stock_pct=0.80, stock_return=0.10, bond_return=0.04)
    0.088
    >>> # 100/0, 80/20, and 60/40 in a bad year
    >>> pl.DataFrame({"stocks": [1.0, 0.8, 0.6]}).with_columns(
    ...     bad=portfolio_return(pl.col("stocks"), -0.40, 0.0)
    ... )["bad"].round(2).to_list()
    [-0.4, -0.32, -0.24]
    """
    args = {
        "stock_pct": stock_pct,
        "stock_return": stock_return,
        "bond_return": bond_return,
    }
    s, sr, br = (
        x if isinstance(x, pl.Expr) else _as_numeric(x, name)
        for name, x in args.items()
    )
    return s * sr + (1 - s) * br


def rebalance_amount(
    target_pct: ArrayLike, total: ArrayLike, current_amount: ArrayLike
) -> Numeric:
    """Amount to buy (positive) or sell (negative) to reach a target.

    From the [Asset Allocation](https://mjfrigaard.github.io/fm-finance/asset_allocation.html)
    chapter.

    Parameters
    ----------
    target_pct
        Target share of the portfolio, as a decimal.
    total
        Total portfolio value.
    current_amount
        Current value of the holding.

    Returns
    -------
    float or numpy.ndarray
        Amounts to buy (positive) or sell (negative).

    Raises
    ------
    TypeError
        If an argument is not numeric.
    ValueError
        If an argument contains missing values.

    Examples
    --------
    >>> from perfinpy import rebalance_amount
    >>> # $5,600 in stocks and $2,000 in bonds after a 30% stock drop
    >>> rebalance_amount(target_pct=0.80, total=5600 + 2000, current_amount=5600)
    480.0
    """
    target_pct = _as_numeric(target_pct, "target_pct")
    total = _as_numeric(total, "total")
    current_amount = _as_numeric(current_amount, "current_amount")
    return target_pct * total - current_amount
