## wealth_formula()


Wealth from saving part of an income every year.


Usage

``` python
wealth_formula(
    median_income,
    savings_rate,
    annual_return,
    years,
)
```


The future value of saving `median_income * savings_rate` at the end of each year (contributions plus growth). From the [Income](https://mjfrigaard.github.io/fm-finance/income.html) chapter.


## Parameters


`median_income: ArrayLike`  
Yearly income.

`savings_rate: ArrayLike`  
Share of income saved, as a decimal.

`annual_return: ArrayLike`  
Yearly return, as a decimal. A 0% return gives the sum of the contributions.

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

[raise_invested_value()](raise_invested_value.md#perfinpy.raise_invested_value)  
Monthly version for investing part of a raise.


## Examples

``` python
>>> from perfinpy import wealth_formula
>>> # $45,000 income, 20% saved, 7% return, 30 years
>>> wealth_formula(45000, savings_rate=0.20, annual_return=0.07, years=30)
```

850147.07
