'''

Christina-Theano (Theatina) Kylafi
Advent of Code 2020

Day 1
Part 1

'''

input_nums_list = list(set(open("./inputDay1.txt","r").read().split("\n")))
input_nums_list = [int(i) for i in input_nums_list]
input_nums_list.sort()

for i in input_nums_list[::-1]:
    for j in input_nums_list[::]:
        if i+j>2020:
            break
        elif i+j==2020:
            print(f"\n{i} + {j} = {i+j} - {i} * {j} = {i*j}\n") 
            exit()
        