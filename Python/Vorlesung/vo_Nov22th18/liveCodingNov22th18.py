#! /usr/bin/env python3

# Py06 "Concurrency" 22. November 2018 18:00-20:15
# ONL 1: https://meet.lync.com/fhjoanneum-edu/lynctest10/7ZCYRFYK
# https://git-iit.fh-joanneum.at/ProgKonz/2018ws-itm17-prog-konz/tree/master/2018-11-22_SWD17-Read-Concurrency-Code

# execute this etherpad at your computer in the terminal using:
#  curl 'https://houston.fh-joanneum.at/ep_moodle/p/g.JkK1v7EYT4Ggm0TQ$moodle/export/txt' > /tmp/tst.py 2>/dev/null; python3 /tmp/tst.py

import re

participants = re.split(r'[,;]\s+', """
jfeiner, mwalzl, bmaderer, rgrossschaedl, lwechtitsch, asackl,akraus, asowinska,aklautzer, mfeil, kkoch, sfilipovic, nsucher, mleitold, aschadler,  mprem, nolah, kschmid, kgruber, igrasenick, lleopold, afeichtinger, lsarcevic,ekatic, rrehberger, dspanner, lladinig, pdvorak, asauer,mtomberger, cfressl, dreindl, awagner, nkaehling,pdürnberger,bektas,akozlova,hgschwend,jgassner, mklug,mkonrad,jbaier, rhafellner;   
""")

##############
# just for fun: --- start ---
partAM = list(filter(lambda p: re.match(r'^[a-m]', p, re.I), participants))
partLZ = list(filter(lambda p: re.match(r'^[l-z]', p, re.I), participants))
print("""
A-M: {am}
L-Z: {lz}
""".format(
    am=" and ".join(partAM),
    lz=" and ".join(partLZ)
)
)
# just for fun:  --- end---
##############

print("""
Agenda
... Review OOP-Advanced: 
Operator Overloading: ...
Multiple inheritance: ...
+ Slides: Modules: ... import, from, __init__.py __cache__
+ Slides: Networking: ... server, request handler 

... Concurrency
Concurrency vs. Parallelism
preemtive vs. cooperative Multitasking 
Consequences (speed, parallelism) of Global Interpreter Lock (GIL)
Tasks/Process vs. Threads vs. Fibers vs. AsyncIO vs. ... 
... Read Code = Motivation
multithreaded server: "Daemon", "Workers", ...
(see code: ....https://git-iit.fh-joanneum.at/ProgKonz/2018ws-itm17-prog-konz/blob/master/2018-11-22_SWD17-Read-Concurrency-Code/dangerous-server.py )
... Read Code = Find problems
(see code: .... https://git-iit.fh-joanneum.at/ProgKonz/2018ws-itm17-prog-konz/blob/master/2018-11-22_SWD17-Read-Concurrency-Code/mt_oop.py )
time synchronisation
data synchronisation

READ code
TRY out
TRY run / start

=> Note your ideas / suggestions

until 19:25 run / analyse code mt_oop.py

19:25 Discussion

(1) output should be: <= idee auftraggeber
l ein, l2 ein, ...

status: alle sind ein

l brennt, l4 brennt ... 
l aus, l30 aus
x l2 ein 
x l2 brent
x l2 aus
...
zum ende:  verbrauch = kWh 8*30 = 240
(2) IST:
2a) l.run() => verbrauch passt
ABER: NICHT concurrent
Nachteil? dauert EWIG
2b) ohne run/start
nie aktiv: nie eingeschalten.... 
We light up the city:
Evening status: every of the 30 lights is on... and shining.
 Morning Summary: we consumed energy of 0 kWh
2c) l.start()
alles ok?
zu früh ausgabe (summary)

3 Verbessern: wie
a) Zeitliche Ausgabe summary:  
# warten bis alle threads beendet sind
ok, ABER: <> 240
Problem:
l3 merkt (liest v. powerconsumption) 43 kWh
l4 merkt (liest v. powerconsumption) 43 kWh
l7 merkt (liest v. powerconsumption) 43 kWh
l7 43 + 8 = 51 schreibt -> powerconsumtion = 51
l3 43 + 8 = 51 schreibt -> powerconsumtion = 51
l14 merkt (liest v. powerconsumption) 51 kWh
l4 43 + 8 = 51 schreibt -> powerconsumtion = 51
l14 51 + 8 = 59 schreibt -> powerconsumtion = 59
3 lichte 43 -> 59 ?? XX 
beschreiben gleichen speicher <= überschreiben sich 
b) Überschreiben verhindern, wie?
code-abschnitt schützen: synchronize, semaphore,.. 
code kann dann NUR von EINEM thread ausgeführt werden

technisch - python: Lock  acquire, release

Immer noch langsam (nicht "genug" concurrent)

c) acquire - release block of code umfasst
NUR lesen ändern schreiben einer "globalen" variable (gemeinsamer speicherbereich)








schönen Abend.... 

und UNBEDINGT SELBST nochmals probieren
"falsche Lösung" -> irgendeine richtige :) Lösung




TODO:
with block um exception ... 


... Coding / Modify Code = Solve problems
wait (join) for threads to finish, lock critical regions, 
be fair => take a break! 
... More (code) examples
Slides: eval, exec,... os.system, os.popen, sys.stdin, sys.stdout, os.fork,..
multithreading OOP vs. multithreading with "functions"
import threading, threading.Thread(...), class MyThread(threading.Thread) ...
start, run, time.sleep, setDaemon, ...
join, notify, notifyAll, ... 
threading.Lock, acquire, try: finally:, release, ...
multiprocessing: Pool, Queue, ... <= subprocesses (no threads) side-stepping GIL
""")


