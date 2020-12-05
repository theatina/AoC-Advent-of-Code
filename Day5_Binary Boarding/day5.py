'''

Christina-Theano (Theatina) Kylafi
Advent of Code 2020

Day 5
Part 1 & 2

'''

import numpy as np

input_bpass_list = list(open("./inputDay5.txt","r").read().split("\n"))

rows = 127
row_factors = np.array([ 2**i for i in range(7) ][::-1])

columns = 7
column_factors = np.array([ 2**i for i in range(3) ][::-1])

id_nums = []
seat_dict = {}
for i in range(128):
    seat_dict[i] = []

for passenger in input_bpass_list:

    passenger_data_row = [ i=='B' for i in passenger[:7] ]
    passenger_row = sum(row_factors * passenger_data_row)

    passenger_data_column = [ i=='R' for i in passenger[-3:] ]
    passenger_column = sum(column_factors * passenger_data_column)

    id_of_bpass = passenger_row * 8 + passenger_column
    id_nums.append(id_of_bpass)

    seat_dict[passenger_row].append(passenger_column)

max_id = max(id_nums)

find_my_seat = [ i for i in seat_dict.items() if len(i[1])==7 ][0]
my_row = find_my_seat[0]
my_column= [i for i in range(8) if i not in find_my_seat[1]][0]
my_id_of_bpass = my_row * 8 + my_column

print(f"\nMaximum seat id: {max_id}")
print(f"\nMy seat id: {my_id_of_bpass} (row: {my_row} - column: {my_column})\n")