## apply_rules()


Categorize transactions with keyword rules.


Usage

``` python
apply_rules(
    df,
    rules,
)
```


Each row of `rules` holds a regular expression (`Pattern`) and the `Category` it assigns. Rules are tried in order and the first match wins; matching ignores case. Descriptions that match no rule get `"Other"`. From the [Tracking Spending](https://mjfrigaard.github.io/fm-finance/tracking_spending.html) chapter.


## Parameters


`df: pl.DataFrame`  
Transactions with a string `Description` column.

`rules: pl.DataFrame`  
Rules with string `Pattern` and `Category` columns.


## Returns


`polars.DataFrame`  
`df` with a `Category` column added (or replaced).


## Raises


`TypeError`  
If `df` or `rules` is not a polars DataFrame.

`ValueError`  
If a required column is missing.


## Examples

``` python
>>> import polars as pl
>>> from perfinpy import apply_rules
>>> transactions = pl.DataFrame(
...     {"Description": ["SAFEWAY #123", "NETFLIX.COM", "ATM FEE"]}
... )
>>> rules = pl.DataFrame(
...     {"Pattern": ["safeway", "netflix"],
...      "Category": ["Groceries", "Subscriptions"]}
... )
>>> apply_rules(transactions, rules)["Category"].to_list()
```

\['Groceries', 'Subscriptions', 'Other'\]
