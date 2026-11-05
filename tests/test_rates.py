import pytest

from expense_tracker.rates import to_dollars


@pytest.mark.parametrize(
    ("euros", "rate", "dollars"),
    [
        (100.0, 1.08, 108.0),
        (0.0, 1.08, 0.0),
        (19.99, 1.0825, 21.64),
    ],
)
def test_to_dollars_multiplies_by_the_rate_and_rounds_to_cents(
    euros: float, rate: float, dollars: float
) -> None:
    assert to_dollars(euros, rate) == dollars
