## dti_ratio()


Debt to income ratio.


Usage

``` python
dti_ratio(
    monthly_debt_payments,
    gross_monthly_income,
)
```


Monthly debt payments as a percent of gross monthly income. From the [Managing Debt](https://mjfrigaard.github.io/fm-finance/managing_debt.html) chapter.


## Parameters


`monthly_debt_payments: ArrayLike`  
Total monthly debt payments.

`gross_monthly_income: ArrayLike`  
Monthly income before taxes. Must be greater than 0.


## Returns


`float or numpy.ndarray`  
Percentages (`28.3` is 28.3%).


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values, or `gross_monthly_income` is not greater than 0.


## Examples

``` python
>>> from perfinpy import dti_ratio
>>> dti_ratio(monthly_debt_payments=1061, gross_monthly_income=3750)
```

28.29
