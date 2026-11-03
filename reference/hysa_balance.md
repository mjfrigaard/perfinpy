## hysa_balance()


High-yield savings account balance.


Usage

``` python
hysa_balance(
    principal,
    annual_apy,
    years=1,
)
```


Grows `principal` at `annual_apy` for `years`. From the [High-Yield Savings Accounts](https://mjfrigaard.github.io/fm-finance/high_yield_accounts.html) chapter.


## Parameters


`principal: ArrayLike`  
Starting balance.

`annual_apy: ArrayLike`  
Annual percentage yield, as a decimal.

`years: ArrayLike = ``1`  
Number of years. Defaults to 1.


## Returns


`float or numpy.ndarray`  
Ending balances.


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values.


## Examples

``` python
>>> from perfinpy import hysa_balance
>>> # $9,600 at 4% APY after 1 and 5 years
>>> hysa_balance(principal=9600, annual_apy=0.04, years=[1, 5])
```

array(\[ 9984. , 11679.86786304\])
