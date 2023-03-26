""" helper functions"""

from decimal import Decimal

def round_num(number: float) -> int:
    """rounds input to the nearest multiple of 5, assuming smallest plate is 2.5 pounds

    Args:
        number (float): number to be rounded

    Returns:
        int: rounded number
    """
    if number % 10 < 5:
        rounded_number = number - (number % 10)
    elif number % 10 > 5:
        rounded_number = number + (10 - (number % 10))
    else:
        rounded_number = number
    return int(rounded_number)


def calc_plates(weight: int, available_plates: list) -> dict:
    """computes the required weight plates to reach supplied weight

    Args:
        weight (int): desired weight
        available_plates (list): available plates

    Returns:
        dict: number of plates per weight to reach supplied weight
    """
    plates = {}
    remaining_weight = Decimal(round_num(weight)) / Decimal(2)
    for plate in available_plates:
        if remaining_weight / Decimal(plate) >= Decimal(1):
            plates[plate] = Decimal(remaining_weight) // Decimal(plate)
            remaining_weight -= Decimal(plate) * Decimal(plates[plate])
    return plates
