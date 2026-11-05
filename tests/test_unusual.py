from expense_tracker.report import Expense, format_report

COFFEE = Expense("2025-07-01", "Bar Ramon", "dining", 3.5)
LAPTOP = Expense("2025-07-02", "Fnac", "electronics", 899.0)

WARNING = "That is unusually large: check it is not a mistake."


def test_a_very_large_expense_gets_a_warning() -> None:
    lines = format_report("expenses.csv", "", 0.0, [], LAPTOP)

    assert lines[-1] == WARNING


def test_an_ordinary_expense_gets_no_warning() -> None:
    lines = format_report("expenses.csv", "", 0.0, [], COFFEE)

    assert WARNING not in lines
