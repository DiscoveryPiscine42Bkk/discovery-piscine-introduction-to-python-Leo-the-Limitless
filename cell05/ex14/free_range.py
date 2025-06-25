#!/usr/bin/env python3
import sys

args = sys.argv[1:]

if len(args) == 2:
    start = args[0]
    end = args[1]

    result = list(range(int(start), int(end) + 1))
    print(result)
else:
    print("none")