# - - - - -
# Useful Links:
# https://realpython.com/python-gil/


class Person:
    def __init__(self, name="unknown"):
        self._name = name

    def __str__(self):
        return "my name is " + self._name


class Racer:
    _score = 3

    def __str__(self):
        return "status=" + str(self._score)

    def setScore(self, score):
        self._score = score


# Note: without a __str__ method in RacingPerson
# the order of base-classes might be VERY important
class RacingPerson(Person, Racer):  # MRO (!)
    pass
    # def __str__(self):
    #        return Person.__str__(self) +" and " + Racer.__str__(self)


p2 = RacingPerson("Max")
p2.setScore(33)
print(p2)

# !/usr/bin/env python3

# measure time on linux with:
# > time ./mt_oop.py

import threading
from time import sleep

# read
#   => output should be (after __ secs):
#                   1.) ...
#                   2.) ...
#                   3.) ...
#                   4.) ...
#   => output currently is (after __ secs):
#                   1.)
#                   2.) ...
#                   3.) ...
#                   4.) ...
# repair
#   => (a) Problem: ...
#   => (b) Problem: ...

print("We light up the city:")
NO_OF_LIGHTS = 30
powerconsumption = 0


class Light(threading.Thread):
    lock = threading.Lock()

    def __init__(self, no):
        threading.Thread.__init__(self)
        self.no = no

    def run(self):
        global powerconsumption  # access global var

        # energy used up to now
        curr_powerconsumption = powerconsumption

        sleep(0.1)  # setup time (e.g.: press "ON" switch)
        print(self.no, ". lamp switched on.")

        print(self.no, ". lamp shining...")
        sleep(8)  # shining for 8 hours. Try 0.001

        sleep(0.1)  # setup time (e.g.: press "ON" switch)
        print(self.no, ". lamp switched off.")

        # update overall energy consumption
        powerconsumption = curr_powerconsumption + 8


lights = []
for no in range(NO_OF_LIGHTS):
    l = Light(no + 1)
    lights += [l]
    # try: l.run()
    l.start()  # l.run()

print("Evening status: every of the {} lights is on... and shining.".format(len(lights)))

# code?

print(" Morning Summary: we consumed energy of {} kWh".format(powerconsumption))
