#!/usr/bin/env python

"""whichPlates.py: Returns weight and plates needed per set based on 1 RM."""

from decimal import *


##############################################################
# func_input_sets()
# This function prompts user for percentages of each set and
# returns list of percentages
# inputs: None
# returns: List of 1 rep max percentages.
def func_input_sets():
    list = raw_input("Percentages for each set, space separated: ").split()
    return [float(n)/100 for n in list if n.isdigit()]


##############################################################



##############################################################



if __name__ == "__main__":
    setCount = 1
    weightInSet = []
    usedPlates = {}
    availablePlates = [45, 35, 25, 15, 10, 5, 2.5]


    barWeight = int(input("Bar Weight:"))
    repMax = int(input("One rep max:"))
    workingWeight = repMax - barWeight
    percentages = func_input_sets()

    for plates in availablePlates:
        usedPlates[plates] = 0

    for percent in percentages:
        weight = func_round_num((repMax * percent) - barWeight)
        if weight <= 0:
            print '    Computed weight less than bar weight, try again'
        else:
            print "Set " + str(setCount) + " @ " + str(percent * 100) + '%: ' + str((weight + barWeight)) + "lbs, " + str(weight) + "lbs in plates"
        plates = func_calc_plates(weight, availablePlates)

        for plate in plates:
            if usedPlates[plate] < plates[plate]:
                usedPlates[plate] = plates[plate] * 2
            print "     " + str(plate) + ":" + str(plates[plate] * 2)
        setCount += 1

    # Print summary
    print 'Plates Needed:'
    for plate in usedPlates:
        if usedPlates[plate]:
            print '     ' + str(plate) + ': ' + str(usedPlates[plate])
