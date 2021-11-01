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
player_health = int(10)
print("mans health remaining")
man_health = man_health - (first_hit + second_hit)                                                                            # Mans health - Damage (big brain moment)
print(man_health)


receive_dmg = input("The man attaks! Type 'yes' to defend ")                                                                 #man attacks back! 1st time.
if receive_dmg == ("yes"):
    man__dmg = {int(0),int(1), int(2), int(3)} 
numbers_to_select = 1   
list_of_dmg = random.sample(list(receive_dmg), numbers_to_select) 
first_hit = list_of_hits[0] 
second_hit = list_of_hits[1] 
print("Damage Received!")
print(first_hit)
print("HEALTH REMAINING!")
player_health = player_health - (first_hit)
print(player_health)
if player_health <= int(0):
    print("YOU HAVE DIED \n GAME OVER")
    end()
else:
    print("You still stand strong.")

if man_health <= int(0):
    print("you killed the man! And in one hit too? WOW! ")
    end()
else:
    list_of_hits = random.sample(list(iron_sword_potential_special_dmg) , numbers_to_select)
    swing = input("It seeems that one special swing wasn't enough, Want to swing again? ")
    if swing == ("yes"):
        first_hit = list_of_hits[0]
        second_hit = list_of_hits[0]
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
receive_dmg = input("The man attaks! Type 'yes' to defend ")                                                                 #man attacks back! 2nd time.
if receive_dmg == ("yes"):
    man__dmg = {int(0),int(1), int(2), int(3)} 
numbers_to_select = 1   
list_of_dmg = random.sample(list(receive_dmg), numbers_to_select) 
first_hit = list_of_hits[0] 
second_hit = list_of_hits[0] 
print("Damage Received!")
print(first_hit)
print("HEALTH REMAINING!")
player_health = player_health - (first_hit)
print(player_health)

if player_health <= int(0):
    print("YOU HAVE DIED \n GAME OVER")
    end()

else:
    print("You still stand strong.")

swing = input(' "Twas only a scratch! - says the man.. Swing again? " ')

if swing == ("yes"):
        first_hit = list_of_hits[0]
        second_hit = list_of_hits[0]
        print("DAMAGE DONE")
print(first_hit)
print(second_hit)
man_health = man_health - (first_hit + second_hit)
print("Mans health")
if man_health <= int(0):
    print("CONGRATULATION THE MAN IS DEAD")
    end()