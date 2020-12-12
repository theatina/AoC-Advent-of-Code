'''

Christina-Theano (Theatina) Kylafi
Advent of Code 2020

Day 9
Parts 1 & 2

'''

def check_sum(num,prev_nums):
    result = 0
    prev_nums_sorted = prev_nums.copy()
    prev_nums_sorted.sort(reverse=True)

    prev_nums_sorted = [ i for i in prev_nums_sorted if i <= num ]

    for i in prev_nums_sorted:
        for j in prev_nums_sorted[prev_nums_sorted.index(i)+1:]:

            if i+j == num and i!=j:
                result = 1

    return result

def window_sum(window):
    return sum(window)

def sum_min_max_window(window):
    return min(window)+max(window)

def find_window(input_nums,num):
    start = 0
    end = 2
    window = input_nums[start:end]
    sum_of_window = window_sum(window)

    while sum_of_window!= num:  
        window = input_nums[start:end]
        sum_of_window = window_sum(window)
        if sum_of_window > num:
            start+=1
            end = start+2  
        else:
            end+=1  

    return window

input_nums = [ int(i) for i in list(open("./inputDay9.txt","r").read().split("\n")) ]

start = 0
step = 25
preamble = input_nums[start:start+step]
for i in input_nums[step:]:
    result = check_sum(i,preamble)
    if result==0:
        number = i
        print(f"\nFirst number: {i}\n")
        break

    start+=1
    preamble = input_nums[start:start+step] 
    
window = find_window(input_nums,number)
sum_min_max_window_result = sum_min_max_window(window)

print(f"\nSum Min-Max elements of set {set(window)}: {sum_min_max_window_result}\n")