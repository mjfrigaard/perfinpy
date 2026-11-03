# High-Yield Savings Accounts

Where should your savings live, and what does that choice earn? The [High-Yield Savings Accounts](https://mjfrigaard.github.io/fm-finance/high_yield_accounts.html) chapter of the book makes the case for a high yield savings account (HYSA) at an online bank: it's insured, you can reach the money in a day or two, and it pays far more than a big bank's basic savings account. In this page I'll put numbers on that case with [hysa_balance()](../reference/hysa_balance.md#perfinpy.hysa_balance), using the chapter's \$9,600 emergency fund so you can check every result against the book.


# The high yield accounts function

[hysa_balance()](../reference/hysa_balance.md#perfinpy.hysa_balance) follows the conventions on the [Get started](get-started.md) page: the APY goes in as a decimal, and every argument accepts arrays.

| Function | Returns | Units |
|----|----|----|
| [hysa_balance()](../reference/hysa_balance.md#perfinpy.hysa_balance) | the balance after growing at an APY for some years | dollars (`annual_apy` is a decimal; `years` defaults to 1) |


# How much does an emergency fund earn in a year?

The chapter follows the \$9,600 emergency fund from [Emergency Fund](emergency-fund.md) into a HYSA paying 4% APY. The APY (annual percentage yield) already includes daily compounding, so a year of growth is one multiplication by 1.04:


``` python
one_year = hysa_balance(principal=9600, annual_apy=0.04)
one_year, one_year - 9600
```


    (9984.0, 384.0)


After one year the fund holds \$9,984, and \$384 of that is interest. `years` defaults to 1, so the call above doesn't need it.


# How does the balance grow year by year?

Leave the money alone and each year multiplies the previous balance by 1.04 again. The chapter draws each year as a bar split into the money you put in and the interest it has earned so far:


<figure class="figure">
<p><img src="assets/high-yield-accounts-hysa-bar-model.png" class="img-fluid figure-img" alt="Stacked bar chart of a $9,600 deposit at 4% APY over years 0 through 5. Each bar has the same bluish green base for the $9,600 deposit, topped by a blue layer for interest earned that grows each year. Bar totals read $9,600, $9,984, $10,383, $10,799, $11,231, and $11,680." /></p>
<figcaption>$9,600 at 4% APY: deposit and interest earned, year by year</figcaption>
</figure>


The bluish green base never changes; only the blue interest layer grows. Passing several values to `years` reproduces every bar in one call:


``` python
years = list(range(6))
balances = hysa_balance(principal=9600, annual_apy=0.04, years=years)
pl.DataFrame({
    "years": years,
    "deposit": [9600] * 6,
    "interest": balances - 9600,
    "balance": balances,
}).with_columns(pl.col("interest", "balance").round(2))
```


shape: (6, 4)

| years | deposit | interest | balance  |
|-------|---------|----------|----------|
| i64   | i64     | f64      | f64      |
| 0     | 9600    | 0.0      | 9600.0   |
| 1     | 9600    | 384.0    | 9984.0   |
| 2     | 9600    | 783.36   | 10383.36 |
| 3     | 9600    | 1198.69  | 10798.69 |
| 4     | 9600    | 1630.64  | 11230.64 |
| 5     | 9600    | 2079.87  | 11679.87 |


After five years the fund holds \$11,679.87, which is the chapter's \$11,680. That's \$2,080 of growth without putting a dollar of the deposit at risk.


# Variations

The chapter compares account types rather than banks. In late 2026 the national average savings rate was 0.39%, a big bank's basic account often paid 0.01%, and the best online accounts paid 3.8% to 4.2%. `annual_apy` accepts an array, so one call compares a \$10,000 balance across all of them:


``` python
apys = [0.0001, 0.0039, 0.038, 0.04, 0.042]
pl.DataFrame({
    "account": ["big bank basic", "national average", "online low", "online typical", "online high"],
    "apy": apys,
    "interest_year_1": hysa_balance(principal=10000, annual_apy=apys) - 10000,
}).with_columns(pl.col("interest_year_1").round(2))
```


shape: (5, 3)

| account            | apy    | interest_year_1 |
|--------------------|--------|-----------------|
| str                | f64    | f64             |
| "big bank basic"   | 0.0001 | 1.0             |
| "national average" | 0.0039 | 39.0            |
| "online low"       | 0.038  | 380.0           |
| "online typical"   | 0.04   | 400.0           |
| "online high"      | 0.042  | 420.0           |


The gap between online banks is small: \$40 a year separates the low and high ends on \$10,000. The gap between an online bank and a big bank's basic account is large: \$400 against \$1. As the chapter puts it, pick an online HYSA and don't overthink which one.

> **Warning: Limits**
>
> [hysa_balance()](../reference/hysa_balance.md#perfinpy.hysa_balance) grows one lump sum at one rate, so it leaves out a few things:
>
> - It assumes the APY never changes. Real HYSA rates move with interest rates, sometimes several times a year.
> - It doesn't add deposits along the way. For a fixed monthly deposit, use [future_value_series()](../reference/future_value_series.md#perfinpy.future_value_series) from [Investing Basics](investing-basics.md).
> - It ignores taxes on interest and inflation.
> - It doesn't know about the \$250,000 FDIC limit per account holder per bank. Balances above that need a second bank.
> - It checks that inputs are numbers, not that they make sense. A negative `annual_apy` or `years` returns a result instead of an error.


# Putting it together

The chapter's two headline numbers are an APY and an emergency fund, and both come from other chapters' functions. Banks sometimes advertise an APR, the rate before compounding. [apr_to_apy()](../reference/apr_to_apy.md#perfinpy.apr_to_apy) from [Managing Debt](managing-debt.md) converts it with daily compounding, the way most HYSAs pay:


``` python
apy = apr_to_apy(apr=0.0392)
apy
```


    0.03997626956226452


A 3.92% APR compounded daily is an APY of 4.00%. Next, [emergency_fund_target()](../reference/emergency_fund_target.md#perfinpy.emergency_fund_target) from [Emergency Fund](emergency-fund.md) sets the balance to park: four months of \$2,400 in essential expenses. We can then compare that fund after five years in the HYSA and in a big bank's basic account:


``` python
ef_target = emergency_fund_target(monthly_expenses=2400, months=4)
in_hysa = hysa_balance(principal=ef_target, annual_apy=apy, years=5)
in_basic = hysa_balance(principal=ef_target, annual_apy=0.0001, years=5)
ef_target, round(in_hysa, 2), round(in_basic, 2)
```


    (9600.0, 11678.54, 9604.8)


The same \$9,600 fund grows to \$11,678.54 in the HYSA and \$9,604.80 at the big bank, a difference of \$2,074. Finally, [ef_growth()](../reference/ef_growth.md#perfinpy.ef_growth) from the Emergency Fund chapter does the same math in months, which helps when a goal doesn't land on a whole year:


``` python
ef_growth(balance=ef_target, apy=0.04, months=[12, 18])
```


    array([ 9984.        , 10181.72216474])


Twelve months matches [hysa_balance()](../reference/hysa_balance.md#perfinpy.hysa_balance) with the default one year, and 18 months shows the balance halfway through year two.


# Recap

A HYSA keeps your savings safe and reachable while paying hundreds of times what a basic account pays. [hysa_balance()](../reference/hysa_balance.md#perfinpy.hysa_balance) grows a balance at an APY, and passing several years or several APYs compares horizons and accounts in one call. With [apr_to_apy()](../reference/apr_to_apy.md#perfinpy.apr_to_apy), [emergency_fund_target()](../reference/emergency_fund_target.md#perfinpy.emergency_fund_target), and [ef_growth()](../reference/ef_growth.md#perfinpy.ef_growth), it shows what an emergency fund earns while it waits.

- [High-Yield Savings Accounts](https://mjfrigaard.github.io/fm-finance/high_yield_accounts.html) in Personal Finance: a field manual
- Reference: [hysa_balance()](../reference/hysa_balance.md#perfinpy.hysa_balance)
- Next: [Automating Savings](automating-savings.md)
