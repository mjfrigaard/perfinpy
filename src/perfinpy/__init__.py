"""Tested versions of the Python functions in Personal Finance: a field manual.

Book: https://mjfrigaard.github.io/fm-finance/
"""

from .asset_allocation import (
    portfolio_return,
    rebalance_amount,
)
from .automating_savings import (
    monthly_savings,
)
from .budgeting import (
    months_to_break_even,
    opportunity_cost,
    percent_of_income,
    to_annual,
    to_monthly,
)
from .emergency_fund import (
    ef_growth,
    emergency_fund_target,
    monthly_contribution_needed,
    months_to_ef_goal,
)
from .estate_planning import (
    beneficiary_share,
    net_worth,
)
from .financial_goals import (
    monthly_for_goal,
    months_to_fund,
)
from .high_yield_accounts import (
    hysa_balance,
)
from .income import (
    fixed_cost_ratio,
    raise_invested_value,
    wealth_formula,
)
from .index_funds import (
    future_value_after_fees,
    yearly_fee,
)
from .insurance import (
    break_even_years,
    plan_cost,
)
from .investing_basics import (
    future_value,
    future_value_series,
    real_return,
    rule_of_72,
)
from .major_purchases import (
    first_payment_split,
    mortgage_payment,
    rent_buy_threshold,
)
from .managing_debt import (
    apr_to_apy,
    credit_utilization,
    dti_ratio,
    idr_monthly_payment,
    loan_income_ratio,
    monthly_standard_payment,
    months_to_payoff,
    order_avalanche,
    order_snowball,
    payoff_vs_invest,
    total_interest,
)
from .retirement_accounts import (
    after_tax_value,
    employer_match,
)
from .savings_strategies import (
    savings_rate,
)
from .taxes import (
    income_tax,
    raise_kept,
)
from .tracking_spending import (
    apply_rules,
    subscription_opportunity_cost,
)

__version__ = "0.1.0"

__all__ = [
    "wealth_formula",
    "fixed_cost_ratio",
    "raise_invested_value",
    "apply_rules",
    "subscription_opportunity_cost",
    "percent_of_income",
    "to_annual",
    "to_monthly",
    "opportunity_cost",
    "months_to_break_even",
    "apr_to_apy",
    "months_to_payoff",
    "total_interest",
    "loan_income_ratio",
    "monthly_standard_payment",
    "idr_monthly_payment",
    "dti_ratio",
    "payoff_vs_invest",
    "order_avalanche",
    "order_snowball",
    "credit_utilization",
    "emergency_fund_target",
    "months_to_ef_goal",
    "monthly_contribution_needed",
    "ef_growth",
    "savings_rate",
    "hysa_balance",
    "monthly_savings",
    "future_value",
    "rule_of_72",
    "future_value_series",
    "real_return",
    "employer_match",
    "after_tax_value",
    "yearly_fee",
    "future_value_after_fees",
    "portfolio_return",
    "rebalance_amount",
    "income_tax",
    "raise_kept",
    "break_even_years",
    "plan_cost",
    "monthly_for_goal",
    "months_to_fund",
    "rent_buy_threshold",
    "mortgage_payment",
    "first_payment_split",
    "net_worth",
    "beneficiary_share",
]
