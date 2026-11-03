# Tracking Spending

A bank export tells you every dollar that left your account, but it doesn't tell you where your money went. To answer that, each transaction needs a category, and the small recurring charges need a second look. The [Tracking Spending](https://mjfrigaard.github.io/fm-finance/tracking_spending.html) chapter of the book covers both questions. In this page I'll answer them with two perfinpy functions. [apply_rules()](../reference/apply_rules.md#perfinpy.apply_rules) sorts transactions into buckets. [subscription_opportunity_cost()](../reference/subscription_opportunity_cost.md#perfinpy.subscription_opportunity_cost) shows what a subscription would have grown to if you had invested the money instead.

| Function | Returns | Units |
|----|----|----|
| [apply_rules()](../reference/apply_rules.md#perfinpy.apply_rules) | the transactions with a `Category` column added | text categories; `"Other"` when nothing matches |
| [subscription_opportunity_cost()](../reference/subscription_opportunity_cost.md#perfinpy.subscription_opportunity_cost) | what the yearly cost grows to if invested | dollars; `rate` is a decimal (`0.07` is 7%) |


# Where did the money go?

The book starts with a January 2026 bank export. It has the three columns most banks include: `Date`, `Description`, and `Amount` (negative for money going out, positive for money coming in). The code below builds the same statement as a `polars` DataFrame:


``` python
bank_statement = pl.DataFrame({
    "Date": [
        "2026-01-02", "2026-01-02", "2026-01-03", "2026-01-03",
        "2026-01-04", "2026-01-04", "2026-01-05", "2026-01-06",
        "2026-01-07", "2026-01-08", "2026-01-09", "2026-01-10",
        "2026-01-11", "2026-01-12", "2026-01-13", "2026-01-14",
        "2026-01-15",
    ],
    "Description": [
        "Employer Payroll",     "Rent",
        "Comcast Internet",     "Trader Joe's",
        "Shell Gas",            "Netflix",
        "Starbucks",            "PG&E Electric",
        "AT&T Wireless",        "Spotify",
        "Whole Foods",          "Chipotle",
        "Geico Auto Insurance", "NYTimes Digital",
        "Shell Gas",            "Costco",
        "24 Hour Fitness",
    ],
    "Amount": [
         2400.00, -1500.00,
          -75.00,   -82.45,
          -45.20,   -15.99,
           -6.75,  -142.30,
          -85.00,   -10.99,
          -64.12,   -14.50,
         -125.00,   -17.00,
          -42.80,  -156.78,
          -39.99,
    ],
}).with_columns(pl.col("Date").str.to_date())
```


The statement has 17 transactions and no `Category` column. To add one, we map each description to a bucket with a lookup table of keyword patterns. Each `Pattern` is a regular expression (a text search pattern), so `|` means "or" and one rule can cover several merchants:


``` python
rules = pl.DataFrame({
    "Pattern": ["Payroll", "Rent", "Comcast|PG&E|AT&T",
                "Trader Joe|Whole Foods|Costco", "Shell",
                "Starbucks|Chipotle",
                "Netflix|Spotify|NYTimes|24 Hour Fitness", "Geico"],
    "Category": ["Income", "Housing", "Utilities", "Groceries",
                 "Transportation", "Dining", "Subscriptions", "Insurance"],
})
```


[apply_rules()](../reference/apply_rules.md#perfinpy.apply_rules) checks the 8 rules in order against each description and keeps the first match. The table below shows each transaction next to the bucket it landed in:


``` python
categorized = apply_rules(df=bank_statement, rules=rules)
categorized.select("Description", "Amount", "Category")
```


shape: (17, 3)

| Description            | Amount  | Category         |
|------------------------|---------|------------------|
| str                    | f64     | str              |
| "Employer Payroll"     | 2400.0  | "Income"         |
| "Rent"                 | -1500.0 | "Housing"        |
| "Comcast Internet"     | -75.0   | "Utilities"      |
| "Trader Joe's"         | -82.45  | "Groceries"      |
| "Shell Gas"            | -45.2   | "Transportation" |
| …                      | …       | …                |
| "Geico Auto Insurance" | -125.0  | "Insurance"      |
| "NYTimes Digital"      | -17.0   | "Subscriptions"  |
| "Shell Gas"            | -42.8   | "Transportation" |
| "Costco"               | -156.78 | "Groceries"      |
| "24 Hour Fitness"      | -39.99  | "Subscriptions"  |


Every transaction found a bucket, so nothing fell through to `"Other"`. With a `Category` column in place, the tracking questions from the book become one line of `polars`. The code below totals each category:


``` python
totals = categorized.group_by("Category").agg(pl.col("Amount").sum()).sort("Category")
totals
```


shape: (8, 2)

| Category         | Amount  |
|------------------|---------|
| str              | f64     |
| "Dining"         | -21.25  |
| "Groceries"      | -303.35 |
| "Housing"        | -1500.0 |
| "Income"         | 2400.0  |
| "Insurance"      | -125.0  |
| "Subscriptions"  | -83.97  |
| "Transportation" | -88.0   |
| "Utilities"      | -302.3  |


Subscriptions took \$83.97 in the first half of January. That total is small next to rent, but it repeats every month, which is why the next section looks at it more closely.


## When a transaction doesn't match

New merchants show up every month. The book's rule is "when in doubt, Other." A transaction that matches no pattern lands in `"Other"` until you've seen it often enough to deserve its own rule. The code below runs two new transactions through the same rules:


``` python
new_transactions = pl.DataFrame({
    "Description": ["Venmo Payment", "SPOTIFY FAMILY PLAN"],
})
apply_rules(df=new_transactions, rules=rules)
```


shape: (2, 2)

| Description           | Category        |
|-----------------------|-----------------|
| str                   | str             |
| "Venmo Payment"       | "Other"         |
| "SPOTIFY FAMILY PLAN" | "Subscriptions" |


The Venmo payment falls through to `"Other"`. The Spotify charge still lands in `"Subscriptions"` because [apply_rules()](../reference/apply_rules.md#perfinpy.apply_rules) ignores case, so `"Spotify"` matches `"SPOTIFY"`.


# What does a subscription really cost?

A subscription's real cost is its opportunity cost: the money you give up by spending instead of investing. The book's example is a monthly subscription you don't really use, with the money invested instead at a real return (the return after inflation). The code below stores the book's inputs:


``` python
monthly_cost = 20
years = 30
rate = 0.07
```


Canceling the \$20 a month subscription frees up \$240 a year to invest at 7% for 30 years. The chart below shows what that money grows into at each checkpoint, split into the money you put in and the growth it earned.


<figure class="figure">
<p><img src="assets/tracking-spending-subscription-bar-model.png" class="img-fluid figure-img" alt="Stacked bar chart of $240 a year invested at 7%, with bars at years 1, 5, 10, 20, and 30. Each bar splits into money put in (bluish green, bottom) and growth (vermillion, top). The totals are $240, $1,380, $3,316, $9,839, and $22,671. Growth is a thin sliver at year 5, about equal to the money put in at year 20, and roughly twice the money put in at year 30." /></p>
<figcaption>$240 a year invested at 7% instead of a $20/month subscription</figcaption>
</figure>


Each bar adds another year's deposit to everything saved so far, and the whole pile grows by 7%. [subscription_opportunity_cost()](../reference/subscription_opportunity_cost.md#perfinpy.subscription_opportunity_cost) adds up every year's deposit and its growth in one step:


``` python
sub_cost = subscription_opportunity_cost(
    monthly_cost=monthly_cost,
    years=years,
    rate=rate,
)
sub_cost
```


    22670.58871769843


Over 30 years you put in \$7,200, and growth adds \$15,471 on top of it. That "small" \$20 a month is a \$22,671 decision.


# Comparing horizons

[subscription_opportunity_cost()](../reference/subscription_opportunity_cost.md#perfinpy.subscription_opportunity_cost) accepts arrays, so one call can fill in every bar of the chart above. The code below puts the five checkpoints in a `pl.DataFrame` with the money put in and the growth:


``` python
checkpoints = [1, 5, 10, 20, 30]
horizons = pl.DataFrame({
    "years": checkpoints,
    "put_in": [monthly_cost * 12 * y for y in checkpoints],
    "value": subscription_opportunity_cost(monthly_cost, checkpoints, rate).round(2),
}).with_columns(growth=pl.col("value") - pl.col("put_in"))
horizons
```


shape: (5, 4)

| years | put_in | value    | growth   |
|-------|--------|----------|----------|
| i64   | i64    | f64      | f64      |
| 1     | 240    | 240.0    | 0.0      |
| 5     | 1200   | 1380.18  | 180.18   |
| 10    | 2400   | 3315.95  | 915.95   |
| 20    | 4800   | 9838.92  | 5038.92  |
| 30    | 7200   | 22670.59 | 15470.59 |


Growth is \$180 after 5 years and \$15,471 after 30. Most of the cost of a subscription shows up late, which is exactly when you've stopped noticing the charge.

> **Warning: Limits**
>
> - [apply_rules()](../reference/apply_rules.md#perfinpy.apply_rules): the first matching rule wins, so put specific patterns above general ones. Patterns are regular expressions with case ignored, so characters like `.`, `+`, and `(` have special meanings. The function only reads `Description`; a Netflix refund lands in `"Subscriptions"` just like the charge. An existing `Category` column is replaced. Both arguments must be `polars` DataFrames.
> - [subscription_opportunity_cost()](../reference/subscription_opportunity_cost.md#perfinpy.subscription_opportunity_cost): it invests the yearly total once, at the end of each year, at one fixed rate. The book's \$267,000 figure for \$219 a month assumes monthly deposits, so it comes out higher than this function's result for the same inputs. The 7% default is a real return, so the result is in today's dollars. It does not reject negative costs.


# Putting it together

The book's monthly review ends with a subscription audit: list every recurring charge and decide whether it's worth the cost. The categorized statement already holds that list. The code below pulls the subscription rows and prices each one over the same horizon:


``` python
subs = categorized.filter(pl.col("Category") == "Subscriptions")
monthly = -subs["Amount"]
audit = pl.DataFrame({
    "Description": subs["Description"],
    "monthly": monthly,
    "cost_30": subscription_opportunity_cost(monthly.to_numpy(), years=years).round(2),
})
audit
```


shape: (4, 3)

| Description       | monthly | cost_30  |
|-------------------|---------|----------|
| str               | f64     | f64      |
| "Netflix"         | 15.99   | 18125.14 |
| "Spotify"         | 10.99   | 12457.49 |
| "NYTimes Digital" | 17.0    | 19270.0  |
| "24 Hour Fitness" | 39.99   | 45329.84 |


These 4 subscriptions cost \$83.97 a month, which adds up to \$95,182 over 30 years. To put the monthly total in context, [percent_of_income()](../reference/percent_of_income.md#perfinpy.percent_of_income) from the [Budgeting](budgeting.md) page compares it with the paycheck on the statement:


``` python
paycheck = categorized.filter(pl.col("Category") == "Income")["Amount"][0]
subs_share = percent_of_income(expense=audit["monthly"].sum(), income=paycheck)
subs_share
```


    3.49875


Subscriptions take about 3.5% of the paycheck. As in the rest of perfinpy, the ratio comes out as a percent, not a decimal (see the conventions in [Get started](get-started.md)). The gym membership alone accounts for \$45,330 of the 30 year total. That makes it the first one to check against the book's audit question: have you used it in the last 30 days?


# Recap

[apply_rules()](../reference/apply_rules.md#perfinpy.apply_rules) turns a bank export into categorized spending with a small, stable table of keyword patterns, and anything new falls through to `"Other"`. [subscription_opportunity_cost()](../reference/subscription_opportunity_cost.md#perfinpy.subscription_opportunity_cost) puts a price on recurring charges by showing what the money would grow to if invested. Together they cover the recording side of personal finance, which feeds the allocation decisions in [Budgeting](budgeting.md).

- [Tracking Spending](https://mjfrigaard.github.io/fm-finance/tracking_spending.html) in Personal Finance: a field manual
- Reference: [apply_rules()](../reference/apply_rules.md#perfinpy.apply_rules), [subscription_opportunity_cost()](../reference/subscription_opportunity_cost.md#perfinpy.subscription_opportunity_cost), [percent_of_income()](../reference/percent_of_income.md#perfinpy.percent_of_income)
- Next: [Budgeting](budgeting.md)
