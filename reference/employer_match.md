## employer_match()


Yearly employer match on retirement contributions.


Usage

``` python
employer_match(
    salary,
    contribution_pct,
    match_limit_pct,
    match_rate,
)
```


The employer matches `match_rate` of your contributions, up to `match_limit_pct` of salary. From the [Retirement Accounts](https://mjfrigaard.github.io/fm-finance/retirement_accounts.html) chapter.


## Parameters


`salary: ArrayLike`  
Yearly salary.

`contribution_pct: ArrayLike`  
Share of salary you contribute, as a decimal.

`match_limit_pct: ArrayLike`  
Share of salary the employer matches up to, as a decimal.

`match_rate: ArrayLike`  
Share of each matched dollar the employer adds, as a decimal.


## Returns


`float or numpy.ndarray`  
Yearly employer contributions.


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values.


## Examples

``` python
>>> from perfinpy import employer_match
>>> # $45,000 salary, 50% match on the first 6%, contributing 6% or 3%
>>> employer_match(salary=45000, contribution_pct=[0.06, 0.03],
...                match_limit_pct=0.06, match_rate=0.50)
```

array(\[1350., 675.\])
