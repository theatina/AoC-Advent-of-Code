'''

Christina-Theano (Theatina) Kylafi
Advent of Code 2020

Day 14
Part 1 

'''

def bin_to_dec(binary):
    decimal = sum([ 2**pos*int(bit) for pos,bit in enumerate(str(binary)[::-1]) ])
    return decimal

def bin_to_dec_from_list(binary):
    decimal = sum([ 2**pos*int(bit) for pos,bit in enumerate(binary[::-1]) ])
    return decimal

def dec_to_bin(decimal,binary):
    if decimal > 1:
        dec_to_bin(decimal // 2, binary)
    
    binary.append(decimal % 2)
    return binary

def dec_to_bin_fin(decimal,binary):
    return "".join([ str(i) for i in dec_to_bin(decimal,[])])


import re 

input_file = [ i.split(" = ") for i in list(open("./inputDay14.txt","r").read().split("\n")) ] 
print(input_file)

mem_dict = {}
zeros_36bit_num = [ 0 for i in range(36)]
for i in input_file:
    if i[0]!="mask":
        mem_num = int(re.findall(r"\d+",i[0])[0])
        value = int(i[1])
        mem_val_dec = dec_to_bin_fin(value,[]) 
        length = len(str(mem_val_dec))
        value_36bit = zeros_36bit_num.copy()[:-length]
        value_36bit.extend([ int(i) for i in str(mem_val_dec) ])
        masked_value_36bit = [ value_i if mask_i=="." else mask_i for mask_i,value_i in zip(mask_36bit, value_36bit) ]

        mem_dict[mem_num] = masked_value_36bit

    else:
        mask = i[1]
        mask_36bit = [ "." if i=="X" else int(i) for i in mask ]
        print(mask_36bit)

sum_of_mems = 0

for i in mem_dict.values():
    sum_of_mems+= bin_to_dec_from_list(i)

print(f"\nSum of mem values: {sum_of_mems}\n")