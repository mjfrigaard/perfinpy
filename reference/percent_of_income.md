## percent_of_income()


An expense as a percent of income.


Usage

``` python
percent_of_income(
    expense,
    income,
)
```


`expense` and `income` must cover the same period. From the [Budgeting](https://mjfrigaard.github.io/fm-finance/budgeting.html) chapter.


## Parameters


`expense: ArrayLike`  
Amount spent.

`income: ArrayLike`  
Income for the same period. Must be greater than 0.


## Returns


`float or numpy.ndarray`  
Percentages (`30` is 30%).


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values, or `income` is not greater than 0.


## Examples

``` python
>>> from perfinpy import percent_of_income
>>> percent_of_income(expense=1500, income=5000)
```

30.0
