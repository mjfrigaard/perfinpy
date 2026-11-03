## rule_of_72()


Years for money to double, by the rule of 72.


Usage

``` python
rule_of_72(annual_return_pct)
```


The one function in the package that takes a percent rather than a decimal (`7`, not `0.07`). From the [Investing Basics](https://mjfrigaard.github.io/fm-finance/investing_basics.html) chapter.


## Parameters


`annual_return_pct: ArrayLike`  
Yearly return, as a percent. Must be greater than 0.


## Returns


`float or numpy.ndarray`  
Years to double.


## Raises


`TypeError`  
If `annual_return_pct` is not numeric.

`ValueError`  
If `annual_return_pct` contains missing values or is not greater than 0.


## Examples

``` python
>>> from perfinpy import rule_of_72
>>> rule_of_72(annual_return_pct=7)
```

10.28
