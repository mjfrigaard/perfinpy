import numpy as np
import polars as pl
import pytest

from perfinpy._checks import _annuity_factor, _as_numeric, _as_positive, _as_scalar


def test_as_numeric_scalars_become_floats():
    assert _as_numeric(5, "x") == 5.0
    assert isinstance(_as_numeric(np.int64(5), "x"), float)


def test_as_numeric_sequences_become_arrays():
    for x in ([1, 2], (1, 2), np.array([1, 2]), pl.Series([1, 2])):
        np.testing.assert_array_equal(_as_numeric(x, "x"), [1.0, 2.0])


@pytest.mark.parametrize("bad", ["5", None, True, [1, "a"], [True, False]])
def test_as_numeric_rejects_non_numbers(bad):
    with pytest.raises(TypeError, match="`x` must be numeric"):
        _as_numeric(bad, "x")


def test_as_numeric_rejects_missing_values():
    with pytest.raises(ValueError, match="`x` must not contain missing values"):
        _as_numeric([1, float("nan")], "x")
    with pytest.raises(ValueError, match="missing values"):
        _as_numeric(pl.Series([1, None]), "x")


def test_as_positive():
    assert _as_positive(1, "x") == 1.0
    with pytest.raises(ValueError, match="`x` must be greater than 0"):
        _as_positive([1, 0], "x")


def test_as_scalar():
    with pytest.raises(ValueError, match="`x` must be a single number"):
        _as_scalar([1, 2], "x")


def test_annuity_factor_zero_rate_limit():
    assert _annuity_factor(0.0, 12.0) == 12.0
    np.testing.assert_allclose(_annuity_factor(np.array([0.0, 0.1]), 2.0), [2.0, 2.1])
