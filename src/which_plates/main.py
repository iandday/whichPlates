""" main function for which_plates"""

import sys
from . import functions


def main_function(bar_weight, rep_max, available_plates, percentages):
    """main function
    """

    set_count = 1
    used_plates = {}

    for plates in available_plates:
        used_plates[plates] = 0

    for percent in percentages:

        # calculate plate weight needed for current percentage
        plate_weight = functions.round_num((rep_max * percent) - bar_weight)

        if plate_weight <= 0:
            print('    Computed weight less than bar weight, try again')
        else:
            total_weight = round(plate_weight + bar_weight)
            weight = round(plate_weight)
            print(F"Set {set_count} @ {percent * 100}%: {total_weight}lbs, {weight}lbs in plates")  # noqa: E501

        plates = functions.calc_plates(plate_weight, available_plates)
        for p_weight, p_count in plates.items():
            if used_plates[p_weight] < p_count:
                used_plates[p_weight] = p_count
        set_count += 1

    # Print summary
    for p_weight, p_count in used_plates.items():
        if p_count:
            print(F'     {p_weight}: {p_count}')

    return 0


def main():
    """function with no inputs to allow use as a console script"""

    available_plates = [45, 35, 25, 15, 10, 5, 2.5]
    bar_weight = int(input("Bar Weight:"))
    rep_max = int(input("One rep max:"))
    raw_list = input("Percentages for each set, space separated: ").split()
    percentages = [float(n)/100 for n in raw_list if n.isdigit()]

    sys.exit(main_function(bar_weight, rep_max, available_plates, percentages))

if __name__ == "__main__":

    main()
