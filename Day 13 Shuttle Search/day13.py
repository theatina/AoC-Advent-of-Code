'''

Christina-Theano (Theatina) Kylafi
Advent of Code 2020

Day 13
Part 1 

'''

input_file = [ i for i in list(open("./inputDay13.txt","r").read().split("\n")) ]
# print(input_file)
time = int(input_file[0])
buses = [  int(i) for i in input_file[1].split(",") if i !="x"  ]
# print(buses)

found = False
counter = 0
while found==False:
    temp_time = time+counter
    for i in buses:
        if temp_time%i==0:
            print(f"\nTime: {temp_time} -> bus: {i} -> waiting time: {temp_time-time} -> mult_prod: {(temp_time-time)*i}\n")
            found = True
            break
    
    counter+=1

