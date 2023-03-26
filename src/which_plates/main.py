""" main function for which_plates"""

import sys
from . import functions


def main():
    """main function
    """

    set_count = 1
    weight_in_set = []
    used_plates = {}
    available_plates = [45, 35, 25, 15, 10, 5, 2.5]


    bar_weight = int(input("Bar Weight:"))
    rep_max = int(input("One rep max:"))
    working_weight = rep_max - bar_weight

    raw_list = input("Percentages for each set, space separated: ").split()
    percentages = [float(n)/100 for n in raw_list if n.isdigit()]
    

    for plates in available_plates:
        used_plates[plates] = 0

    for percent in percentages:
        weight = functions.round_num((rep_max * percent) - bar_weight)
        if weight <= 0:
            print ('    Computed weight less than bar weight, try again')
        else:
            print(F"Set {set_count} @ {round(percent * 100)}%: {round(weight + bar_weight)}lbs, {round(weight)}lbs in plates")
        plates = functions.calc_plates(weight, available_plates)

        for plate in plates:
            if used_plates[plate] < plates[plate]:
                used_plates[plate] = plates[plate] * 2
            print(F"     {plate}: {plates[plate] * 2}")
        set_count += 1

    # Print summary
    print ('Plates Needed:')
    for plate in used_plates:
        if used_plates[plate]:
            print(F'     {plate}: {used_plates[plate]}')


if __name__ == "__main__":
    sys.exit(main())
