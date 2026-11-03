## to_monthly()


Convert a daily, weekly, or yearly amount to a monthly amount.


Usage

``` python
to_monthly(
    amount,
    period="daily",
)
```


Uses the book's rounded factors: 30.44 days and 4.33 weeks per month, so a round trip through [to_annual()](to_annual.md#perfinpy.to_annual) drifts slightly. From the [Budgeting](https://mjfrigaard.github.io/fm-finance/budgeting.html) chapter.


## Parameters


`amount: ArrayLike`  
Amount per `period`.

`period: Literal[``"daily", `<span class="st">`"weekly"``, ``"annual"``]`</span>` = ``"daily"`  
One of `"daily"`, `"weekly"`, or `"annual"`.


## Returns


`float or numpy.ndarray`  
Monthly amounts.


## Raises


`TypeError`  
If `amount` is not numeric.

`ValueError`  
If `amount` contains missing values, or `period` is not one of the choices.


## See Also

[to_annual()](to_annual.md#perfinpy.to_annual)  
Convert to a yearly amount.


## Examples

``` python
>>> from perfinpy import to_monthly
>>> # $150 a week in groceries
>>> to_monthly(amount=150, period="weekly")
```

649.5
