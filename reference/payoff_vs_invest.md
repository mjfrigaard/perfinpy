## payoff_vs_invest()


Pay off a debt or invest the difference.


Usage

``` python
payoff_vs_invest(
    loan_rate,
    expected_return,
)
```


Compares a loan's interest rate with an expected investment return. From the [Managing Debt](https://mjfrigaard.github.io/fm-finance/managing_debt.html) chapter.


## Parameters


`loan_rate: float`  
The loan's yearly interest rate, as a decimal. A single number.

`expected_return: float`  
Expected yearly investment return, as a decimal. A single number.


## Returns


`str`  
`"Pay off the debt"`, `"Invest the difference"`, or `"Roughly a wash; do both"`.


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values or is not a single number.


## Examples

``` python
>>> from perfinpy import payoff_vs_invest
>>> payoff_vs_invest(loan_rate=0.05, expected_return=0.07)
```

'Invest the difference'
