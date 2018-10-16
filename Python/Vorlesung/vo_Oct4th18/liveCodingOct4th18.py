#! /usr/bin/env python3
# Py02 "Functional" 4. October 2018 19:00-22:00 ONL 2 https://meet.lync.com/fhjoanneum-edu/lynctest10/KPL4JFMQ
# execute this etherpad at your computer in the terminal using:
#  curl 'https://houston.fh-joanneum.at/ep_moodle/p/g.5xgDdhsQ20eObaVT$moodle/export/txt' > /tmp/tst.py 2>/dev/null; python3 /tmp/tst.py

# Hear you soon at 19:00 :)

students = [
     # enter YOUR NAME here (note the comma ',' at end of line):
"j. feiner",
"a. sauer",
"d.reindl",
"s.filipovic",
"m.gurdet",
"m.walzl",
"k.schmid",
"c.fressl",
"l.sarcevic",
"a.feichtinger",
"a.schadler",
"r.rehberger",
"s.schoenegger",
"n.sucher",
"k.gruber",
"a.wagner",
"m.tomberger",
"d.spanner",
"a.kraus",
"a.klautzer",
"n.kaehling",
"l.leopold",
"h.gschwend",
"p. dvorak",
"m.leitold",
"m.prem",
"c.radlingmayer",
"a.bektas",
"j.gassner",
"b.maderer",
"m.konrad",
"n.olah",
"f.trenchevski",
"p.duernberger",
"l.wechtitsch",
"m.klug",
"r. hafellner",
"j.baier",
"l.haidacher",
"a.sackl",
"a.sowinska",
"m.feil",
"e.katic",
"i.grasenick",
"r.grossschaedl",
"a.kozlova",
"d.gross",
"j.kaufmann",
"l.ladinig"
]

# print("Welcome SWD17: {stds}".format( stds = students) )

agenda = """
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
Agenda 19:00 - 22:00 3h = 4 EH
======
1) Review: by Students Z->A
What is a script? What is the "interactive python shell" (REPL read execute print loop) # *.py
How to execute? #!
Python help yourself: python3, dir, help, ... 
import, online help for modules <= try import this
Python datastructures: lists and slices []... <= see cheat sheet
Everything is a list: for each ELEMENT in LIST

2.) Input and "coding together": 
What means "functional" programming? 
Advantages/Disadvantages
More Python datastructures and methods
"strings" <= format, upper, int, split, join, ... <= see cheat sheet
list [] <= join, pop, sort, ... <= see cheat sheet
tuple () <= how to add and remove values?
set {} <= useful for ??
map {} <= keys, values, items, .... <= see cheat sheet
Syntax <= (multiple) assignments, operators (%, !, in), conditional statements, loops, .... True/False,... None
Useful functions: range, ... <= e.g. range returns which kind of object?
Operations on "Containers":
len, sorted, enumerate, ...  <= see cheat sheet
Functions "first class citizens"
def <= named parameter, multiple return values (tuples), default values, _ , ... *args, *kwargs
'_' ist auch nur eine Variable, oder? man kann sie zuweisen und dann z.B. ausgeben
Filter, Map, Reduce:
lambda

BREAK: Coffee?

READ CODE until 21:45 
3) Read real-world Code "on your own"
a) script prepare_manpage.py from youtube downloader
https://github.com/rg3/youtube-dl/blob/master/devscripts/prepare_manpage.py
Question-1 Py2 or Py3?
Question-2 docu, default values, return values, error handling?
Question-3 compare with "Style Guide"
 (https://www.python.org/dev/peps/pep-0008/ vs.
  https://github.com/google/styleguide/blob/gh-pages/pyguide.md )
Question-4 guess, what are the imported libraries good for?
b) https://github.com/getDolla/map-reduce/blob/master/mapreduce.py
Question-1 what is "text" in line 21, what in line 22?
Question-2 did you find: "map", "filter", "lambda"? explain each usage!
Question-3 explain the inner workings of the list comprehension (line 22)!

Bei Bedarf ... Fragen gerne gleich hier sammeln:
    ? ...Frage: Sollen die Übungen immer am / bis Montag abgegeben werden oder bis nächsten Unterricht, bzw. welche Fristen? Danke!
    ? ...

5.) 21: 45 Discussion

a) docu, style, __main__, ...  find out all possible python keywords
...
Das Filehandle wird nie geschlossen ;) Es gibt ja die with open() x:

b) what about recursion (memory usage,...)? what about concurrency (side-effects, sync, ...)?

22:00... Ich wünsche einen schönen Abend!

* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 






Beer, 


# Punkt 4 ist optional, wer möchte darf natürlich schon gerne üben ;)

4.) Code "on your own" <= da werden wir am Samstag einiges coden...
Time to code on your own
a) extract the two digit year from string
b) print all even numbers from 2314 down to 1917
c) create a function to compute the sum of two, three or four numbers
d) print out your “shrinking name” e.g. “Markus”, “Marku”, “Mark”, “Mar”,...
e) print a numbered list (e.g. english terms “ten”, “nine”, “eight”,...”zero”)
f) print a (reverse) sorted list of the names of your colleges
--
g) create some statistics: return list with len of strings of long text
h) normalize text (e.g.: lowercase, remove special chars,... ), optional: remove duplicates 
-- optional --
i) re-implement some solutions shorter: e.g. use list/dictionary comprehension (instead of: for, filter, map,...)
j) read data from commandlineargs/input/web/file-system, output to file in "excel" format



"""
# print(agenda)
# Python help yourself: python3, dir, help, ...
currYear = "2018"
print(dir(currYear))
#help(str.format)

# import, online help for modules <= try import this
import sys
arguments = sys.argv
print("ARGS: ",arguments)

# Python datastructures: lists and slices []... <= see cheat sheet
aList = ['A','B']
aList.reverse()
print(aList)
aList = ['a','A','C','b','c','B']
aList.sort(reverse = True)
# aList.reverse()
print(aList)


## reverse liefert void zurück bzw. None *IN PLACE *

# and slices []... <= see cheat sheet

title = "I am from Austria"[-7:]
print(title)

# Everything is a list: for each ELEMENT in LIST
words = """Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.""".split()
print(words)
for w in words:
   if len(w)>7:
        print(w)

# Viele Grüße aus Flixbus!
# Entschuldigen Sie mich bitte, es tut mir leid, aber ich habe eine sehr schwache Internetverbindung und kann nichts sehen,
# nur hören und auch dies nicht immer.
# Und gerade um 21:25 soll ich umsteigen.
