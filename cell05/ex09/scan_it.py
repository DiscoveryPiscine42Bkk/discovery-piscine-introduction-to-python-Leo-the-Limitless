#!/usr/bin/env python3
import sys
import re

args = sys.argv[1:]

if len(args) == 2:
    pattern = args[0]
    string = args[1]
    matches = re.findall(pattern, string)
    if len(matches) == 0:
        print("none")
    else:
        print(len(matches))
else:
    print("none") 