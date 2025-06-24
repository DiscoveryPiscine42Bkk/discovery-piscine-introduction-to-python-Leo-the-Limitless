#!/usr/bin/env python3

age_str = input("Please tell me your age: ")

try: 
    age_int = int(age_str)
    in_ten = age_int + 10
    in_twenty = age_int + 20
    in_thirty = age_int + 30

    print("You are currently " + age_str + " years old.")
    print("In 10 years, you'll be " + str(in_ten) + " years old.")
    print("In 20 years, you'll be " + str(in_twenty) + " years old.")
    print("In 30 years, you'll be " + str(in_thirty) + " years old.")
except ValueError:
    print("Please Enter a valid integer!")