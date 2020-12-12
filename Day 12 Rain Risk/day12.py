'''

Christina-Theano (Theatina) Kylafi
Advent of Code 2020

Day 12
Part 1 

'''

def move_transcription(moves):
    compass = ['E','S','W','N']
    rotation_moves = ['R', 'L']
    direction_moves = ['F']
    direction_moves.extend(compass)
    map_moves = []

    moving_direction = ['E']
    steps = [0]
    facing_direction = ['E']

    for i in moves:
        if i[0] in compass:
            moving_direction.append(i[0])
            steps.append(i[1])
            facing_direction.append(facing_direction[-1])
        elif i[0]=="F":
            moving_direction.append(facing_direction[-1])
            steps.append(i[1])
            facing_direction.append(facing_direction[-1])
        elif i[0] in rotation_moves:
            if i[0]=="R":
                new_direction = compass[ (compass.index(facing_direction[-1])+i[1]//90)%4 ]
            elif  i[0]=="L":
                new_direction = compass[ (compass.index(facing_direction[-1])-i[1]//90)%4 ]

            moving_direction.append(new_direction)
            steps.append(0)
            facing_direction.append(new_direction)

    return moving_direction,steps,facing_direction

def ship_coords(moving_direction,steps,facing_direction):
    
    north_south_coords = [ +steps[i] if moving_direction[i]=="N" else -steps[i] if moving_direction[i]=="S" else 0 for i in range(len(moving_direction))  ]
    east_west_coords = [ +steps[i] if moving_direction[i]=="E" else -steps[i] if moving_direction[i]=="W" else 0 for i in range(len(moving_direction))  ]
    map_moves = [ sum(north_south_coords), sum(east_west_coords) ]

    return map_moves

def manhattan(coordinates):
    return sum([abs(i) for i in coordinates])

moves = [ i for i in list(open("./inputDay12.txt","r").read().split("\n")) ]
moves = [ [i[0],int(i[1:])] for i in moves ]

moving_direction,steps,facing_direction = move_transcription(moves)
coordinates = ship_coords(moving_direction,steps,facing_direction)
manh_dist = manhattan(coordinates)

print(f"\nManhattan distance between that location and the ship's starting position: {manh_dist} \n")

