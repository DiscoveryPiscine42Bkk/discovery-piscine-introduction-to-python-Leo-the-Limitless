#!/usr/bin/env python3

msg_string = input("")

for m in msg_string:
    if m.isupper():
        print(m.lower(), end="")
    else:
        print(m.upper(), end="")

print("")