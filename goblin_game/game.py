#1. INclude pygame
import pygame
#from the math module (built into python), get the fabs method
from math import fabs 
#2. Init pygame
#in order to use pygame, we have to run the init method
pygame.init()
#3. Create a screen with a particular size
#the screen size MUST be a tuple!
screen_size = (512,480)
#Actually tell pygame to set the screen up and store it
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Chase")
#set up a variable with our image
background_image = pygame.image.load('background.png')
hero_image = pygame.image.load('hero.png')
goblin_image = pygame.image.load('goblin.png')
#Make a font so we can write on the screen

 
#8 Set up the hero location
hero = {
	"x": 100,
	"y": 100,
	"speed": 20,
	"wins": 0
}

goblin = {
	"x": 200,
	"y": 200,
	"speed": 15
}
keys = {
	"up": 273,
	"down": 274,
	"right": 275,
	"left": 276
}

keys_down = {
	"up": False,
	"down": False,
	"left": False,
	"right": False
}
#4. Create a game loop (whie)
#Create a boolean for whether the game should be going or not
game_on = True
while game_on:
	#we are inside the main game loop.
	# it will keep running, as long as our bool is true 
	#5. Add a quit event (Python needs and escape)
	# Pygame comes with an event loop! (sort of like JS)
	for event in pygame.event.get():
		if (event.type == pygame.QUIT):
			#the user clicked the red x in the top left
			game_on = False
		elif event.type == pygame.KEYDOWN:
			if event.key == keys["up"]:
				# hero ["y"] -= hero["speed"]
				keys_down["up"] = True
			elif event.key == keys["down"]:
				# hero ["y"] += hero["speed"]
				keys_down["down"] = True
			elif event.key == keys["left"]:
				# hero ["x"] -= hero["speed"]
				keys_down["left"] = True
			elif event.key == keys["right"]:
				# hero ["x"] += hero["speed"]
				keys_down["right"] = True
		elif event.type == pygame.KEYUP:		
			if event.key == keys["up"]:
					keys_down["up"] = False	
			if event.key == keys["down"]:
					keys_down["down"] = False	
			if event.key == keys["left"]:
					keys_down["left"] = False	
			if event.key == keys["right"]:
					keys_down["right"] = False					
	if keys_down["up"]:
		hero ["y"] -= hero["speed"]
	elif keys_down["down"]:
		hero["y"] += hero["speed"]
	if keys_down["left"]:
		hero ["x"] -= hero["speed"]
	elif keys_down["right"]:
		hero["x"] += hero["speed"]	

		#COLLISION DETECTION !!
	distance_between = fabs(hero["x"] - goblin ["x"]) + fabs(hero["y"] - goblin["y"])
	# if distance_between < 32:
	#  	print "collision"
	# else:
	#  	print "not touching"

#6. Fill in the screen with a color (or image)
# blit takes 2 arguments...
# 1. what do you want to draw?
# 2. Where do you want to draw it?
	pygame_screen.blit(background_image, [0,0])
	font = pygame.font.Font(None, 25)
	wins_text = font.render("Wins: %d" % (hero["wins"]), True, (0,0,0))	
	pygame_screen.blit(wins_text, [40,40])
	pygame_screen.blit(hero_image, [hero["x"], hero["y"]])
	pygame_screen.blit(goblin_image, [goblin["x"], goblin["y"]])
#7. Repeat 6 over and over and over....
	pygame.display.flip() #clear the screen out and draw it again