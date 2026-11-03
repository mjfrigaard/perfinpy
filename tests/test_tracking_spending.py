import polars as pl
import pytest

from perfinpy import apply_rules, subscription_opportunity_cost

transactions = pl.DataFrame(
    {"Description": ["SAFEWAY #123", "NETFLIX.COM", "Shell Oil", "ATM FEE"]}
)
rules = pl.DataFrame(
    {
        "Pattern": ["safeway", "netflix", "shell"],
        "Category": ["Groceries", "Subscriptions", "Gas"],
    }
)


def test_apply_rules_ignores_case():
    out = apply_rules(transactions, rules)
    assert out["Category"].to_list() == ["Groceries", "Subscriptions", "Gas", "Other"]


def test_apply_rules_first_match_wins():
    overlap = pl.DataFrame({"Pattern": ["oil", "shell"], "Category": ["Auto", "Gas"]})
    assert apply_rules(transactions, overlap)["Category"][2] == "Auto"


def test_apply_rules_regex_alternation():
    book = pl.DataFrame({"Pattern": ["Netflix|Spotify"], "Category": ["Subs"]})
    out = apply_rules(pl.DataFrame({"Description": ["Spotify USA"]}), book)
    assert out["Category"].to_list() == ["Subs"]


def test_apply_rules_empty_inputs():
    no_rules = rules.clear()
    assert apply_rules(transactions, no_rules)["Category"].to_list() == ["Other"] * 4
    assert apply_rules(transactions.clear(), rules).height == 0


def test_apply_rules_bad_inputs():
    with pytest.raises(ValueError, match="`Description` column"):
        apply_rules(pl.DataFrame({"x": [1]}), rules)
    with pytest.raises(ValueError, match="`Pattern` and `Category`"):
        apply_rules(transactions, pl.DataFrame({"Pattern": ["a"]}))
    with pytest.raises(TypeError, match="polars DataFrame"):
        apply_rules({"Description": ["a"]}, rules)


def test_subscription_opportunity_cost():
    expected = 180 * (1.07**30 - 1) / 0.07
    assert subscription_opportunity_cost(15, 30) == pytest.approx(expected)
    assert subscription_opportunity_cost(15, 10, rate=0) == pytest.approx(1800)
