## monthly_contribution_needed()


Monthly contribution needed to reach an emergency fund target.


Usage

``` python
monthly_contribution_needed(
    target,
    current_balance,
    months,
)
```


Rounded up to whole dollars. Returns 0 when the fund is already at or above the target. From the [Emergency Fund](https://mjfrigaard.github.io/fm-finance/emergency_fund.html) chapter.


## Parameters


`target: ArrayLike`  
Target balance.

`current_balance: ArrayLike`  
Amount already saved.

`months: ArrayLike`  
Months to reach the target. Must be greater than 0.


## Returns


`int or numpy.ndarray`  
Whole dollars per month.


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values, or `months` is not greater than 0.


## See Also

[months_to_ef_goal()](months_to_ef_goal.md#perfinpy.months_to_ef_goal)  
Solve for the months instead.


## Examples

``` python
>>> from perfinpy import monthly_contribution_needed
>>> monthly_contribution_needed(target=9600, current_balance=1200, months=18)
```

467
