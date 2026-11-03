## net_worth()


Net worth: total assets minus total debts.


Usage

``` python
net_worth(
    assets,
    debts,
)
```


From the [Estate Planning](https://mjfrigaard.github.io/fm-finance/estate_planning.html) chapter.


## Parameters


`assets: Mapping[str, float] | ArrayLike`  
Asset values, as a dict of name to amount or a sequence of amounts.

`debts: Mapping[str, float] | ArrayLike`  
Debt balances, as a dict of name to amount or a sequence of amounts.


## Returns


`float`  
Net worth.


## Raises


`TypeError`  
If a value is not numeric.

`ValueError`  
If a value is missing.


## Examples

``` python
>>> from perfinpy import net_worth
>>> assets = {"401k": 12000, "roth_ira": 6000, "savings": 8000, "car": 9000}
>>> debts = {"car_loan": 6000, "credit_card": 1000}
>>> net_worth(assets, debts)
```

28000.0
