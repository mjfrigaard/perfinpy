## apr_to_apy()


Convert an APR to an annual percentage yield (APY).


Usage

``` python
apr_to_apy(
    apr,
    periods_per_year=365,
)
```


From the [Managing Debt](https://mjfrigaard.github.io/fm-finance/managing_debt.html) chapter.


## Parameters


`apr: ArrayLike`  
Annual percentage rate, as a decimal.

`periods_per_year: ArrayLike = ``365`  
Compounding periods per year. Defaults to 365 (daily). Must be greater than 0.


## Returns


`float or numpy.ndarray`  
APYs, as decimals.


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values, or `periods_per_year` is not greater than 0.


## Examples

``` python
>>> from perfinpy import apr_to_apy
>>> # 24% APR compounded daily
>>> apr_to_apy(apr=0.24)
```

0.27114
