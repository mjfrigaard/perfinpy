## break_even_years()


Years of premium savings to cover a higher deductible.


Usage

``` python
break_even_years(
    high_deductible,
    low_deductible,
    yearly_savings,
)
```


If you go longer than this between claims, the higher deductible comes out ahead. From the [Insurance](https://mjfrigaard.github.io/fm-finance/insurance.html) chapter.


## Parameters


`high_deductible: ArrayLike`  
The higher deductible.

`low_deductible: ArrayLike`  
The lower deductible.

`yearly_savings: ArrayLike`  
Yearly premium saved by choosing the higher deductible. Must be greater than 0.


## Returns


`float or numpy.ndarray`  
Years.


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values, or `yearly_savings` is not greater than 0.


## Examples

``` python
>>> from perfinpy import break_even_years
>>> break_even_years(high_deductible=1000, low_deductible=500,
...                  yearly_savings=150)
```

3.33
