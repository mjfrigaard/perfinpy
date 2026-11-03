## to_annual()


Convert a daily, weekly, or monthly amount to a yearly amount.


Usage

``` python
to_annual(
    amount,
    period="daily",
)
```


Uses 365 days, 52 weeks, and 12 months per year. From the [Budgeting](https://mjfrigaard.github.io/fm-finance/budgeting.html) chapter.


## Parameters


`amount: ArrayLike`  
Amount per `period`.

`period: Literal[``"daily", `<span class="st">`"weekly"``, ``"monthly"``]`</span>` = ``"daily"`  
One of `"daily"`, `"weekly"`, or `"monthly"`.


## Returns


`float or numpy.ndarray`  
Yearly amounts.


## Raises


`TypeError`  
If `amount` is not numeric.

`ValueError`  
If `amount` contains missing values, or `period` is not one of the choices.


## See Also

[to_monthly()](to_monthly.md#perfinpy.to_monthly)  
Convert to a monthly amount.


## Examples

``` python
>>> from perfinpy import to_annual
>>> # $5 a day coffee
>>> to_annual(amount=5, period="daily")
```

1825.0
