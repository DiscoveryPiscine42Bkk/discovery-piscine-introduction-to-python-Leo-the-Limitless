#!/usr/bin/env python3

org_arr = [2, 8, 9, 48, 8, 22, -12, 2]
new_arr = [x + 2 for x in org_arr if x > 5]

print(f"Original array: {org_arr}")
print(f"New array: {new_arr}")