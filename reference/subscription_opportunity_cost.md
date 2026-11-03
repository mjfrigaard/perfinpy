## subscription_opportunity_cost()


What a subscription would grow to if invested instead.


Usage

``` python
subscription_opportunity_cost(
    monthly_cost,
    years,
    rate=0.07,
)
```


Treats the yearly cost (`monthly_cost * 12`) as a contribution made at the end of each year and grows it at `rate`. From the [Tracking Spending](https://mjfrigaard.github.io/fm-finance/tracking_spending.html) chapter.


## Parameters


`monthly_cost: ArrayLike`  
Monthly subscription price.

`years: ArrayLike`  
Number of years.

`rate: ArrayLike = ``0.07`  
Yearly return, as a decimal. Defaults to 0.07.


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
>>> from perfinpy import subscription_opportunity_cost
>>> # $15/month for 30 years at 7%
>>> subscription_opportunity_cost(monthly_cost=15, years=30)
```

17002.94
