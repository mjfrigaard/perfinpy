## raise_kept()


How much of a raise you keep after federal income tax.


Usage

``` python
raise_kept(
    old_income,
    raise_amount,
)
```


The raise minus the extra tax it adds, using [income_tax()](income_tax.md#perfinpy.income_tax). From the [Taxes](https://mjfrigaard.github.io/fm-finance/taxes.html) chapter.


## Parameters


`old_income: float`  
Yearly gross income before the raise. A single number.

`raise_amount: float`  
Size of the raise. A single number.


## Returns


`float`  
Amount of the raise kept after tax.


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values or is not a single number.


## See Also

[income_tax()](income_tax.md#perfinpy.income_tax)  
The tax calculation used here.


## Examples

``` python
>>> from perfinpy import raise_kept
>>> # $2,000 raise on a $66,000 salary
>>> raise_kept(old_income=66000, raise_amount=2000)
```

1610.0
