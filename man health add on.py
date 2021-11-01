import random
from typing import MutableSequence
swing = input("There is a evil lookin dude standing in front of you, do you wish to swing your iron sword at him? ")
if swing == ("yes"):
    iron_sword_potential_special_dmg = {int(0),int(1), int(2), int(3), int(4), int(5)} 
numbers_to_select = 2   
list_of_hits = random.sample(list(iron_sword_potential_special_dmg), numbers_to_select) 
first_hit = list_of_hits[0] 
second_hit = list_of_hits[1] 
print("DAMAGE DONE!")
print(first_hit)
print(second_hit)

man_health = int(10)                                                                                                        #MANS INITIAL HEALTH
player_health = int(10)                                                                                                     #Players Health
man_health = man_health - (first_hit + second_hit)                                                                          # Mans health - Damage (big brain moment)

print("mans health remaining")
print(man_health)

if man_health <= int(0):
    print("you killed the man! And in one hit too? WOW! ")
    end()
else:
    list_of_hits = random.sample(list(iron_sword_potential_special_dmg) , numbers_to_select)
    swing = input("It seeems that one special swing wasn't enough, Want to swing again? ")
    if swing == ("yes"):
        first_hit = list_of_hits[0]
        second_hit = list_of_hits[1]
print("DAMAGE DONE")
print(first_hit)
print(second_hit)
man_health = man_health - (first_hit + second_hit)
print("Mans health")
print(man_health)
if man_health <= int(0):
    print(" CONGRATULATIONS THE MAN IS DEAD")
    end()
else:list_of_hits = random.sample(list(iron_sword_potential_special_dmg) , numbers_to_select)
swing = input(' "Twas only a scratch! - says the man.. swing again?" ')
if swing == ("yes"):
        first_hit = list_of_hits[0]
        second_hit = list_of_hits[1]
        print("DAMAGE DONE")
print(first_hit)
print(second_hit)
man_health = man_health - (first_hit + second_hit)
print("Mans health")
if man_health <= int(0):
    print("CONGRATULATION THE MAN IS DEAD")
    end()

