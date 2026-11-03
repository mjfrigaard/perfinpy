## months_to_fund()


Whole months to fund a goal with no interest.


Usage

``` python
months_to_fund(
    goal,
    monthly,
)
```


From the [Financial Goals](https://mjfrigaard.github.io/fm-finance/financial_goals.html) chapter.


## Parameters


`goal: ArrayLike`  
Amount needed.

`monthly: ArrayLike`  
Amount saved each month. Must be greater than 0.


## Returns


`int or numpy.ndarray`  
Whole months, rounded up.


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values, or `monthly` is not greater than 0.


## Examples

``` python
>>> from perfinpy import months_to_fund
>>> # one at a time: a $3,000 trip, then a $9,000 car, at $600/month
>>> months_to_fund(3000, 600), months_to_fund(3000 + 9000, 600)
```

(5, 20)
