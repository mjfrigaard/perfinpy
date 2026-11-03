## beneficiary_share()


Share of assets that pass directly to a named beneficiary.


Usage

``` python
beneficiary_share(
    with_beneficiary,
    without_beneficiary,
)
```


Assets with a beneficiary (retirement accounts, life insurance, payable on death accounts) skip probate. From the [Estate Planning](https://mjfrigaard.github.io/fm-finance/estate_planning.html) chapter.


## Parameters


`with_beneficiary: Mapping[str, float] | ArrayLike`  
Values of assets with a named beneficiary, as a dict or a sequence.

`without_beneficiary: Mapping[str, float] | ArrayLike`  
Values of assets without one, as a dict or a sequence.


## Returns


`float`  
Share, as a decimal (`0.8875` is 88.75%).


## Raises


`TypeError`  
If a value is not numeric.

`ValueError`  
If a value is missing, or total assets are not greater than 0.


## Examples

``` python
>>> from perfinpy import beneficiary_share
>>> with_beneficiary = {"401k": 12000, "roth_ira": 6000,
...                     "life_insurance": 45000, "savings_pod": 8000}
>>> beneficiary_share(with_beneficiary, {"car": 9000})
```

0.8875
