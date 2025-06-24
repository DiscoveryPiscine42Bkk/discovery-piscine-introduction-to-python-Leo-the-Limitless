#!/usr/bin/env python3

try:
    number = int(input("Enter a number less than 25: \n"))
except ValueError:
    print("Please Enter a valid integer")
    exit(1)

if number > 25:
    print("Error")

while number <= 25:
    print("Inside the loop, my variable is " + str(number))
    number += 1