## first_payment_split()


Interest and principal in a loan's first monthly payment.


Usage

``` python
first_payment_split(
    principal,
    annual_rate,
    years,
)
```


From the [Major Purchases](https://mjfrigaard.github.io/fm-finance/major_purchases.html) chapter.


## Parameters


`principal: float`  
Amount borrowed. A single number.

`annual_rate: float`  
Yearly interest rate, as a decimal. A single number.

`years: float`  
Loan term in years. A single number greater than 0.


## Returns


`dict`  
Keys `payment`, `interest`, `principal`, and `pct_interest` (the share of the payment that is interest, as a percent).


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values or is not a single number, or `years` is not greater than 0.


## See Also

[mortgage_payment()](mortgage_payment.md#perfinpy.mortgage_payment)  
The payment formula used here.


## Examples

``` python
>>> from perfinpy import first_payment_split
>>> split = first_payment_split(principal=480000, annual_rate=0.06, years=30)
>>> {k: round(v, 2) for k, v in split.items()}
```

{'payment': 2877.84, 'interest': 2400.0, 'principal': 477.84, 'pct_interest': 83.4}
