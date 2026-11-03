## opportunity_cost()


What an amount could grow to if invested instead of spent.


Usage

``` python
opportunity_cost(
    amount,
    rate,
    years,
)
```


Compounds `amount` once a year at `rate`. From the [Budgeting](https://mjfrigaard.github.io/fm-finance/budgeting.html) chapter.


## Parameters


`amount: ArrayLike`  
Amount spent today.

`rate: ArrayLike`  
Yearly return, as a decimal.

`years: ArrayLike`  
Number of years.


## Returns


`float or numpy.ndarray`  
Future values.


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values.


## Examples

``` python
>>> from perfinpy import opportunity_cost
>>> # $25,000 saved on a car, invested at 7% for 30 years
>>> opportunity_cost(amount=25000, rate=0.07, years=30)
```

190306.37
