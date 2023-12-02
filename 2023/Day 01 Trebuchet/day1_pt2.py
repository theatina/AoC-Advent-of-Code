'''

Christina-Theano (Theatina) Kylafi
Advent of Code 2023

Day 1
Part 2

'''

import re

digit_dict={ 
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9 }

input_file="inputDay1.txt"
with open(input_file,"r",encoding="utf-8") as reader:
    doc=reader.read().split("\n")
    before=[]
    # TODO - check for cases sharing chars e.g. "eightwo" -> 82 or 88?
    for i,line in enumerate(doc):
        l = [ (obj.start(), obj.end(), obj.re.pattern) for word in digit_dict.keys() for obj in re.finditer(word,line)  ]
        l = [ lis[2] for lis in sorted(l, key=lambda x: x[0], reverse=False) if lis]
        before_line=doc[i]
        for w in l:
            line=line.replace(w,str(digit_dict[w]))
        doc[i]=line
        before.append([ before_line,doc[i] ])

val_list= [ re.findall(r"\d", value) for value in doc ] 


# for b,n in zip(before,[ int(f"{val[0]}{val[-1]}") if val else 0 for val in val_list ]):
#     print(b,n)

num_sum = sum( [ int(f"{val[0]}{val[-1]}") if val else 0 for val in val_list ] )

print(num_sum)