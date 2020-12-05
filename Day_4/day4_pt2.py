'''

Christina-Theano (Theatina) Kylafi
Advent of Code 2020

Day 4
Part 2

'''

import re

input_bpass_list = list(open("./inputDay4.txt","r").read().split("\n\n"))
input_bpass_list = [  re.split(r"[ : \n]+",i) for i in input_bpass_list]

valid = 0
att_dict = {}
for i in input_bpass_list:
    att_dict = {}
    if set(["byr","iyr","eyr","hgt","hcl","ecl","pid"]).issubset(i):
        
        for k in range(0,len(i)-1,2):
            att_dict[i[k]] = i[k+1]

        matched_byr = bool(re.match("19[2-9][0-9]|200[0-2]", att_dict["byr"]))
        matched_iyr = bool(re.match("201[0-9]|2020", att_dict["iyr"]))
        matched_eyr = bool(re.match("202[0-9]|2030", att_dict["eyr"]))
        matched_hgt = bool(re.match("1[5-8][0-9][cm]|19[0-3][cm]|59[in]|6[0-9][in]|7[0-6][in]", att_dict["hgt"]))
        matched_hcl = bool(re.match("#{1}[a-z0-9]{6}$", att_dict["hcl"]))
        matched_pid = bool(re.match("[0-9]{9}$", att_dict["pid"]))
        
        matched_ecl = True
        if att_dict["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            matched_ecl = False
        
        check = matched_byr * matched_iyr * matched_eyr * matched_hgt * matched_hcl * matched_pid * matched_ecl

        if check:
            valid+=1


print(f"\nValid Passports: {valid}\n")