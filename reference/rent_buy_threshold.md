## rent_buy_threshold()


Monthly rent that matches the unrecoverable cost of owning.


Usage

``` python
rent_buy_threshold(
    home_value,
    unrecoverable_rate=0.05,
)
```


The 5% rule: property tax, maintenance, and the cost of capital come to about 5% of the home's value each year. Rent below this monthly amount favors renting. From the [Major Purchases](https://mjfrigaard.github.io/fm-finance/major_purchases.html) chapter.


## Parameters


`home_value: ArrayLike`  
Price of the home.

`unrecoverable_rate: ArrayLike = ``0.05`  
Yearly unrecoverable cost, as a decimal. Defaults to 0.05.


## Returns


`float or numpy.ndarray`  
Monthly rent thresholds.


## Raises


`TypeError`  
If an argument is not numeric.

`ValueError`  
If an argument contains missing values.


## Examples

``` python
>>> from perfinpy import rent_buy_threshold
>>> rent_buy_threshold(home_value=500000)
```

2083.33
