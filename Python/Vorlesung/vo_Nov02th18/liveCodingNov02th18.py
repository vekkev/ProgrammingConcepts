#! /usr/bin/env python3
info = """
Py05 "OOP-Advanced" 2. November 2018 16:30-18:45 
ONL 2 https://meet.lync.com/fhjoanneum-edu/lynctest10/KPL4JFMQ
"""


# execute this etherpad at your computer in the terminal using:
#  curl 'https://houston.fh-joanneum.at/ep_moodle/p/g.egFBUkgwXjHjdE9e$moodle/export/txt' > /tmp/tst.py 2>/dev/null; python3 /tmp/tst.py

class Participant:
    def __init__(self, name):  # constructor, self ~ this

        self.name = name


# def __str__(self): # toString
# return self.name

##################################
# "HörerInnen einer Lehrveranstaltung"
##################################
# whoops, da hats was :D zwei mal 'ak' drinnen als key
participantsLookupDict = {
    'jf': Participant("john feiner"),
    'ml': Participant("Manuel Leitold"),
    'mw': Participant("Martin Walzl"),
    'bm': Participant("Bernd Maderer"),
    'ak': Participant("anastasiia kozlova"),
    'ak2': Participant("Andreas Kraus"),
    'nk': Participant("Nicoletta Kaehling"),
    'as': Participant("Angelika Sauer"),
    'pd': Participant("Philip Dvorak"),
    'kg': Participant("Kevin Gruber"),
    'll': Participant("Lucca Ladinig"),
    'as': Participant("Alexander Schadler"),
    'af': Participant("Andreas Feichtinger"),
    'ab': Participant("aldin bektas"),
    'no': Participant("Nimrod Olah"),
    'sf': Participant("stefan filipovic"),
    'mg': Participant("maximilian gurdet"),
    'cr': Participant("Christian Radlingmayer"),
    'ks': Participant("Kevin Schmid"),
    'cf': Participant("Christian Fressl"),
    'hg': Participant("Hannes Gschwend"),
    'ns': Participant("Natalya Sucher"),
    'll': Participant("Leonhard Leopold"),
    'ss': Participant("Simon Schönegger"),
    'kk': Participant("kerstin koch"),
    'ak3': Participant("anna klautzer"),
    'mp': Participant("Markus Prem"),
    'ft': Participant("Filip Trenchevski"),
    'ig': Participant("ingo grasenick"),
    'as': Participant("andrea sackl"),
    'mf': Participant("Maximilian Feil"),
    'jg': Participant("Jennifer Gassner")
    'mk': Participant("Markus Konrad"),
    'mk2': Participant("Michael Klug"),
    'pd': Participant("Patrick Dürnberger"),
    'dr': Participant("David Reindl"),
    'ek': Participant("Elvira Katic"),
    'lw': Participant("Lukas Wechtitsch"),
    'mt': Participant("Markus Tomberger"),
    'as': Participant("Agnieszka Sowinska"),
    'rr': Participant("Rehberger Raffael"),
    'rh': Participant("Robert Hafellner"),
    'aw': Participant("Alexander Wagner"),
    'ds': Participant("Doris Spanner"),
    'dg': Participant("Dominic Gross"),
    'jb': Participant("Jasmin Baier"),
    'ls': Participant("Lejla Sarcevic")
}
print("Happy to meet {you}!".format(
    you=" and ".join(map(str, participantsLookupDict.values()))
))


##################################
# Working with objects/classes
##################################
# self nit vergessen
class Link:
    def __init__(self, url, desc):
        self.url = url
        self.desc = desc

    def __str__(self):
        return self.url + ":  " + self.desc


class PyOnl:
    """Python online lecture for/with SWD"""


def __init__(self, topic="", on="", linkSet=set()):
    self.topic = topic


self.on = on
self.linkSet = linkSet


# pass

def __getitem__(self, key):  # py05onl2[ "Python Hilfe" ] => return the link
    pass  # TODO


def display_info(self):
    print (info, "Hear you soon at 16:30")  # info ??


print("following links were added:")
for link in self.linkSet:
    print(link)


def reviewOOP():
    pass


def addLink(self, link):
    self.linkSet.add(link)


##################################
# Main
##################################

if __name__ == '__main__':
    print("Some examples with class:", PyOnl.__doc__)

    py05onl2 = PyOnl(on="2018-11-02", topic="OOP-Advanced")
    pyLink = Link("http://python.org", "Python Hilfe")
    py05onl2.addLink(pyLink)
    py05onl2.display_info()

    # reviewOOP: 16:30-17:00 students G,H,I,...
    # create class "SmartNode" for adding notes (inkluding a link-url) to the PyOnl....
    #    then add SmartNodes about properties and about super (see below)

    # CODE REVIEW (Remarks/Discussion ... your uploads of Py04)
    # see:
    # https://houston.fh-joanneum.at/ep_moodle/p/g.zShNfKjnbiDtF5y9$moodle

    # refactor class hierarchy: base class = PyLecture, specialised: PyLab PyOnl
    # constructor/toString/inheritance/... class variables (count no of instances, share large data,...)... isinstance, __private

    # readCode <= find three ways to call a base method (or base constructor) 17:00-17:15
    # e.g. read https://docs.python.org/3/library/functions.html#super

    # OOP-Advanced  17:15-17:25: Operator-Overloading []
    # room = py05onl2['2018-11-02"]

    # OOP-Advanced  17:25-17:45: Multiple Inheritance <= what is "mro" (method resolution order)? # A, B, C
    # e.g. another base class "Scheduler": start, stop, trigger in x minutes

    # optional: 17:45 - 18:15 (break/read) "Properties" (better than getter/setter??, differences to getter/setter ??)
    # https://www.programiz.com/python-programming/property

    # optional: structure code until 18:40
    # => put your class into a module,
    # => put your classes into several modules

    # outlook 18:40-18:45
    # upcoming lecutures
    # concurrency / multithreading(!!) first in py then in go

# schönen Abend...






