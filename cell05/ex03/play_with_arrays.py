#!/usr/bin/env python3

org_arr = [2, 8, 9, 48, 8, 22, -12, 2]
new_arr = [x + 2 for x in org_arr if x > 5]
new_set = set(new_arr)

print(org_arr)
print(new_set)