## ef_growth()


Emergency fund balance after earning interest.


Usage

``` python
ef_growth(
    balance,
    apy,
    months,
)
```


Grows `balance` at `apy` for `months / 12` years. From the [Emergency Fund](https://mjfrigaard.github.io/fm-finance/emergency_fund.html) chapter.


## Parameters


`balance: ArrayLike`  
Starting balance.

`apy: ArrayLike`  
Annual percentage yield, as a decimal.

`months: ArrayLike`  
Number of months.


## Returns


`float or numpy.ndarray`  
Ending balances.


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values.


## Examples

``` python
>>> from perfinpy import ef_growth
>>> ef_growth(balance=9600, apy=0.04, months=12)
```

9984.0
