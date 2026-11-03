## monthly_for_goal()


Monthly saving needed to reach a goal.


Usage

``` python
monthly_for_goal(
    goal,
    annual_rate,
    months,
)
```


Solves the future value of a series for the contribution, compounding monthly at `annual_rate / 12`. A 0% rate gives `goal / months`. From the [Financial Goals](https://mjfrigaard.github.io/fm-finance/financial_goals.html) chapter.


## Parameters


`goal: ArrayLike`  
Amount needed.

`annual_rate: ArrayLike`  
Yearly return on savings, as a decimal.

`months: ArrayLike`  
Months until the goal. Must be greater than 0.


## Returns


`float or numpy.ndarray`  
Monthly contributions.


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values, or `months` is not greater than 0.


## Examples

``` python
>>> from perfinpy import monthly_for_goal
>>> # $15,000 in 5 years at 4%, compared to no interest
>>> monthly_for_goal(goal=15000, annual_rate=[0.04, 0], months=60)
```

array(\[226.24783083, 250. \])
