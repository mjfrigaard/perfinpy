## total_interest()


Total interest paid over the life of a loan.


Usage

``` python
total_interest(
    monthly_payment,
    n_months,
    principal,
)
```


All payments minus the amount borrowed. From the [Managing Debt](https://mjfrigaard.github.io/fm-finance/managing_debt.html) chapter.


## Parameters


`monthly_payment: ArrayLike`  
Fixed monthly payment.

`n_months: ArrayLike`  
Number of payments.

`principal: ArrayLike`  
Amount borrowed.


## Returns


`float or numpy.ndarray`  
Interest paid.


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values.


## Examples

``` python
>>> from perfinpy import total_interest
>>> # 6-year vs. 4-year car loan, $20,000 at 7%
>>> total_interest(monthly_payment=[340.98, 478.92], n_months=[72, 48],
...                principal=20000)
```

array(\[4550.56, 2988.16\])
