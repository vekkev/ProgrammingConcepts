#!/usr/bin/env python3

# Requirement for Python Upload 06 about Multithreading:
#
#
# a) Comments required: Add your Name
#    remove this comments or other unused lines of code

# b) Multithreading:
#    Create a class to simulate concurrent "downloading of x files with the size of y MB each"
#    return the final amount of MB downloaded.
#    REQUIRED: a thread for each download,
#              (concurrent) waiting 2 secs for each download
#              locking when accessing common memory


import time
import threading


class Download(threading.Thread):
	lock = threading.Lock()

	def __init__(self, number, mb):
		threading.Thread.__init__(self)
		self.number = number
		self.mb = mb

	def run(self):
		global wholeDownload
		time.sleep(2)
		Download.lock.acquire()
		tmp = wholeDownload
		time.sleep(0.001)
		wholeDownload = tmp + self.mb
		Download.lock.release()


def startup(no_of_concurrent_downloads, mb):
	global wholeDownload
	wholeDownload = 0
	downloads = []

	for no_of_concurrent_downloads in range(no_of_concurrent_downloads):
		downloads.append(Download(no_of_concurrent_downloads, mb))

	for number in downloads:
		number.start()

	for number in downloads:
		number.join()

	return ("Downloaded {} MB.".format(wholeDownload))


# Just for testing:

# (the moodle-"evaluate" might  use different test data set!)

print('\nTEST "concurrency":')
print(startup(33, 3))  # Downloaded 99 MB.