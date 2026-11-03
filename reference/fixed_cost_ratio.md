## fixed_cost_ratio()


Fixed costs as a percent of take home pay.


Usage

``` python
fixed_cost_ratio(
    fixed_costs,
    take_home,
)
```


From the [Income](https://mjfrigaard.github.io/fm-finance/income.html) chapter.


## Parameters


`fixed_costs: ArrayLike`  
Monthly fixed costs (rent, insurance, loan payments).

`take_home: ArrayLike`  
Monthly take home pay. Must be greater than 0.


## Returns


`float or numpy.ndarray`  
Percentages (`56.25` is 56.25%).


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values, or `take_home` is not greater than 0.


## Examples

``` python
>>> from perfinpy import fixed_cost_ratio
>>> fixed_cost_ratio(fixed_costs=1800, take_home=3200)
```

56.25
