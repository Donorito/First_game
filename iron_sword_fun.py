import random
swing = input("There is a evil lookin dude standing in front of you, do you wish to swing your iron sword at him? ")
if swing == ("yes"):
    iron_sword_potential_special_dmg = {"0","1", "2", "3", "4", "5"} 
numbers_to_select = 2   
list_of_hits = random.sample(iron_sword_potential_special_dmg, numbers_to_select) 
first_hit = list_of_hits[0] 
second_hit = list_of_hits[1] 
print(first_hit)
print(second_hit)


