## months_to_payoff()


Months to pay off a balance with a fixed payment.


Usage

``` python
months_to_payoff(
    balance,
    monthly_payment,
    apr,
)
```


Interest compounds monthly at `apr / 12`. The result is not rounded; the last payment is a partial one. From the [Managing Debt](https://mjfrigaard.github.io/fm-finance/managing_debt.html) chapter.


## Parameters


`balance: ArrayLike`  
Current balance. Must be greater than 0.

`monthly_payment: ArrayLike`  
Fixed monthly payment. Must be greater than 0.

`apr: ArrayLike`  
Annual percentage rate, as a decimal.


## Returns


`float or numpy.ndarray`  
Months.


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values, `balance` or `monthly_payment` is not greater than 0, or the payment does not cover the first month's interest (the balance would never be paid off).


## Examples

``` python
>>> from perfinpy import months_to_payoff
>>> # $5,000 balance, $100/month, 22% APR
>>> months_to_payoff(balance=5000, monthly_payment=100, apr=0.22)
```

136.779
