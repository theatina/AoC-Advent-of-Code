'''

Christina-Theano (Theatina) Kylafi
Advent of Code 2020

Day 3
Part 2

'''

input_map_list = list(open("./inputDay3.txt","r").read().split("\n"))

step_right = [1,3,5,7,1]
step_down = [1,1,1,1,2]

trees_list = []
traverse_pos_list = []
counter = 0
for i,j in zip(step_right,step_down):
    traverse_pos_list.append([(line*i)%len(input_map_list[0]) for line in range(len(input_map_list))])

    trees = 0
    pos = 0
    line = 0
    pos_prev = traverse_pos_list[counter][pos]
    while line < len(input_map_list):
        if input_map_list[line][traverse_pos_list[counter][pos]] == "#":
            trees+=1
        pos_prev = traverse_pos_list[counter][pos]
        pos+=1
        line+=j
    
    counter+=1
    trees_list.append(trees)
        
mult_product = 1
for i in trees_list:
    mult_product*=i

trees_str = ", ".join([ str(i) for i in trees_list ])
print(f"\nTotal trees encountered: {trees_str}")
trees_str = " * ".join([ str(i) for i in trees_list ])
print(f"\nProduct {trees_str} : {mult_product}\n")
