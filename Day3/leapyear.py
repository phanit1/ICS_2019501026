"""Python program to check if YEAR is a leap YEAR or not
"""
YEAR = 2020
if (YEAR % 4) == 0:
    if (YEAR % 100) == 0:
        if (YEAR % 400) == 0:
            print("{0} is a leap YEAR".format(YEAR))
        else:
            print("{0} is not a leap YEAR".format(YEAR))
    else:
        print("{0} is a leap YEAR".format(YEAR))
else:
    print("{0} is not a leap YEAR".format(YEAR))
