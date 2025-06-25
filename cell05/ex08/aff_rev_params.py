#!/usr/bin/env python3
import sys

length = len(sys.argv)
if length < 3:
    print("none")
else:
    i = length - 1
    while i > 0:
        print(sys.argv[i])
        i -= 1
