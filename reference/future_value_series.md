## future_value_series()


Future value of a fixed contribution made every period.


Usage

``` python
future_value_series(
    contribution,
    rate,
    periods,
)
```


Contributions are made at the end of each period. `rate` is the rate per period, so a monthly series uses `annual_rate / 12`. A 0% rate gives the sum of the contributions. From the [Investing Basics](https://mjfrigaard.github.io/fm-finance/investing_basics.html) chapter.


## Parameters


`contribution: ArrayLike`  
Amount contributed each period.

`rate: ArrayLike`  
Return per period, as a decimal.

`periods: ArrayLike`  
Number of periods.


## Returns


`float or numpy.ndarray`  
Future values.


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values.


## See Also

[future_value()](future_value.md#perfinpy.future_value)  
Future value of a single amount.


## Examples

``` python
>>> from perfinpy import future_value_series
>>> # $500/month for 30 years at 7% a year
>>> future_value_series(contribution=500, rate=0.07 / 12, periods=30 * 12)
```

609985.49
