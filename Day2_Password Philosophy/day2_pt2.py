'''

Christina-Theano (Theatina) Kylafi
Advent of Code 2020

Day 2
Part 2

'''

input_passwords_list = list(open("./inputDay2.txt","r").read().split("\n"))
input_passwords_list = [i.split(" ") for i in input_passwords_list if i!="" ]

valid_passwords = 0
counter = 0
for i in input_passwords_list:
    letter = i[1][:-1]
    positions_occs = i[0].split("-")
    positions_occs = [int(i)-1 for i in positions_occs]
    pos_occs_of_letter = [k for k,j in enumerate(i[2]) if j==letter]
    if set(positions_occs).issubset(pos_occs_of_letter) or (positions_occs[0] not in pos_occs_of_letter and positions_occs[1] not in pos_occs_of_letter):
        # print(f"\n{counter}. Password: { i[2] } is invalid ({i})")
        pass
    else:
        # print(f"\n{counter}. Password: { i[2] } is valid ({i})")
        valid_passwords+=1
    counter+=1
        
print(f"\nValid passwords: {valid_passwords}\n")
