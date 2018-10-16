#!/usr/bin/env python3

# Requirement for Python Upload 01: split & slice
#
# a) Comments required: Add your Name
#    remove this comments / unused lines of code
# b) Return your last name in lowercase letters
#    after splitting your full name which you specify as string.
#    e.g. "11. Nov. 2018 by John Feiner, ITM23"



def main():
    result = None

    #### START of my CODE ####

    fullname = "Kevin Gruber"
    splitname = fullname.split()

    name = "4. Nov. 2017 by xxx yyyy, SWD16"

    name2 = name.split()

    name2[4] = splitname[0]
    name2[5] = splitname[1].lower()

    result = ' '.join(name2)

    #### END of my CODE ####

    return result


print(main())
