#!/usr/bin/env python3
import sys

args = sys.argv[1:]
if len(args) < 2:
    print("none")
else:
    for rev in reversed(args):
        print(rev)