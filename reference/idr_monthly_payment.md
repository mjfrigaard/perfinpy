## idr_monthly_payment()


Income driven repayment (IDR) monthly payment.


Usage

``` python
idr_monthly_payment(
    agi, poverty_guideline=15960, threshold_pct=1.5, payment_rate=0.1
)
```


Discretionary income is adjusted gross income (AGI) above `threshold_pct` times the poverty guideline. The yearly payment is `payment_rate` of that, split into 12 months and rounded to cents. From the [Managing Debt](https://mjfrigaard.github.io/fm-finance/managing_debt.html) chapter.


## Parameters


`agi: ArrayLike`  
Adjusted gross income.

`poverty_guideline: ArrayLike = ``15960`  
Federal poverty guideline for the household size. Defaults to 15960 (one person).

`threshold_pct: ArrayLike = ``1.5`  
Multiple of the poverty guideline that is protected. Defaults to 1.5 (150%).

`payment_rate: ArrayLike = ``0.1`  
Share of discretionary income paid each year. Defaults to 0.10.


## Returns


`float or numpy.ndarray`  
Monthly payments.


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values.


## Examples

``` python
>>> from perfinpy import idr_monthly_payment
>>> # IBR: $50,000 AGI, 150% threshold, 10% rate
>>> idr_monthly_payment(agi=50000)
```

217.17

``` python
>>> # IBR for loans before July 2014: 15% rate
>>> idr_monthly_payment(agi=50000, payment_rate=0.15)
```

325.75
