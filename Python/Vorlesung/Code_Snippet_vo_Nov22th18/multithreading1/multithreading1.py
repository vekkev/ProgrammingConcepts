#!/usr/bin/env python3

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