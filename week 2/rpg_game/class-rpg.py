
import os
from Hero import Hero 
from Vampire import Vampire 
from Goblin import Goblin 
from random import randint
from PopPrincess import PopPrincess
#instantiate an object from a hero object from the Hero class
the_hero = Hero()
#ditto
a_goblin = Goblin()
miranda = PopPrincess()
#Make a list to hold all our monsters
monsters = []

print "What is thy name, brave adventurer?"
the_hero.name = raw_input("> ")
the_hero.cheer_for_hero()

print "How many monsters are you willing to fight, brave %s?" % the_hero.name.upper()
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
			break
			#call break to end the while loop
		elif monster.health <= 0:	
				print "Well, GAME OVER. Too bad, Princess Miranda was asking about you."		
		else:
			print "Invalid input %s" % user_input	

		# goblin turn to attack!! (only if he's stil alive")
		# if monster.is_alive():
		# 	# the_hero -= goblin_power
		# 	# the_hero.take_damage(a_goblin.power)
		# 	print "The monster hits you for %d damage" % monster.power	
		if the_hero.health <= 0:
			print "Would you like visit Amazon.com and buy some health potions? " 
			consumer_input = raw_input("Y or N > ")	
			if consumer_input == "Y":
				f = open("store_art.txt", "r")
				message = f.read()
				print (message)  
				print "Welcome to Amazon! Our healing potion is 5 coins, free shipping\nand same day delivery with PRIME."
				if the_hero.check_wallet() >= 5:
					print "Would you like the potion? "
					consumer_input = raw_input("Y or N > ")
					if consumer_input == "Y":						
						the_hero.take_potion()
						print "Hooray! You live to fight another day."
					if consumer_input == "N":
						print "You have been totally killed, dude. That sucks."
			if consumer_input == "N":
				print "You have been totally killed dude. That sucks."
				print "Want to join me in the after life for a beer?"
				mortal_input = raw_input("Y or N > ")
				if mortal_input == "Y":
					f = open("pub.txt", "r")
					message = f.read()
					print (message)
					print "You hear a soft voice behind you."
					# os.system("say") 
					print "'Hello, you look like you could use a drink. May I buy you one?'"
					print "It is Princess Miranda. Do you accept?"
					flirt_input = raw_input("Y or N > ")
					if flirt_input == "Y":
						f = open("princess.txt", "r")
						message = f.read()
						print (message)
						print "Princess Miranda tells you about her creepy\nex-boyfriend who 'followed' (read: stalked) her into the afterlife.\nShe's nervous. She mixes her words, but you understand\nimplicitly---she wants you to fight him."
						print "You have %s inhibitions. Princess Miranda offers you another drink." % the_hero.inhibitions
						another_drink = raw_input("Do you accept? One drink will lower your inhibitions by 5. Y or N > ")
						if another_drink == "Y":
							miranda.persuade(the_hero)
							the_hero.sobriety_check()
							while the_hero.inhibitions > 0:
								miranda.persuade(the_hero)
								the_hero.sobriety_check()
								if the_hero.inhibitions <= 0:
									# print "Princess Miranda sees that you are intoxicated.\nSo, should I give you my ex-boyfriend's address?"
									drunk_fight = raw_input("Do you take his address? Y or N > ")
									if drunk_fight == "Y":
										print "You %s are either very brave, very stupid, or very drunk." % the_hero.name.upper()
										print "You agree that you are 'all of the above' and head out to fight this fathead."
										f = open("journey.txt", "r")
										message = f.read()
										print (message)
										print "TO BE CONTINUED ..."
									if drunk_fight == "N":
										f = open("heart_breaker.txt", "r")
										message = f.read()
										print (message)
										print "Your decision may hurt Princess Miranda's\nfeeling's now, but I think you've made\na reasonable choice. Get some sleep, hero."
										print "GAME OVER!"
						if another_drink == "N":
							print "Our valient hero %s, lived a good life, fought a good fight, but then rejected\nthis kind Princesses' offer in the afterlife.\nWhat a waste. GAME OVER!"	% the_hero.name.upper()					
					if flirt_input == "N":
						print "That's pretty lame, dude. What?\nDo you have WORK tomrrow? NO, you're dead!\nBut actually, if you're in the program, then that's cool.\n'Keep coming back, it works if you work it.'\n"
						print "Also, GAME OVER! But we're really proud of you! Thank you for your sacrifice in the war against MONSTERS."
				if mortal_input == "N":
					print "Well, GAME OVER. Too bad, Princess Miranda was asking about you."
					


							
					
