## months_to_ef_goal()


Months to reach an emergency fund target.


Usage

``` python
months_to_ef_goal(
    target,
    current_balance,
    monthly_contribution,
)
```


Rounded up to whole months. Returns 0 when the fund is already at or above the target. From the [Emergency Fund](https://mjfrigaard.github.io/fm-finance/emergency_fund.html) chapter.


## Parameters


`target: ArrayLike`  
Target balance.

`current_balance: ArrayLike`  
Amount already saved.

`monthly_contribution: ArrayLike`  
Amount added each month. Must be greater than 0.


## Returns


`int or numpy.ndarray`  
Whole months.


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values, or `monthly_contribution` is not greater than 0.


## See Also

[monthly_contribution_needed()](monthly_contribution_needed.md#perfinpy.monthly_contribution_needed)  
Solve for the contribution instead.


## Examples

``` python
>>> from perfinpy import months_to_ef_goal
>>> months_to_ef_goal(target=9600, current_balance=1200,
...                   monthly_contribution=400)
```

21
