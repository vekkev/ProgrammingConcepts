#!/usr/bin/env python3
import sys
# 2018 by the famous python coder: <Kevin Gruber>

res = int(sys.argv[1]) + int(sys.argv[2])  # You might consider slices with [:], argv, map, sum, int, ... (no error handling required)

print("Python Week 1/7: The sum of command line arguments {} is '{}'.".format(sys.argv[1:], res))

