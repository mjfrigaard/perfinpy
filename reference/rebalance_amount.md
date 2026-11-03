## rebalance_amount()


Amount to buy (positive) or sell (negative) to reach a target.


Usage

``` python
rebalance_amount(
    target_pct,
    total,
    current_amount,
)
```


From the [Asset Allocation](https://mjfrigaard.github.io/fm-finance/asset_allocation.html) chapter.


## Parameters


`target_pct: ArrayLike`  
Target share of the portfolio, as a decimal.

`total: ArrayLike`  
Total portfolio value.

`current_amount: ArrayLike`  
Current value of the holding.


## Returns


`float or numpy.ndarray`  
Amounts to buy (positive) or sell (negative).


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values.


## Examples

``` python
>>> from perfinpy import rebalance_amount
>>> # $5,600 in stocks and $2,000 in bonds after a 30% stock drop
>>> rebalance_amount(target_pct=0.80, total=5600 + 2000, current_amount=5600)
```

480.0
