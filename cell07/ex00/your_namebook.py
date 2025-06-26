#!/usr/bin/env python3

def array_of_names(people):
    full_names = [k.capitalize() + " " + v.capitalize() for k, v in people.items()]
    return full_names

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))