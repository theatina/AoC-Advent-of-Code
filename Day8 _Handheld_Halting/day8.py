'''

Christina-Theano (Theatina) Kylafi
Advent of Code 2020

Day 8
Parts 1 & 2

'''

# -------> Part 1 <------- #
def acc_value(input_list):
    visited = []
    acc_value = 0
    running_condition = True
    input_line = 0
    termination_status = 0
    while running_condition: 
        line = input_list[input_line]
        visited.append(input_line)
        action = line[0]
        step = int(line[1])
        if action == "acc":
            acc_value+=step
            input_line+=1
        
        elif action == "nop":
            input_line+=1

        elif action == "jmp":
            input_line+=step
        
        if input_line in visited:
            termination_status = 0 #loop
            break
        
        elif input_line >= len(input_list):
            termination_status = 1 #ended
            break
            
    return acc_value, visited, termination_status

input_list = list(open("./inputDay8.txt","r").read().split("\n"))
input_list = [ i.split(" ") for i in input_list ]

accum_value, visited, terminated = acc_value(input_list)
print(f"\nAccumulator's value (part 1): {accum_value}")

# -------> Part 2 <------- #
def check_termination(input_list):
    terminated = 0
    input_list_2 = input_list.copy()
    accum_value, visited, terminated = acc_value(input_list_2)
    
    while terminated==0:
        line_to_change = visited[-1]
        action = input_list_2[line_to_change][0]

        while action=="acc":
            visited.pop(len(visited)-1)
            line_to_change = visited[-1]
            action = input_list_2[line_to_change][0]

        if action=="nop":
            input_list_2[line_to_change][0] = "jmp"
        else:
            input_list_2[line_to_change][0] = "nop"

        visited.pop(len(visited)-1)
        accum_value, visited_temp, terminated = acc_value(input_list_2)

    return accum_value
     

accum_value = check_termination(input_list)
print(f"\nAccumulator's value (part 2): {accum_value}\n")
