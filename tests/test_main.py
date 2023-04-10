"""test main.py"""

import pytest

from which_plates.main import main, main_function


def test_main(monkeypatch) -> None:  # type: ignore[no-untyped-def]
    """test main"""

    # fake inputs
    bar_weight = 45
    total_weight = 245
    percentages = "50 75 95"
    answers = iter([bar_weight, total_weight, percentages])
    monkeypatch.setattr("builtins.input", lambda name: next(answers))

    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.value.code == 0


def test_main_function() -> None:
    """test main_function"""

    bar_weight = 45
    total_weight = 245
    percentages = [0.50, 0.75, 0.95]
    available_plates = [45, 35, 25, 15, 10, 5, 2.5]

    result = main_function(bar_weight, total_weight, available_plates, percentages)
    assert result == 0
