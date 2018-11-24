Anwesenheitsliste:
jfeiner, mleitold, kschmid, aklautzer, sfilipovic, asackl, bmaderer, aschadler, dreindl, cradlingmayer, mwalzl, kgruber, asauer, kkoch, lhaidacher, akozlova, ekatic, lleopold, mprem, na, cfressl, afeichtinger, rgrossschaedl, lwechtitsch, nolah, asowinska, ftrenchevski, lsarcevic, awagner, nkaehling, akraus, lladinig, dspannermtomberger, igrasenick, nsucher, jgassner, jbaier, mklug

siehe
auch: folien & go - etherpad

schönen
Abend & Prost!





Demo
Code:

# !/usr/bin/python3
import threading, time


# Von Klasse Thread ableiten und dabei die "run"-Methode überschreiben...

# About RLock (reentrant => may be acquired multiple times by the same thread):
# https://docs.python.org/2/library/threading.html#rlock-objects


# with statement (better in the case an exception occures in the critical section)
# https://docs.python.org/2/library/threading.html#using-locks-conditions-and-semaphores-in-the-with-statement

class Customer(threading.Thread):
    def __init__(self, aAccount, no):
        threading.Thread.__init__(self)
        self.account = aAccount;
        self.no = no

    def run(self):
        # do something for a while (e.g. in a loop)
        for i in range(10, 15):
            print(" customer {} deposits now {}...".format(self.no, i))
            self.account.deposit(i)  # 10, 11, 12, 13, 14 (=60)


# Achtung, jetzt ist noch Locking nÃ¶tig!

class Account():
    def __init__(self):
        self.balance = 0;
        self.lock = threading.RLock();

    def deposit(self, amount):
        time.sleep(2)  # parallel waiting => 1*2 Secs
        with self.lock:  # instead of acquire/release
            temp = self.balance
            # ...calc something.. (depositing takes a little while)
            time.sleep(0.1)  # waiting 50 * 0,1 secs = 5 sec
            result = temp + amount
            self.balance = result
        print(" => current account: {}".format(result))


# ...dann eine Instanz erstellen und den Thread starten "start":

account = Account();

customers = [Customer(account, c + 1) for c in range(10)]

# Zeitliches Synchronisieren mit "join":

for i in customers:  # start the threads
    i.start()  # 10 customers doposits 5 times (with sum of 60€ each)...

for i in customers:  # wait for the threads to terminate
    i.join()

# after 50 deposits 2 secs mostly/some in parallel
#  and  50*0,1 secs serialised = ~ 5 secs
#               =>   > 7 secs (e.g. 11 secs)
# 10 customers * 60€ = 600€
print("Done: account-value= {}".format(account.balance))


