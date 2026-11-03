# Income

A bigger paycheck only builds wealth if some of it stays put. The book's [Income](https://mjfrigaard.github.io/fm-finance/income.html) chapter turns that idea into three questions. How much does steady saving grow into? How much of each paycheck is committed before you spend a dollar? And what is a raise worth if you invest part of it? In this page I'll answer each one with `perfinpy`, using the same numbers as the chapter.

| Function | Returns | Units |
|----|----|----|
| [wealth_formula()](../reference/wealth_formula.md#perfinpy.wealth_formula) | the balance after saving part of a yearly income every year | dollars; rates go in as decimals |
| [fixed_cost_ratio()](../reference/fixed_cost_ratio.md#perfinpy.fixed_cost_ratio) | monthly fixed costs as a share of take home pay | percent (`55`, not `0.55`) |
| [raise_invested_value()](../reference/raise_invested_value.md#perfinpy.raise_invested_value) | the balance after investing part of a monthly raise every month | dollars; rates go in as decimals |

The units follow the package conventions described in [Get started](get-started.md): rates go in as decimals and ratios come out as percents.


# How much does steady saving grow into?

The chapter builds on Scott Galloway's wealth formula (focus plus stoicism, time, and diversification multiplied together). To put numbers on it, the book uses a worker who earns about the 2025 median for full time workers. This worker saves a fixed share of income every year and invests it. The scenario below sets those inputs:


``` python
income = 62400
save_pct = 0.15
annual_return = 0.08
wealth_years = 40
```


This worker earns \$62,400 a year and saves 15% of it, which comes to \$9,360 a year. Those savings earn 8% a year for 40 years. Each bar below is the balance at a checkpoint, split into the money put in and what it grew into.


<figure class="figure">
<p><img src="assets/income-wealth-bar-model.png" class="img-fluid figure-img" alt="Stacked bar chart of savings at years 10, 20, 30, and 40 from depositing $9,360 a year at 8%. Each bar splits into money put in (green, bottom) and growth (blue, top). The bar totals are $136k, $428k, $1,060k, and $2,425k. Growth is the smaller layer at year 10 and fills most of the bar by year 40." /></p>
<figcaption>Money put in vs. growth at each checkpoint</figcaption>
</figure>


The green layer rises in a straight line because it is one deposit per year. The blue layer is every deposit growing for the years it has left, and it is the part that takes over. [wealth_formula()](../reference/wealth_formula.md#perfinpy.wealth_formula) adds up all of those growing deposits in one call:


``` python
wealth_40 = wealth_formula(
    median_income=income,
    savings_rate=save_pct,
    annual_return=annual_return,
    years=wealth_years,
)
wealth_40
```


    2424769.0151255885


After 40 years the balance is about \$2,424,769. Only \$374,400 of that is money the worker put in; the other \$2,050,369 is growth.


# How much of your paycheck is already spoken for?

Fixed costs (rent, loan payments, insurance, utilities) are the bills you can't easily change from one month to the next. The book's example is a first job with these monthly numbers:


``` python
fixed_costs = 1760
take_home = 3200
ceiling_pct = 60
```


This paycheck brings in \$3,200 of take home pay a month, and \$1,760 of it goes to fixed costs. The book suggests keeping fixed costs under 60% of take home pay, which is \$1,920 here. The bar below cuts the paycheck into ten equal pieces and marks that ceiling.


<figure class="figure">
<p><img src="assets/income-fixed-cost-bar-model.png" class="img-fluid figure-img" alt="Bar model: one horizontal bar for $3,200 of take home pay, divided by white lines into ten $320 pieces. Fixed costs of $1,760 (vermillion) fill five and a half pieces, and flexible spending of $1,440 (light green) fills the rest. A dashed line marks the 60% ceiling at $1,920, just to the right of where fixed costs end." /></p>
<figcaption>Take home pay split into fixed costs and flexible spending</figcaption>
</figure>


[fixed_cost_ratio()](../reference/fixed_cost_ratio.md#perfinpy.fixed_cost_ratio) divides the fixed costs by take home pay and returns a percent:


``` python
ratio = fixed_cost_ratio(fixed_costs=fixed_costs, take_home=take_home)
ratio
```


    55.00000000000001


Fixed costs take 55% of this paycheck, under the 60% ceiling. That leaves \$160 of room before a new commitment pushes the budget past it. The [Budgeting](budgeting.md) page picks up from here and splits the flexible part of the paycheck.


# What is a raise really worth?

The chapter recommends splitting every raise: half goes to your lifestyle and half gets invested. The book's raise adds a fixed amount to monthly take home pay:


``` python
monthly_raise = 400
share = 0.5
raise_rate = 0.07
raise_years = 25
```


A raise of \$400 a month split in half sends \$200 a month into investments. That money earns 7% a year for 25 years. The bars below show the balance at each checkpoint.


<figure class="figure">
<p><img src="assets/income-raise-value-bar-model.png" class="img-fluid figure-img" alt="Stacked bar chart of $200 a month invested at a 7% annual return, at years 5, 10, 15, 20, and 25. Each bar splits into money put in (green, bottom) and growth (blue, top). The bar totals are $14k, $35k, $63k, $104k, and $162k. By year 25 the growth layer is larger than the money put in." /></p>
<figcaption>A monthly raise contribution invested at each checkpoint</figcaption>
</figure>


[raise_invested_value()](../reference/raise_invested_value.md#perfinpy.raise_invested_value) takes the whole raise and the share you invest, then compounds the contributions monthly:


``` python
raise_value = raise_invested_value(
    monthly_raise=monthly_raise,
    invest_share=share,
    rate=raise_rate,
    years=raise_years,
)
raise_value
```


    162014.33860462217


Half of the raise grows to about \$162,014. The contributions add up to \$60,000, so growth adds about \$102,014. The [Investing Basics](investing-basics.md) page returns to this future value of contributions formula with [future_value_series()](../reference/future_value_series.md#perfinpy.future_value_series).


# Variations

Both growth functions accept arrays, so we can compare options in one call. The savings rate is the stoicism lever in Galloway's formula. The code below keeps the income, return, and horizon from the first section and changes only the share saved:


``` python
rates = [0.10, 0.15, 0.20]
pl.DataFrame({
    "savings_rate": rates,
    "yearly_savings": [income * r for r in rates],
    "wealth": wealth_formula(
        median_income=income,
        savings_rate=rates,
        annual_return=annual_return,
        years=wealth_years,
    ),
})
```


shape: (3, 3)

| savings_rate | yearly_savings | wealth   |
|--------------|----------------|----------|
| f64          | f64            | f64      |
| 0.1          | 6240.0         | 1.6165e6 |
| 0.15         | 9360.0         | 2.4248e6 |
| 0.2          | 12480.0        | 3.2330e6 |


The same idea works for the raise. Here is the \$400 raise with a quarter, half, three quarters, and all of it invested:


``` python
shares = [0.25, 0.50, 0.75, 1.0]
pl.DataFrame({
    "invest_share": shares,
    "per_month": [monthly_raise * s for s in shares],
    "value": raise_invested_value(
        monthly_raise=monthly_raise,
        invest_share=shares,
        rate=raise_rate,
        years=raise_years,
    ),
})
```


shape: (4, 3)

| invest_share | per_month | value         |
|--------------|-----------|---------------|
| f64          | f64       | f64           |
| 0.25         | 100.0     | 81007.169302  |
| 0.5          | 200.0     | 162014.338605 |
| 0.75         | 300.0     | 243021.507907 |
| 1.0          | 400.0     | 324028.677209 |


Both tables scale in a straight line with the share saved because the return and horizon don't change. The horizon is where the curve bends, as the bar models above show.

> **Warning: Limits**
>
> - [wealth_formula()](../reference/wealth_formula.md#perfinpy.wealth_formula) assumes one deposit at the end of every year, the same income every year (no raises), and the same return every year. It ignores taxes, fees, and inflation, so results are in future dollars.
> - [raise_invested_value()](../reference/raise_invested_value.md#perfinpy.raise_invested_value) makes the same assumptions with a deposit at the end of every month and monthly compounding.
> - A 0% return in either function gives the plain sum of the deposits instead of `nan`.
> - [fixed_cost_ratio()](../reference/fixed_cost_ratio.md#perfinpy.fixed_cost_ratio) raises a `ValueError` when `take_home` is 0 or negative. It doesn't decide which bills count as fixed, and the 60% ceiling is a guideline from the book, not an argument.
> - The growth functions reject text and `nan` but not negative values, so check the signs of your inputs.


# Putting it together

The worker from the fixed cost section gets the \$400 raise. Investing half is the easy part; the real question is where the lifestyle half goes. If it stays flexible (dinners, trips), fixed costs don't change. If it goes to a pricier apartment, fixed costs rise by the full lifestyle half. The code below compares the fixed cost ratio before the raise and under both choices:


``` python
new_take_home = take_home + monthly_raise
plans = pl.DataFrame({
    "plan": [
        "before the raise",
        "lifestyle half stays flexible",
        "lifestyle half goes to rent",
    ],
    "fixed_costs": [
        float(fixed_costs),
        float(fixed_costs),
        fixed_costs + monthly_raise * (1 - share),
    ],
    "take_home": [take_home, new_take_home, new_take_home],
})
plans = plans.with_columns(
    ratio=fixed_cost_ratio(
        fixed_costs=plans["fixed_costs"].to_numpy(),
        take_home=plans["take_home"].to_numpy(),
    )
)
plans
```


shape: (3, 4)

| plan                            | fixed_costs | take_home | ratio     |
|---------------------------------|-------------|-----------|-----------|
| str                             | f64         | i64       | f64       |
| "before the raise"              | 1760.0      | 3200      | 55.0      |
| "lifestyle half stays flexible" | 1760.0      | 3600      | 48.888889 |
| "lifestyle half goes to rent"   | 1960.0      | 3600      | 54.444444 |


Keeping the lifestyle half flexible drops the ratio to 48.9%. Moving it into rent leaves the ratio at 54.4%, almost where it started, so the raise buys very little breathing room. This is the lifestyle inflation the chapter warns about: the upgrade becomes a permanent bill.

The invested half grows the same way in both plans. The code below values it twice: once with monthly deposits, and once with a single deposit at the end of each year. The yearly version uses [wealth_formula()](../reference/wealth_formula.md#perfinpy.wealth_formula), whose `median_income` argument accepts any yearly amount:


``` python
monthly_value = raise_invested_value(
    monthly_raise=monthly_raise,
    invest_share=share,
    rate=raise_rate,
    years=raise_years,
)
yearly_value = wealth_formula(
    median_income=monthly_raise * 12,
    savings_rate=share,
    annual_return=raise_rate,
    years=raise_years,
)
monthly_value, yearly_value
```


    (162014.33860462217, 151797.69051849932)


The same dollars come out about \$10,217 ahead when they're invested every month. Each monthly deposit starts growing sooner, which is one more reason to automate the transfer the day the raise arrives.


# Recap

[wealth_formula()](../reference/wealth_formula.md#perfinpy.wealth_formula) and [raise_invested_value()](../reference/raise_invested_value.md#perfinpy.raise_invested_value) show how a steady deposit turns into a balance that is mostly growth. Time does more of the work than the deposits do. [fixed_cost_ratio()](../reference/fixed_cost_ratio.md#perfinpy.fixed_cost_ratio) tells you how much of each paycheck is committed before you spend anything, and returns a percent you can compare against the 60% ceiling. Together they make the chapter's advice measurable: keep fixed costs low, and invest part of every raise before your lifestyle absorbs it.

- [Income](https://mjfrigaard.github.io/fm-finance/income.html) in Personal Finance: a field manual
- Reference: [wealth_formula()](../reference/wealth_formula.md#perfinpy.wealth_formula), [fixed_cost_ratio()](../reference/fixed_cost_ratio.md#perfinpy.fixed_cost_ratio), [raise_invested_value()](../reference/raise_invested_value.md#perfinpy.raise_invested_value)
- Next: [Tracking Spending](tracking-spending.md)
