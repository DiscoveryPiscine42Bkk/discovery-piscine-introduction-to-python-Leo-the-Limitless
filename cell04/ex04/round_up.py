#!/usr/bin/env python3
import math

num = input("Give me a number: ")

try:
    number = float(num)
    print(math.ceil(number))
except ValueError:
    print("Please Enter a valid number!")
