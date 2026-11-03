## emergency_fund_target()


Emergency fund target.


Usage

``` python
emergency_fund_target(
    monthly_expenses,
    months=3,
)
```


Essential monthly expenses times the number of months to cover. From the [Emergency Fund](https://mjfrigaard.github.io/fm-finance/emergency_fund.html) chapter.


## Parameters


`monthly_expenses: ArrayLike`  
Essential monthly expenses.

`months: ArrayLike = ``3`  
Months of expenses to cover. Defaults to 3.


## Returns


`float or numpy.ndarray`  
Target balances.


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values.


## Examples

``` python
>>> from perfinpy import emergency_fund_target
>>> # 3-month and 6-month targets on $2,400/month
>>> emergency_fund_target(monthly_expenses=2400, months=[3, 6])
```

array(\[ 7200., 14400.\])
