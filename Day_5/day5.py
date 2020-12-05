'''

Christina-Theano (Theatina) Kylafi
Advent of Code 2020

Day 5
Part 1 & 2

'''

import numpy as np

input_bpass_list = list(open("./inputDay5.txt","r").read().split("\n"))

rows = 127
row_factors = []
row_factors.append(int(np.ceil(rows/2)))
for i in range(1,7):
    row_pos_temp = int(np.ceil(row_factors[i-1]/2))
    row_factors.append(row_pos_temp)

columns = 7
column_factors = []
column_factors.append(int(np.ceil(columns/2)))
for i in range(1,3):
    column_pos_temp = int(np.ceil(column_factors[i-1]/2))
    column_factors.append(column_pos_temp)

max_id = -1
seat_dict = {}
for i in range(128):
    seat_dict[i] = []

for passenger in input_bpass_list:

    passenger_row = 0
    for row_factor,passenger_data in zip(row_factors,passenger):
        passenger_row+= row_factor*(passenger_data=='B')

    passenger_column = 0
    for column_factor,passenger_data in zip(column_factors,passenger[-3::]):
        passenger_column+= column_factor*(passenger_data=='R')

    id_of_bpass = passenger_row * 8 + passenger_column

    if id_of_bpass > max_id:
        max_id = id_of_bpass

    seat_dict[passenger_row].append(passenger_column)

for i in seat_dict:
    if len(seat_dict[i]) == 7:
        my_row = i
        for j in range(8):
            if j not in seat_dict[i]:
                my_column = j
                my_id_of_bpass = my_row * 8 + my_column
                break

print(f"\nMaximum seat id: {max_id}")
print(f"\nMy seat id: {my_id_of_bpass} (row: {my_row} - column: {my_column})\n")
