# Managing Debt

Lenders quote whichever number makes a loan look cheapest, and they count on borrowers not running the math. The book's [Managing Debt](https://mjfrigaard.github.io/fm-finance/managing_debt.html) chapter runs that math. It asks what a balance really costs, how much student debt a salary can carry, which ratios lenders check, and which debt to pay first. In this page I'll answer the same questions with perfinpy's 11 managing debt functions. Each example uses the chapter's numbers, so you can check every result against the book.


# The managing debt functions

The functions follow the conventions in [Get started](get-started.md): rates go in as decimals and ratios come out as percents. The one exception to watch is [loan_income_ratio()](../reference/loan_income_ratio.md#perfinpy.loan_income_ratio), which returns a plain ratio rather than a percent.

| Function | Returns | Units |
|----|----|----|
| [apr_to_apy()](../reference/apr_to_apy.md#perfinpy.apr_to_apy) | the effective yearly rate of an APR | decimal (`0.27` is 27%) |
| [months_to_payoff()](../reference/months_to_payoff.md#perfinpy.months_to_payoff) | months to clear a balance with a fixed payment | months, not rounded |
| [total_interest()](../reference/total_interest.md#perfinpy.total_interest) | all payments minus the amount borrowed | dollars |
| [loan_income_ratio()](../reference/loan_income_ratio.md#perfinpy.loan_income_ratio) | student loans relative to starting salary | ratio (`1` is one year of salary) |
| [monthly_standard_payment()](../reference/monthly_standard_payment.md#perfinpy.monthly_standard_payment) | payment on a standard student loan plan | dollars per month |
| [idr_monthly_payment()](../reference/idr_monthly_payment.md#perfinpy.idr_monthly_payment) | payment on an income driven repayment plan | dollars per month, rounded to cents |
| [dti_ratio()](../reference/dti_ratio.md#perfinpy.dti_ratio) | debt payments as a share of gross income | percent (`28` is 28%) |
| [payoff_vs_invest()](../reference/payoff_vs_invest.md#perfinpy.payoff_vs_invest) | whether to pay off a loan or invest | a single string |
| [order_avalanche()](../reference/order_avalanche.md#perfinpy.order_avalanche) | debts sorted by APR, highest first | a list of dicts |
| [order_snowball()](../reference/order_snowball.md#perfinpy.order_snowball) | debts sorted by balance, smallest first | a list of dicts |
| [credit_utilization()](../reference/credit_utilization.md#perfinpy.credit_utilization) | a card balance as a share of the limit | percent (`30` is 30%) |


# What does a balance really cost?

Every debt has a price, called the APR (annual percentage rate): the yearly cost of borrowing, shown as a percent of what you owe. The APR is only the starting point. Compounding, slow payments, and long terms all add to what you pay, and the three functions in this section measure each one.


## APR vs. APY

The chapter's example is a credit card with a 24% APR that compounds daily, carrying a \$5,000 balance. Credit card companies quote the APR, but compounding (charging interest on interest you haven't paid yet) means the balance grows faster than the APR suggests.

Both bars below represent one year of interest on the same balance. The shorter bar is what the APR implies; the taller bar is what you actually owe:


<figure class="figure">
<p><img src="assets/managing-debt-apr-apy-bar-model.png" class="img-fluid figure-img" alt="Bar chart of one year of interest on a $5,000 balance. The bluish green APR cost bar, labeled stated, reaches $1,200. The vermillion APY cost bar, labeled actual, reaches $1,356, and a double headed arrow at its top marks the $156 difference as hidden cost." /></p>
<figcaption>APR cost vs. APY cost on a $5,000 balance (24% APR, daily compounding)</figcaption>
</figure>


The APY (annual percentage yield) is the effective yearly rate once compounding is included. [apr_to_apy()](../reference/apr_to_apy.md#perfinpy.apr_to_apy) converts one to the other, with `periods_per_year` defaulting to 365 for daily compounding:


``` python
apy = apr_to_apy(apr=0.24)
apy
```


    0.27114889144128895


A 24% APR compounded daily is really 27.1% a year. On the \$5,000 balance, that gap is about \$156 of interest the quoted rate never mentions.


## How long does a minimum payment take?

The chapter's next example is a \$5,000 balance at 22% APR with a \$100 minimum payment. A \$100 payment sounds reasonable until you see how little of it reaches the balance. The principal is the amount you borrowed; interest is what the lender charges on top.


<figure class="figure">
<p><img src="assets/managing-debt-min-payment-bar-model.png" class="img-fluid figure-img" alt="Bar chart splitting a $100 payment into two bars. A tall vermillion bar shows $92 going to interest, and a short blue bar shows $8 going to principal reduction." /></p>
<figcaption>Where a $100 minimum payment actually goes</figcaption>
</figure>


Only the principal slice shrinks the debt. As the balance falls, the interest slice shrinks too, so each payment retires a little more principal than the one before. [months_to_payoff()](../reference/months_to_payoff.md#perfinpy.months_to_payoff) accounts for that, compounding interest monthly at `apr / 12`:


``` python
first_interest = 5000 * 0.22 / 12
card_months = months_to_payoff(balance=5000, monthly_payment=100, apr=0.22)
first_interest, card_months
```


    (91.66666666666667, 136.77905405676316)


The first month's interest is about \$92, so only \$8 of the first payment touches the balance. Paying the minimum clears the card in about 137 months (11.4 years), and the payments add up to about \$13,678 on a \$5,000 balance. Minimum payments are designed to keep you in debt for years.


## What does the loan term cost?

An installment loan is one you repay in equal monthly payments, like a car loan or a mortgage. For these loans, total interest is the number that should drive the decision. The chapter's example is a \$20,000 used car loan at 7%. It runs either 6 years at \$340.98 a month or 4 years at \$478.92 a month.

The amount borrowed is the same either way. The bars below stack the principal and interest layers, so the cost of the longer term is visible:


<figure class="figure">
<p><img src="assets/managing-debt-total-interest-bar-model.png" class="img-fluid figure-img" alt="Two stacked bars of total paid on a $20,000 car loan. The 6-year loan stacks a $4,551 vermillion interest layer on a $20,000 bluish green principal layer. The 4-year loan stacks a thinner $2,988 interest layer on the same $20,000 of principal." /></p>
<figcaption>$20,000 car loan at 7%: principal vs. interest for 6 year and 4 year terms</figcaption>
</figure>


Subtract the principal from everything you pay and the interest layer is what's left. [total_interest()](../reference/total_interest.md#perfinpy.total_interest) accepts arrays, so both terms fit in one call:


``` python
car_interest = total_interest(
    monthly_payment=[340.98, 478.92],
    n_months=[72, 48],
    principal=20000,
)
car_interest
```


    array([4550.56, 2988.16])


The 6 year loan costs \$4,550.56 in interest, and the 4 year loan costs \$2,988.16. Shortening the term saves \$1,562.40, which is the math behind the 20/4/10 car rule (20% down, no more than 4 years, transportation under 10% of gross income).


# How much student debt can a salary carry?

Student loans sit in a complicated middle ground. Education is an investment in your future earning potential, but only when the math works. The chapter gives two tools for checking it: the 1x rule before you borrow, and income driven repayment after.


## The 1x rule

The 1x rule says total student debt at graduation should not exceed your expected first year salary. The chapter's example borrower has \$45,000 in loans and a \$42,000 starting salary, repaying on a standard 10 year plan at 6.5%.

Picture what you borrowed and what your first job pays as two bars side by side. The rule says the loan bar shouldn't run past the salary bar:


<figure class="figure">
<p><img src="assets/managing-debt-loan-income-bar-model.png" class="img-fluid figure-img" alt="Two horizontal bars. The vermillion student loans bar is $45,000 and the bluish green starting salary bar is $42,000. A dashed vertical line at $42,000 marks the end of the salary bar, and the loan bar runs a little past it." /></p>
<figcaption>$45,000 in student loans vs. a $42,000 starting salary</figcaption>
</figure>


[loan_income_ratio()](../reference/loan_income_ratio.md#perfinpy.loan_income_ratio) divides the loan bar by the salary bar. [monthly_standard_payment()](../reference/monthly_standard_payment.md#perfinpy.monthly_standard_payment) then spreads the loan, plus interest, over 120 equal payments, with the 6.5% rate and 10 year term as defaults:


``` python
ratio = loan_income_ratio(loan_total=45000, expected_salary=42000)
student_payment = monthly_standard_payment(principal=45000)
ratio, student_payment
```


    (1.0714285714285714, 510.9658974901199)


The ratio is 1.07, so this borrower is a little over the 1x rule. The standard payment is about \$511 a month, or roughly \$0.0114 a month for every dollar borrowed. The 1x rule is a ceiling, not a target; lower earning majors often need a lower personal cap.


## Income driven repayment

When the 1x rule is out of reach, federal income driven repayment (IDR) plans cap payments as a share of discretionary income. Discretionary income is your AGI (adjusted gross income, from your tax return) minus a protected multiple of the Federal Poverty Guideline. The chapter's example is a \$50,000 AGI under IBR. IBR protects 1.5 times the 2026 guideline (\$15,960) and charges 10% on whatever is left.

Think of the AGI as one bar. The plan protects the first part of it, and the payment is a small slice of what's left:


<figure class="figure">
<p><img src="assets/managing-debt-idr-bar-model.png" class="img-fluid figure-img" alt="A single horizontal bar for $50,000 of AGI, split into three segments. A light bluish green segment of $23,940 is protected income (1.5 times $15,960). A narrow vermillion segment of $2,606 a year is the payment (10% of discretionary income). A bluish green segment of $23,454 is the rest of discretionary income." /></p>
<figcaption>$50,000 AGI under IBR: protected income, discretionary income, and the yearly payment</figcaption>
</figure>


[idr_monthly_payment()](../reference/idr_monthly_payment.md#perfinpy.idr_monthly_payment) subtracts the protected part, takes the payment rate of what's left, and divides by 12. The defaults are the IBR terms for loans from July 2014 on; older IBR loans use a 15% rate:


``` python
ibr = idr_monthly_payment(agi=50000)
ibr_old = idr_monthly_payment(agi=50000, payment_rate=0.15)
ibr, ibr_old
```


    (217.17, 325.75)


IBR comes to \$217.17 a month, and \$325.75 for loans made before July 2014. IDR plans change with Congress, the courts, and the Department of Education, so check current terms at [studentaid.gov](https://studentaid.gov/manage-loans/repayment/plans) before enrolling.


# What ratios do lenders check?

Lenders don't just look at what you owe; they look at how much of your income and credit is already spoken for. These two ratios are what lenders calculate about you, so it pays to calculate them about yourself first.


## Debt to income ratio

The chapter pictures a first job paying \$45,000 a year, or \$3,750 a month in gross income. Its debts are a \$511 student loan payment, a \$450 car payment, and \$100 in credit card minimums. Gross income is your pay before taxes, and the bar below splits it into what goes to debt and what's left:


<figure class="figure">
<p><img src="assets/managing-debt-dti-bar-model.png" class="img-fluid figure-img" alt="A horizontal bar for $3,750 of gross monthly income. A vermillion segment of $1,061 (28%) is debt payments, and a bluish green segment of $2,689 (72%) is remaining income. A dashed line marks the 43% danger zone, to the right of where the debt segment ends." /></p>
<figcaption>$3,750 gross monthly income split into debt payments and remaining income</figcaption>
</figure>


DTI (debt to income) is just the debt slice as a share of the whole bar. [dti_ratio()](../reference/dti_ratio.md#perfinpy.dti_ratio) returns it as a percent:


``` python
debt_payments = {"student_loan": 511, "car": 450, "cards": 100}
dti = dti_ratio(
    monthly_debt_payments=sum(debt_payments.values()),
    gross_monthly_income=45000 / 12,
)
dti
```


    28.293333333333333


The \$1,061 in monthly debt payments take about 28% of gross income. The chapter calls 20% to 35% manageable but worth watching; above 43%, most mortgage lenders won't approve you.


## Credit utilization

Credit utilization is how much of your available credit you're using. Credit scores penalize high utilization because using most of your available credit is a sign of money trouble. The chapter's example is a \$900 balance on a first card with a \$3,000 limit:


<figure class="figure">
<p><img src="assets/managing-debt-utilization-bar-model.png" class="img-fluid figure-img" alt="A horizontal bar for a $3,000 credit limit. A vermillion segment of $900 (30%) is the used balance, and a light bluish green segment of $2,100 (70%) is unused credit. A blue dashed line marks the 10% ideal at $300, and a vermillion dashed line marks the 30% threshold, exactly where the used balance ends." /></p>
<figcaption>$900 balance against a $3,000 credit limit: used vs. unused</figcaption>
</figure>


[credit_utilization()](../reference/credit_utilization.md#perfinpy.credit_utilization) divides the used slice by the whole limit and returns a percent:


``` python
utilization = credit_utilization(balance=900, credit_limit=3000)
utilization
```


    30.0


The card sits at 30% utilization, right at the threshold. Keep utilization under 30% on each card and across all cards; under 10% (a \$300 balance on this card) is ideal.


# Which debt should you pay first?

Not all debt is created equal. Attack it in order of damage potential. This section covers two versions of that decision. The first is whether extra money should go to a loan or to investments; the second is which of several debts to attack first.


## Pay off or invest?

The chapter compares a 5% student loan against an expected 7% stock market return. The math slightly favors investing, but the bar model adds what the math alone misses:


<figure class="figure">
<p><img src="assets/managing-debt-payoff-invest-bar-model.png" class="img-fluid figure-img" alt="Two bars of annual return. The blue pay off debt bar reaches 5% and is labeled certain. The taller bluish green invest bar reaches 7% and is labeled expected, not guaranteed." /></p>
<figcaption>Guaranteed 5% debt payoff vs. expected 7% investment return</figcaption>
</figure>


[payoff_vs_invest()](../reference/payoff_vs_invest.md#perfinpy.payoff_vs_invest) compares the two rates (as decimals) and returns the option that wins on paper:


``` python
loan_rate = 0.05
expected_return = 0.07
payoff_vs_invest(loan_rate=loan_rate, expected_return=expected_return)
```


    'Invest the difference'


Investing wins by about 2.0 percentage points a year. But the return from paying off the loan is guaranteed, and the investment return is not. A guaranteed 5% beats a probable 7% for many people psychologically, so run the math, then add your peace of mind premium.


## Avalanche vs. snowball

The chapter's example has three credit cards: Card A (\$1,000 at 18%), Card B (\$5,000 at 24%), and Card C (\$2,000 at 15%). The avalanche method pays the highest APR first; the snowball method pays the smallest balance first. Both attack the same three debts, just in a different order:


<figure class="figure">
<p><img src="assets/managing-debt-avalanche-snowball-bar-model.png" class="img-fluid figure-img" alt="Two panels of bars showing the attack order for three cards. The avalanche panel goes Card B ($5,000 at 24%) first, Card A ($1,000 at 18%) second, and Card C ($2,000 at 15%) third. The snowball panel goes Card A first, Card C second, and Card B third." /></p>
<figcaption>Avalanche order (highest APR first) vs. snowball order (smallest balance first)</figcaption>
</figure>


Both functions take a list of debts (one dict per debt) and return a new, sorted list. [order_avalanche()](../reference/order_avalanche.md#perfinpy.order_avalanche) needs an `apr` key, and [order_snowball()](../reference/order_snowball.md#perfinpy.order_snowball) needs a `balance` key. Wrapping the result in `pl.DataFrame()` prints it as a table:


``` python
debts = [
    {"name": "Card A", "balance": 1000, "apr": 0.18},
    {"name": "Card B", "balance": 5000, "apr": 0.24},
    {"name": "Card C", "balance": 2000, "apr": 0.15},
]
pl.DataFrame(order_avalanche(debts))
```


shape: (3, 3)

| name     | balance | apr  |
|----------|---------|------|
| str      | i64     | f64  |
| "Card B" | 5000    | 0.24 |
| "Card A" | 1000    | 0.18 |
| "Card C" | 2000    | 0.15 |


``` python
pl.DataFrame(order_snowball(debts))
```


shape: (3, 3)

| name     | balance | apr  |
|----------|---------|------|
| str      | i64     | f64  |
| "Card A" | 1000    | 0.18 |
| "Card C" | 2000    | 0.15 |
| "Card B" | 5000    | 0.24 |


Avalanche wins on paper because a dollar sent to the highest APR stops the most interest. The code below shows how much interest an extra \$100 stops next month on each card:


``` python
extra_saved = {d["name"]: 100 * d["apr"] / 12 for d in debts}
extra_saved
```


    {'Card A': 1.5, 'Card B': 2.0, 'Card C': 1.25}


An extra \$100 on Card B stops \$2.00 of interest, compared with \$1.50 on Card A. Snowball pays off Card A first, which costs a little more but delivers a win sooner. If that quick win is the price of actually finishing, it's often worth it; if you're disciplined enough for avalanche, take the savings.


# Variations

Most of these functions accept arrays, so one call can compare several versions of the same decision. Raising the credit card payment from the minimum shows how fast the payoff time and the interest fall:


``` python
import math

card_payment = [100, 150, 200, 300]
card_payoff = months_to_payoff(balance=5000, monthly_payment=card_payment, apr=0.22)
card_cost = total_interest(
    monthly_payment=card_payment, n_months=card_payoff, principal=5000
)
pl.DataFrame({"payment": card_payment, "months": card_payoff, "interest": card_cost})
```


shape: (4, 3)

| payment | months     | interest    |
|---------|------------|-------------|
| i64     | f64        | f64         |
| 100     | 136.779054 | 8677.905406 |
| 150     | 51.986889  | 2798.033306 |
| 200     | 33.747686  | 1749.537239 |
| 300     | 20.071394  | 1021.418167 |


Doubling the payment from \$100 to \$200 cuts the interest from about \$8,678 to about \$1,750, and the card is gone in 34 months instead of 137.

The car loan payments in the total interest example come from the same amortization formula that [monthly_standard_payment()](../reference/monthly_standard_payment.md#perfinpy.monthly_standard_payment) uses. Changing the rate to 7% and passing several terms reproduces them, along with the interest for each term:


``` python
car_years = [3, 4, 5, 6]
car_payment = monthly_standard_payment(
    principal=20000, annual_rate=0.07, years=car_years
)
pl.DataFrame({
    "years": car_years,
    "payment": car_payment,
    "interest": total_interest(
        monthly_payment=car_payment,
        n_months=[y * 12 for y in car_years],
        principal=20000,
    ),
})
```


shape: (4, 3)

| years | payment    | interest    |
|-------|------------|-------------|
| i64   | f64        | f64         |
| 3     | 617.541937 | 2231.509743 |
| 4     | 478.924893 | 2988.394876 |
| 5     | 396.023971 | 3761.438248 |
| 6     | 340.980129 | 4550.56932  |


The IDR plans differ only in the protected multiple and the payment rate, so [idr_monthly_payment()](../reference/idr_monthly_payment.md#perfinpy.idr_monthly_payment) can compare them for the same \$50,000 AGI. SAVE protected 225% of the guideline and charged 5% on undergraduate loans before it ended in March 2026:


``` python
idr_plans = pl.DataFrame({
    "plan": [
        "IBR (loans from July 2014)",
        "IBR (loans before July 2014)",
        "SAVE (ended 2026)",
    ],
    "threshold_pct": [1.5, 1.5, 2.25],
    "payment_rate": [0.10, 0.15, 0.05],
})
idr_plans.with_columns(
    monthly=idr_monthly_payment(
        agi=50000,
        threshold_pct=idr_plans["threshold_pct"].to_numpy(),
        payment_rate=idr_plans["payment_rate"].to_numpy(),
    )
)
```


shape: (3, 4)

| plan                           | threshold_pct | payment_rate | monthly |
|--------------------------------|---------------|--------------|---------|
| str                            | f64           | f64          | f64     |
| "IBR (loans from July 2014)"   | 1.5           | 0.1          | 217.17  |
| "IBR (loans before July 2014)" | 1.5           | 0.15         | 325.75  |
| "SAVE (ended 2026)"            | 2.25          | 0.05         | 58.71   |


# What these functions don't model

> **Warning: Limits**
>
> [months_to_payoff()](../reference/months_to_payoff.md#perfinpy.months_to_payoff) raises a `ValueError` when the payment doesn't cover the first month's interest, because the balance would never be paid off. A \$90 payment on the \$5,000 card at 22% falls short of the first month's interest:
>
> <div id="payoff-error" class="cell" execution_count="16">
>
> ``` python
> months_to_payoff(balance=5000, monthly_payment=90, apr=0.22)
> ```
>
> <div class="cell-output cell-output-error">
>
> <div class="ansi-escaped-output">
>
>     ---------------------------------------------------------------------------
>     ValueError                                Traceback (most recent call last)
>     Cell In[16], line 1
>     ----> 1 months_to_payoff(balance=5000, monthly_payment=90, apr=0.22)
>
>     File ~/projects/pkgs/Python/perfinpy/src/perfinpy/managing_debt.py:98, in months_to_payoff(balance, monthly_payment, apr)
>          96 apr = _as_numeric(apr, "apr")
>          97 if np.any(np.asarray(monthly_payment <= balance * apr / 12)):
>     ---> 98     raise ValueError(
>          99         "`monthly_payment` must be larger than the monthly interest "
>         100         "(`balance * apr / 12`)."
>         101     )
>         102 r = np.asarray(apr / 12)
>         103 ratio = np.asarray(balance / monthly_payment)
>
>     ValueError: `monthly_payment` must be larger than the monthly interest (`balance * apr / 12`).
>
> <div id="putting-it-together" class="section level1">
>
> # Putting it together
>
> Picture a first job paying \$45,000 a year, with \$45,000 in federal student loans, a car loan, and one credit card. The first question is whether the loans fit the 1x rule, and what repaying them costs on the standard plan versus IBR:
>
> <div id="cell-together-loans" class="cell" execution_count="17">
>
> ``` python
> salary = 45000
> standard = monthly_standard_payment(principal=45000)
> {
>     "ratio": loan_income_ratio(loan_total=45000, expected_salary=salary),
>     "standard": standard,
>     "ibr": idr_monthly_payment(agi=salary),
> }
> ```
>
> <div id="together-loans" class="cell-output cell-output-display" execution_count="17">
>
>     {'ratio': 1.0, 'standard': 510.9658974901199, 'ibr': 175.5}
>
> </div>
>
> </div>
>
> The loans sit exactly at the 1x ceiling, so the standard plan is affordable. Next, we can add the car loan (\$15,000 at 7%, \$450 a month) and the card (\$900 at 22%, \$100 a month, \$3,000 limit). Then we check the two ratios lenders use:
>
> <div id="cell-together-ratios" class="cell" execution_count="18">
>
> ``` python
> first_job = [
>     {"name": "Student loan", "balance": 45000, "apr": 0.065, "payment": standard},
>     {"name": "Car loan", "balance": 15000, "apr": 0.07, "payment": 450},
>     {"name": "Credit card", "balance": 900, "apr": 0.22, "payment": 100},
> ]
> first_job_dti = dti_ratio(
>     monthly_debt_payments=sum(d["payment"] for d in first_job),
>     gross_monthly_income=salary / 12,
> )
> first_job_util = credit_utilization(balance=900, credit_limit=3000)
> {"dti": first_job_dti, "utilization": first_job_util}
> ```
>
> <div id="together-ratios" class="cell-output cell-output-display" execution_count="18">
>
>     {'dti': 28.292423933069866, 'utilization': 30.0}
>
> </div>
>
> </div>
>
> DTI is about 28%, in the manageable range, but the card sits at the 30% utilization threshold. Both ordering methods point at the same debt first:
>
> <div id="cell-together-avalanche" class="cell" execution_count="19">
>
> ``` python
> pl.DataFrame(order_avalanche(first_job))
> ```
>
> <div id="together-avalanche" class="cell-output cell-output-display" execution_count="19">
>
> <div>
>
> shape: (3, 4)
>
> | name           | balance | apr   | payment    |
> |----------------|---------|-------|------------|
> | str            | i64     | f64   | f64        |
> | "Credit card"  | 900     | 0.22  | 100.0      |
> | "Car loan"     | 15000   | 0.07  | 450.0      |
> | "Student loan" | 45000   | 0.065 | 510.965897 |
>
> </div>
>
> </div>
>
> </div>
>
> <div id="cell-together-snowball" class="cell" execution_count="20">
>
> ``` python
> pl.DataFrame(order_snowball(first_job))
> ```
>
> <div id="together-snowball" class="cell-output cell-output-display" execution_count="20">
>
> <div>
>
> shape: (3, 4)
>
> | name           | balance | apr   | payment    |
> |----------------|---------|-------|------------|
> | str            | i64     | f64   | f64        |
> | "Credit card"  | 900     | 0.22  | 100.0      |
> | "Car loan"     | 15000   | 0.07  | 450.0      |
> | "Student loan" | 45000   | 0.065 | 510.965897 |
>
> </div>
>
> </div>
>
> </div>
>
> The card has both the highest APR and the smallest balance, so avalanche and snowball agree. The last step checks how long the card takes at \$100 a month. It also checks whether extra money should go to each debt or to investments expected to return 7%:
>
> <div id="cell-together-decide" class="cell" execution_count="21">
>
> ``` python
> card_first_job = months_to_payoff(balance=900, monthly_payment=100, apr=0.22)
> (
>     card_first_job,
>     payoff_vs_invest(loan_rate=0.22, expected_return=0.07),
>     payoff_vs_invest(loan_rate=0.065, expected_return=0.07),
> )
> ```
>
> <div id="together-decide" class="cell-output cell-output-display" execution_count="21">
>
>     (9.92571900450847, 'Pay off the debt', 'Invest the difference')
>
> </div>
>
> </div>
>
> The card is gone in 10 months. After that, its \$100 can roll into the car loan. The student loan comparison is closer than the function's answer suggests. The edge is only 0.5 percentage points, and the chapter treats loans above about 6% as worth paying down. The book's [Budgeting](https://mjfrigaard.github.io/fm-finance/budgeting.html#sec-foo-intro) chapter places these steps in the Financial Order of Operations. The [Emergency Fund](emergency-fund.md) page covers the reserve that comes after high interest debt.
>
> <div id="how-monthly_standard_payment-works" class="section level1">
>
> # How [monthly_standard_payment()](../reference/monthly_standard_payment.md#perfinpy.monthly_standard_payment) works
>
> [monthly_standard_payment()](../reference/monthly_standard_payment.md#perfinpy.monthly_standard_payment) doesn't repeat the amortization formula. It passes its arguments to [mortgage_payment()](../reference/mortgage_payment.md#perfinpy.mortgage_payment) (from the [Major Purchases](major-purchases.md) page), which checks its inputs and calls an internal helper, `_annuity_factor()`:
>
> <div id="call-stack" class="cell" execution_count="22">
>
> ``` python
> from rich import print
> from rich.tree import Tree
>
> tree = Tree("monthly_standard_payment()")
> mortgage = tree.add("mortgage_payment()")
> mortgage.add("_as_numeric()")
> mortgage.add("_as_numeric()")
> mortgage.add("_as_positive()").add("_as_numeric()")
> mortgage.add("_annuity_factor()")
> print(tree)
> ```
>
> </div>
>
>     monthly_standard_payment()
>     └── mortgage_payment()
>         ├── _as_numeric()
>         ├── _as_numeric()
>         ├── _as_positive()
>         │   └── _as_numeric()
>         └── _annuity_factor()
>
> `_annuity_factor()` is where the 0% case lives. Instead of dividing by zero, it returns the number of payments, so a 0% loan is just the principal split into equal pieces:
>
> <div id="cell-zero-rate" class="cell" execution_count="23">
>
> ``` python
> monthly_standard_payment(principal=12000, annual_rate=0)
> ```
>
> <div id="zero-rate" class="cell-output cell-output-display" execution_count="22">
>
>     100.0
>
> </div>
>
> </div>
>
> <div id="recap" class="section level1">
>
> # Recap
>
> Debt is a math problem dressed up in emotional clothing, and these 11 functions cover the math the chapter relies on. [apr_to_apy()](../reference/apr_to_apy.md#perfinpy.apr_to_apy), [months_to_payoff()](../reference/months_to_payoff.md#perfinpy.months_to_payoff), and [total_interest()](../reference/total_interest.md#perfinpy.total_interest) show what a balance really costs; [loan_income_ratio()](../reference/loan_income_ratio.md#perfinpy.loan_income_ratio), [monthly_standard_payment()](../reference/monthly_standard_payment.md#perfinpy.monthly_standard_payment), and [idr_monthly_payment()](../reference/idr_monthly_payment.md#perfinpy.idr_monthly_payment) size student loans against a salary. [dti_ratio()](../reference/dti_ratio.md#perfinpy.dti_ratio) and [credit_utilization()](../reference/credit_utilization.md#perfinpy.credit_utilization) return the percents lenders check, and [payoff_vs_invest()](../reference/payoff_vs_invest.md#perfinpy.payoff_vs_invest), [order_avalanche()](../reference/order_avalanche.md#perfinpy.order_avalanche), and [order_snowball()](../reference/order_snowball.md#perfinpy.order_snowball) decide where the next dollar goes.
>
> - [Managing Debt](https://mjfrigaard.github.io/fm-finance/managing_debt.html) in Personal Finance: a field manual
> - Reference: [apr_to_apy()](../reference/apr_to_apy.md#perfinpy.apr_to_apy), [months_to_payoff()](../reference/months_to_payoff.md#perfinpy.months_to_payoff), [total_interest()](../reference/total_interest.md#perfinpy.total_interest), [loan_income_ratio()](../reference/loan_income_ratio.md#perfinpy.loan_income_ratio), [monthly_standard_payment()](../reference/monthly_standard_payment.md#perfinpy.monthly_standard_payment), [idr_monthly_payment()](../reference/idr_monthly_payment.md#perfinpy.idr_monthly_payment), [dti_ratio()](../reference/dti_ratio.md#perfinpy.dti_ratio), [payoff_vs_invest()](../reference/payoff_vs_invest.md#perfinpy.payoff_vs_invest), [order_avalanche()](../reference/order_avalanche.md#perfinpy.order_avalanche), [order_snowball()](../reference/order_snowball.md#perfinpy.order_snowball), [credit_utilization()](../reference/credit_utilization.md#perfinpy.credit_utilization)
> - Next: [Emergency Fund](emergency-fund.md)
>
> </div>
>
> </div>
>
> </div>
>
> </div>
>
> </div>
>
> </div>
