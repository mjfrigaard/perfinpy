## monthly_standard_payment()


Monthly payment on a standard student loan repayment plan.


Usage

``` python
monthly_standard_payment(
    principal,
    annual_rate=0.065,
    years=10,
)
```


The same amortization formula as [mortgage_payment()](mortgage_payment.md#perfinpy.mortgage_payment), with student loan defaults (6.5% over 10 years). From the [Managing Debt](https://mjfrigaard.github.io/fm-finance/managing_debt.html) chapter.


## Parameters


`principal: ArrayLike`  
Amount borrowed.

`annual_rate: ArrayLike = ``0.065`  
Yearly interest rate, as a decimal. Defaults to 0.065.

`years: ArrayLike = ``10`  
Repayment term in years. Defaults to 10. Must be greater than 0.


## Returns


`float or numpy.ndarray`  
Monthly payments.


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values, or `years` is not greater than 0.


## See Also

[mortgage_payment()](mortgage_payment.md#perfinpy.mortgage_payment)  
The general amortization formula.


## Examples

``` python
>>> from perfinpy import monthly_standard_payment
>>> monthly_standard_payment(principal=45000)
```

510.96
