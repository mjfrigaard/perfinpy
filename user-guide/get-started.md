# Get started

`perfinpy` holds the Python functions from [Personal Finance: a field manual](https://mjfrigaard.github.io/fm-finance/). Each chapter of the book builds its calculations from scratch so you can see how the formula works. This package collects those same functions, documents them, and tests them, so you can use them without copying code out of the book. On this page I'll cover how to install `perfinpy` and the conventions every function follows. Then we'll take a short tour with one example from each part of the book.


# Installation

`perfinpy` isn't on PyPI. Install the development version from GitHub:

``` bash
uv pip install git+https://github.com/mjfrigaard/perfinpy
```

`perfinpy` depends on `numpy` and `polars`. If you work in R, the same functions are in [perfinr](https://mjfrigaard.github.io/perfinr/).


# Conventions

The functions keep the names, arguments, and defaults from the book, so code from a chapter runs unchanged after `from perfinpy import *`. A few rules hold across the whole package:

| Rule | Example |
|----|----|
| Rates and returns are decimals | `0.07` is 7% |
| The one exception is [rule_of_72()](../reference/rule_of_72.md#perfinpy.rule_of_72), which takes a percent | `rule_of_72(7)` |
| Ratio functions return percents | `percent_of_income(1500, 5000)` returns `30.0`, not `0.30` |
| Two ratios stay decimals, as in the book | [loan_income_ratio()](../reference/loan_income_ratio.md#perfinpy.loan_income_ratio) (`1.07`) and [beneficiary_share()](../reference/beneficiary_share.md#perfinpy.beneficiary_share) (`0.8875`) |
| Most functions accept arrays | `future_value(10000, 0.07, [10, 20])` returns a `numpy` array |
| Single numbers in, a `float` out | `future_value(10000, 0.07, 10)` returns a `float` |
| A few functions take single values only | [income_tax()](../reference/income_tax.md#perfinpy.income_tax), [raise_kept()](../reference/raise_kept.md#perfinpy.raise_kept), [payoff_vs_invest()](../reference/payoff_vs_invest.md#perfinpy.payoff_vs_invest), [first_payment_split()](../reference/first_payment_split.md#perfinpy.first_payment_split) |
| A 0% rate returns the no interest answer | `mortgage_payment(120000, 0, 30)` is `120000 / 360` |
| Bad inputs raise an error | text raises `TypeError`; `nan`, or a zero where a divisor is needed, raises `ValueError` |

Array inputs make it easy to compare options side by side. Here is the same \$10,000 at 7% over four horizons:


``` python
years = [5, 10, 20, 30]
pl.DataFrame({
    "years": years,
    "value": future_value(present_value=10000, rate=0.07, years=years),
})
```


shape: (4, 2)

| years | value        |
|-------|--------------|
| i64   | f64          |
| 5     | 14025.517307 |
| 10    | 19671.513573 |
| 20    | 38696.844625 |
| 30    | 76122.550427 |


When an input doesn't make sense, the function says which argument is wrong instead of returning `inf` or `nan`:


``` python
percent_of_income(expense=1500, income=0)
```


    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)
    Cell In[3], line 1
    ----> 1 percent_of_income(expense=1500, income=0)

    File ~/projects/pkgs/Python/perfinpy/src/perfinpy/budgeting.py:46, in percent_of_income(expense, income)
         13 """An expense as a percent of income.
         14 
         15 `expense` and `income` must cover the same period. From the
       (...)     43 30.0
         44 """
         45 expense = _as_numeric(expense, "expense")
    ---> 46 income = _as_positive(income, "income")
         47 return (expense / income) * 100

    File ~/projects/pkgs/Python/perfinpy/src/perfinpy/_checks.py:38, in _as_positive(x, arg)
         36 out = _as_numeric(x, arg)
         37 if np.any(np.asarray(out) <= 0):
    ---> 38     raise ValueError(f"`{arg}` must be greater than 0.")
         39 return out

    ValueError: `income` must be greater than 0.


# How the user guide maps to the book

There is one page for each chapter of the book. Each one takes the chapter's examples (with the same numbers), shows the bar model, and then answers the question with perfinpy functions.


*\[Rich HTML output -- view on the documentation site\]*


# A short tour

Each example below uses the numbers from the book, so you can check the result against the chapter.


## Foundations

Rent of \$1,500 on a \$5,000 monthly income:


``` python
rent_share = percent_of_income(expense=1500, income=5000)
rent_share
```


    30.0


Rent takes 30% of income. A \$5,000 credit card balance at 22% APR, paying \$100 a month:


``` python
payoff = months_to_payoff(balance=5000, monthly_payment=100, apr=0.22)
payoff
```


    136.77905405676316


That is about 11.4 years of payments.


## Savings

Spending \$2,720 of a \$3,200 take home paycheck:


``` python
savings_rate(income=3200, spending=2720)
```


    15.0


## Investing

\$10,000 invested at 7% for 10 years:


``` python
future_value(present_value=10000, rate=0.07, years=10)
```


    19671.513572895663


## Taxes and insurance

2026 federal income tax on a \$45,000 salary (single filer), and the effective rate:


``` python
tax = income_tax(income=45000)
tax, tax / 45000
```


    (3220.0, 0.07155555555555555)


The effective rate is 7.2%, well below the 12% top bracket this salary reaches.


## Planning

The monthly payment on a \$480,000 mortgage at 6% over 30 years:


``` python
mortgage_payment(principal=480000, annual_rate=0.06, years=30)
```


    2877.842520733233


# Recap

perfinpy gives you the book's functions as a tested package. Rates go in as decimals, ratios come out as percents, and most functions accept arrays so you can compare options in one call. The chapter pages walk through each part of the book in the same order as the chapters.

Foundations:

- [Income](income.md)
- [Tracking Spending](tracking-spending.md)
- [Budgeting](budgeting.md)
- [Managing Debt](managing-debt.md)
- [Emergency Fund](emergency-fund.md)

Savings:

- [Savings Strategies](savings-strategies.md)
- [High-Yield Savings Accounts](high-yield-accounts.md)
- [Automating Savings](automating-savings.md)

Investing:

- [Investing Basics](investing-basics.md)
- [Retirement Accounts](retirement-accounts.md)
- [Index Funds](index-funds.md)
- [Asset Allocation](asset-allocation.md)

Taxes and insurance:

- [Taxes](taxes.md)
- [Insurance](insurance.md)

Planning:

- [Financial Goals](financial-goals.md)
- [Major Purchases](major-purchases.md)
- [Estate Planning](estate-planning.md)
