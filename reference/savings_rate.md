## savings_rate()


Savings rate: the percent of income not spent.


Usage

``` python
savings_rate(
    income,
    spending,
)
```


From the [Savings Strategies](https://mjfrigaard.github.io/fm-finance/savings_strategies.html) chapter.


## Parameters


`income: ArrayLike`  
Income for the period. Must be greater than 0.

`spending: ArrayLike`  
Spending for the same period.


## Returns


`float or numpy.ndarray`  
Percentages (`15` is 15%). Negative when spending exceeds income.


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values, or `income` is not greater than 0.


## Examples

``` python
>>> from perfinpy import savings_rate
>>> savings_rate(income=3200, spending=2720)
```

15.0
