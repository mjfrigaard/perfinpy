"""Functions from the Estate Planning chapter."""

from __future__ import annotations

from collections.abc import Mapping

import numpy as np
from numpy.typing import ArrayLike

from ._checks import _as_numeric


def _total(x: Mapping[str, float] | ArrayLike, arg: str) -> float:
    values = list(x.values()) if isinstance(x, Mapping) else x
    return float(np.sum(_as_numeric(values, arg)))


def net_worth(
    assets: Mapping[str, float] | ArrayLike, debts: Mapping[str, float] | ArrayLike
) -> float:
    """Net worth: total assets minus total debts.

    From the [Estate Planning](https://mjfrigaard.github.io/fm-finance/estate_planning.html)
    chapter.

    Parameters
    ----------
    assets
        Asset values, as a dict of name to amount or a sequence of amounts.
    debts
        Debt balances, as a dict of name to amount or a sequence of amounts.

    Returns
    -------
    float
        Net worth.

    Raises
    ------
    TypeError
        If a value is not numeric.
    ValueError
        If a value is missing.

    Examples
    --------
    >>> from perfinpy import net_worth
    >>> assets = {"401k": 12000, "roth_ira": 6000, "savings": 8000, "car": 9000}
    >>> debts = {"car_loan": 6000, "credit_card": 1000}
    >>> net_worth(assets, debts)
    28000.0
    """
    return _total(assets, "assets") - _total(debts, "debts")


def beneficiary_share(
    with_beneficiary: Mapping[str, float] | ArrayLike,
    without_beneficiary: Mapping[str, float] | ArrayLike,
) -> float:
    """Share of assets that pass directly to a named beneficiary.

    Assets with a beneficiary (retirement accounts, life insurance, payable
    on death accounts) skip probate. From the
    [Estate Planning](https://mjfrigaard.github.io/fm-finance/estate_planning.html)
    chapter.

    Parameters
    ----------
    with_beneficiary
        Values of assets with a named beneficiary, as a dict or a sequence.
    without_beneficiary
        Values of assets without one, as a dict or a sequence.

    Returns
    -------
    float
        Share, as a decimal (`0.8875` is 88.75%).

    Raises
    ------
    TypeError
        If a value is not numeric.
    ValueError
        If a value is missing, or total assets are not greater than 0.

    Examples
    --------
    >>> from perfinpy import beneficiary_share
    >>> with_beneficiary = {"401k": 12000, "roth_ira": 6000,
    ...                     "life_insurance": 45000, "savings_pod": 8000}
    >>> beneficiary_share(with_beneficiary, {"car": 9000})
    0.8875
    """
    named = _total(with_beneficiary, "with_beneficiary")
    total = named + _total(without_beneficiary, "without_beneficiary")
    if total <= 0:
        raise ValueError("Total assets must be greater than 0.")
    return named / total
