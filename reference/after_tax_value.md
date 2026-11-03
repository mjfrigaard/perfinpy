## after_tax_value()


After tax value of a retirement contribution.


Usage

``` python
after_tax_value(
    contribution,
    tax_rate,
    rate,
    years,
)
```


Taxes the contribution once at `tax_rate`, then grows it. With the same rate and return, it doesn't matter whether the tax comes first (Roth) or last (Traditional); only the tax rate does. From the [Retirement Accounts](https://mjfrigaard.github.io/fm-finance/retirement_accounts.html) chapter.


## Parameters


`contribution: ArrayLike`  
Amount contributed.

`tax_rate: ArrayLike`  
Tax rate applied, as a decimal.

`rate: ArrayLike`  
Yearly return, as a decimal.

`years: ArrayLike`  
Number of years.


## Returns


`float or numpy.ndarray`  
After tax values.


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values.


## Examples

``` python
>>> from perfinpy import after_tax_value
>>> # Roth at 12% today vs. Traditional at 22% in retirement
>>> after_tax_value(contribution=1000, tax_rate=[0.12, 0.22], rate=0.07,
...                 years=40)
```

array(\[13177.5228985 , 11680.07711458\])
