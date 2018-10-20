#!/usr/bin/env python3

# Requirement for Python Upload 03 about regex and generators:
#
# a) Comments required: Add your Name
#    remove this comments or other unused lines of code

# b) For regular expressions:
#    b1) extract all emails from the given html source
#    b2) return all teachers (firstname, lastname) from given html source
#
#    Just for your information: this is (a slightly modified) extracted html snippet from https://archiv.fh-joanneum.at/aw/home/Studienangebot-Uebersicht/department-angewandte-informatik/swd/Menschen/Team/~mcq/lehrpersonal/?lan=de )

# c) For generators
#    c1) generate filenames "2018_img_001.jpg", "2018_img_002.png"..."2018_img_999.svg"

# NOTE: "evaluate" works just within the FH Network! Maybe you want to use VPN.

def extractEmailsFromHTML(src):
    list = []
    one_entry_list = []
    result = []
    result = []

    #### START of my CODE ####

    # find with regex emails (e.g. norah*smith#edu*fh-joanneum*at )
    # import re

    import re
    list = re.findall('[a-zA-Z0-9\*-]+#[a-z*-?]+', str(src))

    # repair emails (by replacing characters *, #)
    # and add those to the result (list)

    for i in list:
        if i not in one_entry_list:
            one_entry_list.append(i)

    for word in one_entry_list:
        line = word.replace('*', '.')
        line = line.replace('#', '@')
        result.append(line)

    #### END of my CODE ####
    return result


def extractNamesFromHTML(src):
    result = []
    #### START of my CODE ####

    # find with regex (firstname/lastname)-tuples
    # and add to the result (list):
    # [ ("Norah","Smith"), (...,...), (...,...) ]

    import re
    teacher_names = re.findall('<strong>(.*?)</strong>', src)
    for name in teacher_names:
        name = name.rsplit(" ", 1)
        name = tuple(name)
        result.append(name)

    return result

    #### END of my CODE ####
    return result


def fileNameGenerator(year=2021, suffix="jpg", count=99):
    #### START of my CODE ####

    for counter in range(1, count + 1):
        name = "_".join([str(year), 'img', format(counter, '03d')])

        yield name + "." + suffix

    # yield x-times something like 2018_img_005.svg ...

    #### END of my CODE ####


# Just for testing:

# (the moodle-"evaluate" will use the exact same test data!!)
htmlSource = open("team_itm.html", encoding='utf-8').read()
# print(htmlSource) # ...<h2><br /><strong>Norah Smith</strong><br/> ...onclick="javascript:anschreiben('norah*smith#edu*fh-joanneum*at')" onmouseover=...

for firstname, lastname in extractNamesFromHTML(htmlSource):
    print(lastname)  # Smith

for email in extractEmailsFromHTML(htmlSource):
    print(email)  # norah.smith@edu.fh-joanneum.at

# (the moodle-"evaluate" might run with different test data!!)
for bc in fileNameGenerator(2016, "png", 4):
    print(bc)  # prints: "2016_img_001.png",...,"2016_img_004.png"

for bc in fileNameGenerator(2019, "svg", 9):
    print(bc)  # prints: "2019_img_001.svg",...,"2019_img_009.svg"

