#!/usr/bin/env python3
import sys

args = sys.argv[1:]

if len(args) == 1:
    count = 0
    for c in args[0]:
        if c == "z":
            print(c, end="")
            count += 1

    if count == 0:
        print("none", end="")
        
    print("")
else:
    print("none")