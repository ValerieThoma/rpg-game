
import os
from Hero import Hero 
from Vampire import Vampire 
from Goblin import Goblin 
from random import randint
#instantiate an object from a hero object from the Hero class
the_hero = Hero()
#ditto
a_goblin = Goblin()
#Make a list to hold all our monsters
monsters = []

print "What is thy name, brave adventurer?"
the_hero.name = raw_input("> ")
the_hero.cheer_for_hero()

print "How many monsters are you willing to fight, brave %s?" % the_hero.name
number_of_enemies = int(raw_input("> "))
for i in range(0, number_of_enemies):
	rand_num = randint(0,1)
	if(rand_num == 1):
		monsters.append(Goblin())
	else:
		monsters.append(Vampire())
print monsters
for monster in monsters:		
	while monster.is_alive() and the_hero.is_alive():
		# os.system("clear") 
		# game is on!
		print "You have %d health and %d power." % (the_hero.health, the_hero.power)
		print "The %s has %d health and %d power." % (monster.name, monster.health, monster.power)
		print "What do you want to do?"
		print "1. fight"
		print "2. do nothing"
		print "3. flee"
		print "> "
		user_input = raw_input()
		if  user_input == "1":
			# a_goblin.health -= the_hero.power 
			#the goblin class should be managing the goblin's health
				monster.take_damage(the_hero.power)
				the_hero.take_damage(monster.power)

		elif user_input == "2":
			# Hero is going to stand there like an idiot
				the_hero.take_damage(monster.power)
		elif user_input == "3":
			print "What! You're leaving? I'm beginning to doubt your commitment to Sparkle Motion."
			#call break to end the while loop
			break		
		else:
			print "Invalid input %s" % user_input	

	    # goblin turn to attack!! (only if he's stil alive")
		if a_goblin.health > 0:
			# the_hero -= goblin_power
			# the_hero.take_damage(a_goblin.power)
			print "The monster hits you for %d damage" % monster.power	
			if the_hero.health <= 0:
				print "Would you like visit Amazon.com and buy some health potions? " 
				consumer_input = raw_input("Y or N > ")	
				if consumer_input == "Y":
					print "Welcome to Amazon! Our healing potion is 5 coins, free shipping\n and same day delivery with Prime."
					if the_hero.check_wallet() >= 5:
						print "Would you like the potion? "
						consumer_input = raw_input("Y or N > ")
						if consumer_input == "Y":						
							the_hero.take_potion()
						if consumer_input == "N":
							print "You have been totally killed dude. That sucks. Hey, I like your jacket. *grabs jacket*"
				if consumer_input == "N":
					print "You have been totally killed dude. That sucks. Hey, I like your jacket. *grabs jacket*"
	
							
					
