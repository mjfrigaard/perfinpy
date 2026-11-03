## future_value()


Future value of a single amount with yearly compounding.


Usage

``` python
future_value(
    present_value,
    rate,
    years,
)
```


From the [Investing Basics](https://mjfrigaard.github.io/fm-finance/investing_basics.html) chapter.


## Parameters


`present_value: ArrayLike`  
Amount invested today.

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


## See Also

[future_value_series()](future_value_series.md#perfinpy.future_value_series)  
Future value of regular contributions.


## Examples

``` python
>>> from perfinpy import future_value
>>> # $10,000 at 7% for 10 years
>>> future_value(present_value=10000, rate=0.07, years=10)
```

19671.51

``` python
>>> # several horizons in one call
>>> future_value(present_value=10000, rate=0.07, years=[5, 10, 20, 30])
```

array(\[14025.517307 , 19671.5135729 , 38696.84462486, 76122.55042662\])
