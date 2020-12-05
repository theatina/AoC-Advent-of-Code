'''

Christina-Theano (Theatina) Kylafi
Advent of Code 2020

Day 2
Part 1

'''

input_passwords_list = list(open("./inputDay2.txt","r").read().split("\n"))
input_passwords_list = [i.split(" ") for i in input_passwords_list if i!="" ]

valid_passwords = 0
counter = 0
for i in input_passwords_list:
    letter = i[1][:-1]
    count_occs_of_letter = i[2].count(letter)
    min_max_occs = i[0].split("-")
    if (count_occs_of_letter > int(min_max_occs[1])) or (count_occs_of_letter < int(min_max_occs[0])):
        # print(f"\n{counter}. Password: { i[2] } is invalid ({i})")
        pass
    else:
        # print(f"\n{counter}. Password: { i[2] } is valid ({i})")
        valid_passwords+=1
    counter+=1
        
print(f"\nValid passwords: {valid_passwords}\n")
