## future_value_after_fees()


Future value of monthly contributions after fund fees.


Usage

``` python
future_value_after_fees(
    contribution,
    annual_return,
    expense_ratio,
    years,
)
```


Subtracts the expense ratio from the yearly return, then compounds monthly contributions. From the [Index Funds](https://mjfrigaard.github.io/fm-finance/index_funds.html) chapter.


## Parameters


`contribution: ArrayLike`  
Amount contributed each month.

`annual_return: ArrayLike`  
Yearly return before fees, as a decimal.

`expense_ratio: ArrayLike`  
Yearly expense ratio, as a decimal.

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
>>> from perfinpy import future_value_after_fees
>>> # $300/month for 40 years at 7%, index fund vs. active fund
>>> future_value_after_fees(300, 0.07, [0.0004, 0.01], 40)
```

array(\[778654.71, 597447.22\])
