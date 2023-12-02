'''

Christina-Theano (Theatina) Kylafi
Advent of Code 2023

Day 1
Part 1

'''

import re

input_file="inputDay1.txt"
with open(input_file,"r",encoding="utf-8") as reader:
    doc=reader.read().split("\n")

val_list= [ re.findall(r"\d", value) for value in doc ] 
num_sum = sum( [ int(f"{val[0]}{val[-1]}") for val in val_list ] )

print(num_sum)