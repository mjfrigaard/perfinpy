## loan_income_ratio()


Total student loans as a multiple of expected starting salary.


Usage

``` python
loan_income_ratio(
    loan_total,
    expected_salary,
)
```


A ratio at or below 1 means you borrow no more than your first year's salary. From the [Managing Debt](https://mjfrigaard.github.io/fm-finance/managing_debt.html) chapter.


## Parameters


`loan_total: ArrayLike`  
Total amount borrowed.

`expected_salary: ArrayLike`  
Expected yearly starting salary. Must be greater than 0.


## Returns


`float or numpy.ndarray`  
Ratios (`1.07` is 107% of salary).


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values, or `expected_salary` is not greater than 0.


## Examples

``` python
>>> from perfinpy import loan_income_ratio
>>> loan_income_ratio(loan_total=45000, expected_salary=42000)
```

1.0714
