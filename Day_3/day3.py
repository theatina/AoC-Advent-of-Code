'''

Christina-Theano (Theatina) Kylafi
Advent of Code 2020

Day 3
Part 1

'''

input_map_list = list(open("./inputDay3.txt","r").read().split("\n"))

traverse_pos = [(i*3)%len(input_map_list[0]) for i in range(len(input_map_list))]

trees = 0
pos = 0
line = 0
pos_prev = traverse_pos[pos]
while line < len(input_map_list):
    if input_map_list[line][traverse_pos[pos]] == "#":
        trees+=1
    pos_prev = traverse_pos[pos]
    pos+=1
    line+=1
    
print(f"\nTotal trees encountered: {trees}\n")