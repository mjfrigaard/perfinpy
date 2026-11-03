## plan_cost()


Yearly cost of a health plan.


Usage

``` python
plan_cost(
    monthly_premium,
    medical_cost,
    oop_max,
    employer_hsa=0,
)
```


Twelve premiums plus what you pay for care (capped at the out of pocket maximum), minus any employer HSA contribution. Use `float("inf")` for `medical_cost` to get the worst case year. From the [Insurance](https://mjfrigaard.github.io/fm-finance/insurance.html) chapter.


## Parameters


`monthly_premium: ArrayLike`  
Monthly premium.

`medical_cost: ArrayLike`  
Medical costs for the year.

`oop_max: ArrayLike`  
Out of pocket maximum.

`employer_hsa: ArrayLike = ``0`  
Employer HSA contribution. Defaults to 0.


## Returns


`float or numpy.ndarray`  
Yearly costs.


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values.


## Examples

``` python
>>> from perfinpy import plan_cost
>>> # Plan A in a healthy year ($300 of care) and the worst year
>>> plan_cost(100, [300, float("inf")], oop_max=3000)
```

array(\[1500., 4200.\])

``` python
>>> # Plan B, with a $500 employer HSA contribution
>>> plan_cost(40, [300, float("inf")], oop_max=5000, employer_hsa=500)
```

array(\[ 280., 4980.\])
