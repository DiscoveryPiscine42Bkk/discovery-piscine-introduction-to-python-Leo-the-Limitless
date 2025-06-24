#!/usr/bin/env python3

num = int(input("Enter a number \n"))

for x in range(0, 10):
    result = x * num
    print(str(x) + " x " + str(num) + " = " + str(result))