from pathlib import Path

from expense_tracker.report import Expense, total_by_category

EXPENSES = [
    Expense("2025-07-01", "Bar Ramon", "dining", 10.0),
    Expense("2025-07-02", "Zara", "clothing", 40.0),
]


def test_totals_are_saved_one_category_per_line(tmp_path: Path) -> None:
    saved = tmp_path / "totals.csv"

    total_by_category(EXPENSES, category="", minimum=0.0, save_to=str(saved))

    assert saved.read_text().splitlines() == ["clothing,40.00", "dining,10.00"]
