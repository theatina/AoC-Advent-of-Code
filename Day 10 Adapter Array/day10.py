'''

Christina-Theano (Theatina) Kylafi
Advent of Code 2020

Day 10
Part 1

'''

def find_diffs(input_list):
    my_adapt = max(input_nums)+3
    input_nums.insert(0,0)
    input_nums.append(my_adapt)
    input_nums.sort()
    diffs = [ i-j for i,j in zip( input_nums[1:], input_nums[:-1] ) ]
   
    diff_1 = diffs.count(1)
    diff_3 = diffs.count(3)

    return diff_1,diff_3

input_nums = [ int(i) for i in list(open("./test.txt","r").read().split("\n")) ]

diff_1,diff_3 = find_diffs(input_nums)

print(f"\n{diff_1} * {diff_3}  = { diff_1 * diff_3 } \n")