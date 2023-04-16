"""which_plates tests"""

import pytest

from which_plates.functions import calc_plates, round_num


def test_round_num_float() -> None:
    """Float input"""
    result = round_num(16.5)
    assert result == 20


def test_round_num_int() -> None:
    """Integer input"""
    result = round_num(16)
    assert result == 20


def test_round_num_string() -> None:
    """String input"""

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        round_num("g")  # type: ignore[arg-type]
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1


def test_calc_plates_int_and_list() -> None:
    """expected input"""
    result = calc_plates(200, [45, 35, 25, 15, 10, 5, 2.5])
    assert isinstance(result, dict)
    assert result == {45: 4, 10: 2}
