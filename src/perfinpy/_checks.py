"""Internal input checks and shared formulas."""

from __future__ import annotations

from typing import Any, Union

import numpy as np
from numpy.typing import ArrayLike, NDArray

Numeric = Union[float, NDArray[np.float64]]
Whole = Union[int, NDArray[np.int64]]


def _out(x: Any) -> Numeric:
    # numpy 0-d results become plain floats; everything else a float array
    if np.ndim(x) == 0:
        return float(x)
    return np.asarray(x, dtype=float)


def _as_numeric(x: ArrayLike, arg: str) -> Numeric:
    # error unless `x` is a number or an array of numbers with no missing values
    if x is None or isinstance(x, (bool, np.bool_, str, bytes)):
        raise TypeError(f"`{arg}` must be numeric.")
    arr = np.asarray(x)
    if arr.dtype.kind not in "iuf":
        raise TypeError(f"`{arg}` must be numeric.")
    arr = arr.astype(float)
    if np.isnan(arr).any():
        raise ValueError(f"`{arg}` must not contain missing values.")
    return _out(arr)


def _as_positive(x: ArrayLike, arg: str) -> Numeric:
    # error unless every value of `x` is a number greater than 0
    out = _as_numeric(x, arg)
    if np.any(np.asarray(out) <= 0):
        raise ValueError(f"`{arg}` must be greater than 0.")
    return out


def _as_scalar(x: ArrayLike, arg: str) -> float:
    # error unless `x` is a single number
    out = _as_numeric(x, arg)
    if not isinstance(out, float):
        raise ValueError(f"`{arg}` must be a single number.")
    return out


def _annuity_factor(rate: Numeric, periods: Numeric) -> Numeric:
    # future value of 1 paid each period: ((1 + rate)**periods - 1) / rate,
    # with the 0% limit (periods) where rate is 0
    r = np.asarray(rate, dtype=float)
    n = np.asarray(periods, dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        out = ((1 + r) ** n - 1) / r
    return _out(np.where(r == 0, n, out))


def _ceil(x: Numeric) -> Whole:
    # round up; ints for scalars, as math.ceil() gives in the book
    if isinstance(x, float):
        return int(np.ceil(x))
    return np.ceil(x).astype(np.int64)
