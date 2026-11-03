## order_avalanche()


Order debts for the avalanche method (highest APR first).


Usage

``` python
order_avalanche(debts)
```


From the [Managing Debt](https://mjfrigaard.github.io/fm-finance/managing_debt.html) chapter.


## Parameters


`debts: list[dict[str, Any]]`  
A list of dicts, each with a numeric `apr` key.


## Returns


`list of dict`  
A new list, sorted by `apr` from highest to lowest. Ties keep their original order.


## Raises


`TypeError`  
If `debts` is not a list of dicts, or an `apr` is not numeric.

`ValueError`  
If a debt has no `apr` key, or an `apr` is missing.


## See Also

[order_snowball()](order_snowball.md#perfinpy.order_snowball)  
Smallest balance first.


## Examples

``` python
>>> from perfinpy import order_avalanche
>>> debts = [
...     {"name": "Card A", "balance": 1000, "apr": 0.18},
...     {"name": "Card B", "balance": 5000, "apr": 0.24},
...     {"name": "Card C", "balance": 2000, "apr": 0.15},
... ]
>>> [d["name"] for d in order_avalanche(debts)]
```

\['Card B', 'Card A', 'Card C'\]
