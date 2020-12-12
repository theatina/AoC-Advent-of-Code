'''

Christina-Theano (Theatina) Kylafi
Advent of Code 2020

Day 4
Part 1

'''

import re

input_bpass_list = list(open("./inputDay4.txt","r").read().split("\n\n"))

input_bpass_list = [  re.split(r"[ : \n]+",i) for i in input_bpass_list]

valid = 0
for i in input_bpass_list:

    if set(["byr","iyr","eyr","hgt","hcl","ecl","pid"]).issubset(i):
        valid+=1

print(f"\nValid Passports: {valid}\n")

