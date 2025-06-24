#!/usr/bin/env python3

i = 0
while i <= 10:
    print("Table de " + str(i) + ": ", end="")
    j = 0   
    while j <= 10:
        print(i * j, end=" ")
        j += 1
    i += 1
    print("")