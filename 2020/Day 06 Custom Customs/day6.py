
import re 

input_answers_list = list(open("./inputDay6.txt","r").read().split("\n\n"))
yes_answers_pt1 = sum( [  len( set("".join(re.split(r"[\ \n]+",i) ))) for i in input_answers_list])
print(yes_answers_pt1)

input_answers_list = [ i.split("\n") for i in input_answers_list  ]
common_quests_pt2 = sum([len(set(i[0]).intersection(*i))  for i in input_answers_list  ])
print(common_quests_pt2)