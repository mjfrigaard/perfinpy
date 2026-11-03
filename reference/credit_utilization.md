## credit_utilization()


Credit utilization: a card balance as a percent of its limit.


Usage

``` python
credit_utilization(
    balance,
    credit_limit,
)
```


From the [Managing Debt](https://mjfrigaard.github.io/fm-finance/managing_debt.html) chapter.


## Parameters


`balance: ArrayLike`  
Card balance.

`credit_limit: ArrayLike`  
Credit limit. Must be greater than 0.


## Returns


`float or numpy.ndarray`  
Percentages (`30` is 30%).


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values, or `credit_limit` is not greater than 0.


## Examples

``` python
>>> from perfinpy import credit_utilization
>>> credit_utilization(balance=900, credit_limit=3000)
```

30.0
