## monthly_savings()


Monthly amount to pay yourself first.


Usage

``` python
monthly_savings(
    gross_monthly_income,
    savings_rate,
)
```


From the [Automating Savings](https://mjfrigaard.github.io/fm-finance/automating_savings.html) chapter.


## Parameters


`gross_monthly_income: ArrayLike`  
Monthly income before taxes.

`savings_rate: ArrayLike`  
Share of income saved, as a decimal.


## Returns


`float or numpy.ndarray`  
Monthly savings.


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values.


## Examples

``` python
>>> from perfinpy import monthly_savings
>>> monthly_savings(gross_monthly_income=4000, savings_rate=0.20)
```

800.0
