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
        roundedNumber = (number - (number % 10))
    elif number % 10 > 5:
        roundedNumber = (number + (10 - (number % 10)))
    else:
        roundedNumber = number
    return roundedNumber


def calc_plates(weight: int, availablePlates: list) -> dict:
    """computes the required weight plates to reach supplied weight

    Args:
        weight (int): desired weight
        availablePlates (list): available plates

    Returns:
        dict: number of plates per weight to reach supplied weight
    """
    plates = {}
    remainingWeight = Decimal(round_num(weight)) / Decimal(2)
    for plate in availablePlates:
        if remainingWeight / Decimal(plate) >= Decimal(1):
            plates[plate] = Decimal(remainingWeight) // Decimal(plate)
            remainingWeight -= Decimal(plate) * Decimal(plates[plate])
    return plates