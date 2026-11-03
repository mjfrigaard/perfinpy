# perfinpy

`perfinpy` holds the Python functions from [Personal Finance: a field manual](https://mjfrigaard.github.io/fm-finance/). Each chapter of the book builds its calculations from scratch so you can see how the formula works. This package collects those same functions, documents them, and tests them, so you can use them without copying code out of the book. It is the Python counterpart to the R package [perfinr](https://mjfrigaard.github.io/perfinr/).

## Installation

`perfinpy` isn't on PyPI. Install the development version from GitHub:

```bash
uv pip install git+https://github.com/mjfrigaard/perfinpy
```

`perfinpy` depends on `numpy` and `polars`.

## Example

The functions keep the book's names, arguments, and defaults, so code from a chapter runs unchanged:

```python
from perfinpy import future_value, mortgage_payment, percent_of_income

# rent of $1,500 on a $5,000 monthly income
percent_of_income(expense=1500, income=5000)
#> 30.0

# $10,000 at 7% over four horizons
future_value(present_value=10000, rate=0.07, years=[5, 10, 20, 30])
#> array([14025.517307  , 19671.5135729 , 38696.84462486, 76122.55042662])

# a $480,000 mortgage at 6% over 30 years
mortgage_payment(principal=480000, annual_rate=0.06, years=30)
#> 2877.842520733233
```

Rates go in as decimals (`0.07` is 7%), ratio functions return percents (`30` is 30%), and most functions accept arrays so you can compare options in one call. The user guide has one page for each chapter of the book.

## Development

```bash
uv venv
uv pip install -e ".[dev]"
uv run pytest
uv run great-docs build
```
