## mortgage_payment()


Monthly payment on a fixed rate loan.


Usage

``` python
mortgage_payment(
    principal,
    annual_rate,
    years,
)
```


The standard amortization formula with monthly compounding. A 0% rate gives `principal / (years * 12)`. From the [Major Purchases](https://mjfrigaard.github.io/fm-finance/major_purchases.html) chapter.


## Parameters


`principal: ArrayLike`  
Amount borrowed.

`annual_rate: ArrayLike`  
Yearly interest rate, as a decimal.

`years: ArrayLike`  
Loan term in years. Must be greater than 0.


## Returns


`float or numpy.ndarray`  
Monthly payments (principal and interest only).


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values, or `years` is not greater than 0.


## See Also

[first_payment_split()](first_payment_split.md#perfinpy.first_payment_split)  
Interest and principal in the first payment.

[monthly_standard_payment()](monthly_standard_payment.md#perfinpy.monthly_standard_payment)  
Student loan defaults.


## Examples

``` python
>>> from perfinpy import mortgage_payment
>>> # $480,000 loan at 6% over 30 years
>>> mortgage_payment(principal=480000, annual_rate=0.06, years=30)
```

2877.84
