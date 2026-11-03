## raise_invested_value()


Future value of investing part of a raise.


Usage

``` python
raise_invested_value(
    monthly_raise,
    invest_share,
    rate,
    years,
)
```


Invests `monthly_raise * invest_share` every month, compounded monthly. From the [Income](https://mjfrigaard.github.io/fm-finance/income.html) chapter.


## Parameters


`monthly_raise: ArrayLike`  
Monthly increase in take home pay.

`invest_share: ArrayLike`  
Share of the raise invested, as a decimal.

`rate: ArrayLike`  
Yearly return, as a decimal.

`years: ArrayLike`  
Number of years.


## Returns


`float or numpy.ndarray`  
Ending balances.


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values.


## See Also

[wealth_formula()](wealth_formula.md#perfinpy.wealth_formula)  
Yearly version for saving part of an income.


## Examples

``` python
>>> from perfinpy import raise_invested_value
>>> # invest half of a $200/month raise at 7% for 30 years
>>> raise_invested_value(200, invest_share=0.5, rate=0.07, years=30)
```

121997.09
