'''

Day 10
Part 2

'''
import numpy 

def find_diff(input_list):
    my_adapt = max(input_nums)+3
    input_nums.insert(0,0)
    input_nums.append(my_adapt)
    input_nums.sort()
    diff = [ i-j for i,j in zip( input_nums[1:], input_nums[:-1] ) ]
    
    return diff

def all_paths(input_list,diffs):
    '''

    Function by Ricardo Busquet 
    GitHub profile: https://github.com/rbusquet
    File: https://github.com/rbusquet/advent-of-code/blob/main/2020/day_10/day_10.py

    '''

    paths = {}
    for i in input_nums[1:-1]:
        paths[i] = 0

    paths[1] = 1

    for adapter in input_nums[1:-1]:
        for diff in range(1, 4):
            next_adapter = adapter + diff
            if next_adapter in input_nums[1:-1]:
                last_adapter = next_adapter
                paths[next_adapter] += paths[adapter]
    
    print(paths)
    return paths[last_adapter]


input_nums = [ int(i) for i in list(open("./test.txt","r").read().split("\n")) ]

diffs = find_diff(input_nums)
combinations = all_paths(input_nums,diffs)
print(f"\n{combinations} Combinations\n")