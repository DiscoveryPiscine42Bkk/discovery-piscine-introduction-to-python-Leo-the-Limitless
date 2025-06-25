#!/usr/bin/env python3

import sys

def shrink(str):
    new_str = str[:8]
    print(new_str)

def enlarge(str):
    count = len(str)
    while count < 8:
        str += "Z"
        count += 1
    print(str)

args = sys.argv[1:]

if len(args) < 1:
    print("none")
else:
    for arg in args:
        if len(arg) < 8:
            enlarge(arg)
        elif len(arg) > 8:
            shrink(arg)
        else:
            print(arg)
