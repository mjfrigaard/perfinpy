## months_to_break_even()


Months until monthly savings cover an upfront cost.


Usage

``` python
months_to_break_even(
    upfront_cost,
    monthly_savings,
)
```


The result is not rounded. From the [Budgeting](https://mjfrigaard.github.io/fm-finance/budgeting.html) chapter.


## Parameters


`upfront_cost: ArrayLike`  
Cost paid today.

`monthly_savings: ArrayLike`  
Amount saved each month. Must be greater than 0.


## Returns


`float or numpy.ndarray`  
Months.


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values, or [monthly_savings](monthly_savings.md#perfinpy.monthly_savings) is not greater than 0.


## Examples

``` python
>>> from perfinpy import months_to_break_even
>>> # $500 membership that saves $60 a month
>>> months_to_break_even(upfront_cost=500, monthly_savings=60)
```

8.33
