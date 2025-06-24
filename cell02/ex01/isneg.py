#!/usr/bin/env python3

try:
    number = int(input(""))
except ValueError:
    print("Not a valid Number.")
    exit(1)

if number < 0:
    print("This number is negative.")
elif number > 0:
    print("This number is positive.")
else:
    print("This number is both positive and negative.")