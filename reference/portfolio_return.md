## portfolio_return()


Return on a two fund (stock and bond) portfolio.


Usage

``` python
portfolio_return(
    stock_pct,
    stock_return,
    bond_return,
)
```


A weighted average of the two returns. Also accepts polars expressions, so it works inside `with_columns()`. From the [Asset Allocation](https://mjfrigaard.github.io/fm-finance/asset_allocation.html) chapter.


## Parameters


`stock_pct: ArrayLike | pl.Expr`  
Share of the portfolio in stocks, as a decimal.

`stock_return: ArrayLike | pl.Expr`  
Yearly stock return, as a decimal.

`bond_return: ArrayLike | pl.Expr`  
Yearly bond return, as a decimal.


## Returns


`float, numpy.ndarray, or polars.Expr`  
Portfolio returns, as decimals. A polars expression when any input is one.


## Raises


`TypeError`  
If an argument is not numeric (or a polars expression).

`ValueError`  
If an argument contains missing values.


## Examples

``` python
>>> import polars as pl
>>> from perfinpy import portfolio_return
>>> # an 80/20 portfolio in an average year
>>> portfolio_return(stock_pct=0.80, stock_return=0.10, bond_return=0.04)
```

0.088

``` python
>>> # 100/0, 80/20, and 60/40 in a bad year
>>> pl.DataFrame({"stocks": [1.0, 0.8, 0.6]}).with_columns(
...     bad=portfolio_return(pl.col("stocks"), -0.40, 0.0)
... )["bad"].round(2).to_list()
```

\[-0.4, -0.32, -0.24\]
