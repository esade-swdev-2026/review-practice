from pathlib import Path

from typer.testing import CliRunner

from expense_tracker.cli import app
from expense_tracker.report import Expense, average_amount

runner = CliRunner()

CSV_TEXT = (
    "date,merchant,category,amount\n"
    "2025-07-01,Bar Ramon,dining,10.00\n"
    "2025-07-02,Zara,clothing,40.00\n"
    "2025-08-01,Cabify,transport,15.00\n"
)


def test_average_is_the_total_divided_by_the_count() -> None:
    expenses = [
        Expense("2025-07-01", "Bar Ramon", "dining", 10.0),
        Expense("2025-07-02", "Zara", "clothing", 40.0),
    ]

    assert average_amount(expenses) == 25.0


def test_report_shows_the_average_expense(tmp_path: Path) -> None:
    csv_file = tmp_path / "expenses.csv"
    csv_file.write_text(CSV_TEXT)

    result = runner.invoke(app, ["report", str(csv_file)])

    assert result.exit_code == 0
    assert "Average expense: 21.67" in result.stdout
