## real_return()


Real (inflation adjusted) return.


Usage

``` python
real_return(
    nominal,
    inflation,
)
```


From the [Investing Basics](https://mjfrigaard.github.io/fm-finance/investing_basics.html) chapter.


## Parameters


`nominal: ArrayLike`  
Nominal yearly return, as a decimal.

`inflation: ArrayLike`  
Yearly inflation rate, as a decimal.


## Returns


`float or numpy.ndarray`  
Real returns, as decimals.


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values.


## Examples

``` python
>>> from perfinpy import real_return
>>> real_return(nominal=0.07, inflation=0.03)
```

0.03883
