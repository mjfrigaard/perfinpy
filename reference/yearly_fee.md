## yearly_fee()


Yearly fund fee from an expense ratio.


Usage

``` python
yearly_fee(
    balance,
    expense_ratio,
)
```


From the [Index Funds](https://mjfrigaard.github.io/fm-finance/index_funds.html) chapter.


## Parameters


`balance: ArrayLike`  
Amount invested.

`expense_ratio: ArrayLike`  
Yearly expense ratio, as a decimal (`0.0004` is 0.04%).


## Returns


`float or numpy.ndarray`  
Yearly fees.


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values.


## Examples

``` python
>>> from perfinpy import yearly_fee
>>> # $10,000 in an index fund vs. an active fund
>>> yearly_fee(balance=10000, expense_ratio=[0.0004, 0.01])
```

array(\[ 4., 100.\])
