## order_snowball()


Order debts for the snowball method (smallest balance first).


Usage

``` python
order_snowball(debts)
```


From the [Managing Debt](https://mjfrigaard.github.io/fm-finance/managing_debt.html) chapter.


## Parameters


`debts: list[dict[str, Any]]`  
A list of dicts, each with a numeric `balance` key.


## Returns


`list of dict`  
A new list, sorted by `balance` from smallest to largest. Ties keep their original order.


## Raises


`TypeError`  
If `debts` is not a list of dicts, or a `balance` is not numeric.

`ValueError`  
If a debt has no `balance` key, or a `balance` is missing.


## See Also

[order_avalanche()](order_avalanche.md#perfinpy.order_avalanche)  
Highest APR first.


## Examples

``` python
>>> from perfinpy import order_snowball
>>> debts = [
...     {"name": "Card A", "balance": 1000, "apr": 0.18},
...     {"name": "Card B", "balance": 5000, "apr": 0.24},
...     {"name": "Card C", "balance": 2000, "apr": 0.15},
... ]
>>> [d["name"] for d in order_snowball(debts)]
```

\['Card A', 'Card C', 'Card B'\]
