def count_shiny_bags(bag):
    value_list = bag_dict[bag]
    
    if value_list==None:
        return 0

    sum_bags = 0
    for i in value_list:

        counter = count_shiny_bags(i[1])
        if counter==0:
            sum_bags+=int(i[0])
        elif counter!=1:
            sum_bags+=int(i[0])*counter + int(i[0])
        else:
            sum_bags+=int(i[0])*counter

    return sum_bags

def create_bag_dict(input_list):
    bag_dict = {}
    for i in input_list:
        tokens = i.split(" ")
        if "no" in tokens:
            value = None
        else:
            value =  (" ".join(tokens[4:]).split(",")) 
            temp_value = [ i.split() for i in value ]
            value = [ (i[0]," ".join(i[1:3])) for i in temp_value ]

        bag_dict[" ".join(tokens[:2])] = value
    
    return bag_dict 

def bag_colours_counter(input_list):
    bags_to_check = ["shiny gold"]
    bags_to_keep = []
    while (len(bags_to_check)!=0):
        for j in bags_to_check:
            for i in input_list:    
                if j in i[4:]:
                    bag = " ".join(i.split(" ")[:2])
                    bags_to_check.append(bag)
                    bags_to_keep.append(bag)
            bags_to_check.remove(j)

    return len(list(set(bags_to_keep)))

input_list = list(open("./inputDay7.txt","r").read().split(".\n"))

bags = bag_colours_counter(input_list)
print(f"\nDay 7 Part 1: {bags} bags") 

bag_dict = create_bag_dict(input_list)
bags = count_shiny_bags("shiny gold")
print(f"\nDay 7 Part 2: {bags} bags\n") 
