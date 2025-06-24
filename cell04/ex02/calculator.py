#!/usr/bin/env python3

first_input = input("Give me the first number: ")
second_input = input("Give me the second number: ")

try:
    first_num = int(first_input)
    second_num = int(second_input)
except ValueError:
    print("Please Enter Valid Numbers!")
    exit(1)

print("Thank you!")

addition = first_num + second_num
print(f"{first_num} + {second_num} = {addition}")

subtraction = first_num - second_num
print(f"{first_num} - {second_num} = {subtraction}")

try:
    division = first_num / second_num
    print(f"{first_num} / {second_num} = {division}")
except ZeroDivisionError:
    print("For the division, the denominator cannot be zero.")

multiplication = first_num * second_num
print(f"{first_num} * {second_num} = {multiplication}")