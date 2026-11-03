## income_tax()


Federal income tax for a single filer (2026 brackets).


Usage

``` python
income_tax(
    income,
    deduction=16100,
)
```


Subtracts the deduction, then taxes each slice of taxable income at its bracket's rate. Uses the 2026 single filer brackets and standard deduction. From the [Taxes](https://mjfrigaard.github.io/fm-finance/taxes.html) chapter.


## Parameters


`income: float`  
Yearly gross income. A single number.

`deduction: float = ``16100`  
Deduction subtracted before tax. Defaults to 16100 (the 2026 standard deduction). A single number.


## Returns


`float`  
Tax owed.


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values or is not a single number.


## See Also

[raise_kept()](raise_kept.md#perfinpy.raise_kept)  
How much of a raise you keep after tax.


## Examples

``` python
>>> from perfinpy import income_tax
>>> income_tax(income=45000)
```

3220.0

``` python
>>> # effective rate
>>> income_tax(income=45000) / 45000
```

0.0715
