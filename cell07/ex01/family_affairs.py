#!/usr/bin/env python3

def find_the_redheads(fam):
    red_filtered_names = [k for k,v in fam.items() if v == "red"]
    return red_filtered_names

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))