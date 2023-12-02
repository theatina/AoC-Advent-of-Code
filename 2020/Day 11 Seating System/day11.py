'''

Christina-Theano (Theatina) Kylafi
Advent of Code 2020

Day 11
Part 1 

'''

def seats_map(seats):
    for i in seats:
        print(i)

def check_adjs(seats, seat_row, seat_col, seats_rows, seats_cols):

    valid_rows = [ i for i in range(seats_rows) ]
    valid_cols = [ i for i in range(seats_cols) ]

    occupied_adjs = [ (row,col) for row in range(seat_row-1,seat_row+2) for col in range(seat_col-1,seat_col+2) if row in valid_rows and col in valid_cols and seats[row][col]=="#" ]

    if (seat_row,seat_col) in occupied_adjs:
        occupied_adjs.remove((seat_row,seat_col))

    occupied_adjs = len(occupied_adjs)

    return occupied_adjs

seats_info= {}
def update_seats_info(current_state):
    global seats_info

    for row in range(len(current_state)):
        for col in range(len(current_state[0])):
            value = current_state[row][col]
            occupied_adj = check_adjs(current_state,row,col,len(current_state),len(current_state[0]))
            seats_info[(row,col)] = [value,occupied_adj]

def create_next_state(current_state,seats_info):
    new_state = [ "".join([ "#" if seats_info[(i,j)][0]=="L" and seats_info[(i,j)][1]==0 else "L" if seats_info[(i,j)][0]=="#" and seats_info[(i,j)][1]>=4  else seats_info[(i,j)][0] for j in range(len(seats[0])) ]) for  i in range(len(seats)) ] 

    return new_state

def count_occupied(seats_state):
    occ_seats = len([ 1 for i in "".join(seats_state) if i=="#" ])
    return occ_seats

seats = [ i for i in list(open("./inputDay11.txt","r").read().split("\n")) ]
update_seats_info(seats)
# seats_map(seats)

prev_state = seats.copy()
new_state = seats.copy()
one_more_please = True
rounds = 0
while one_more_please:
    rounds+=1
    print(f"\nROUND: {rounds}\n")
    prev_state = new_state
    new_state = create_next_state(new_state,seats_info)
    update_seats_info(new_state)
    # seats_map(new_state)
    if prev_state==new_state:
        one_more_please=False

final_occupied = count_occupied(new_state)

print(f"\nOccupied seats: {final_occupied} (round {rounds})\n")

