#1. INclude pygame
import pygame
#from the math module (built into python), get the fabs method
from math import fabs, hypot 
#2. Init pygame
from random import randint 
import time
#in order to use pygame, we have to run the init method
pygame.init()
#3. Create a screen with a particular size
#the screen size MUST be a tuple!
screen_size = (512,480)
#Actually tell pygame to set the screen up and store it
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Grab 'em by the Equal Pay")
#set up a variable with our image
background_image = pygame.image.load('space.png')
hero_image = pygame.image.load('ww_hero.png')
goblin_image = pygame.image.load('that_paper.png')
monster_image = pygame.image.load('bad_donnie.png')
win_music =  'girls.wav'
lose_music = 'grab.wav'
game_music = 'game_music_loop.wav'

#Make a font so we can write o n the screen
 
#8 Set up the hero location
hero = {
	"x": 100,
	"y": 100,
	"speed": 15,
	"wins": 0,
	"lives": ""
}

goblin = {
	"x": 125,
	"y": 125,
	"speed": 4,
	"dx": 1,
	"dy": 1
	
}

monster = {
	"x": 200,
	"y": 200,
	"speed": 2
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


#Keep characters returning to screen! 
def keepOnScreen(self):
	if self["y"] < 0:
		self["y"] = 440
	elif self["y"] > 440:
		self["y"] = 0
	if self["x"] < 0:
		self["x"] = 472
	elif self["x"] > 472:
		self["x"] = 0	


#4. Create a game loop (while)
#Create a boolean for whether the game should be going or not
game_on = True
pygame.mixer.init()
pygame.mixer.music.load(game_music)
pygame.mixer.music.play(-1)
tick = 0  
while game_on:
	tick += 1
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

		#move the bad guy
	dx = monster["x"] - hero["x"] #the change in x (delta x)
	dy = monster["y"] - hero["y"] #the change in y (delt y)
	dist = hypot(dx,dy)		#declare dist 
	dx = dx / dist
	dy = dy / dist
	monster["x"] -= dx * monster["speed"]
	monster["y"] -= dy * monster["speed"]

	if tick % 20 == 0:
		#change directions
		goblin["dx"] = randint(-1,1)
		goblin["dy"] = randint(-1,1)

	goblin["x"] += goblin["dx"] * goblin["speed"]
	goblin["y"] += goblin["dy"] * goblin["speed"]	
	 
		# COLLISION DETECTION !!
	distance_between = fabs(hero["x"] - goblin ["x"]) + fabs(hero["y"] - goblin["y"])
	if distance_between < 32:
		pygame.mixer.init()
		pygame.mixer.music.load(win_music)
		pygame.mixer.music.play(1)
	 	hero["wins"] += 1
	 	hero["lives"] = "Nevertheless, she persisted"
	
		
	death_distance = fabs(hero["x"] - monster["x"]) + fabs(hero["y"] - monster["y"])	 
	if  death_distance < 32:
		pygame.mixer.init()
		pygame.mixer.music.load(lose_music)
		pygame.mixer.music.play(1)	
		hero["lives"] = "The Patriarch Wins!"
	
	keepOnScreen(hero)
	keepOnScreen(goblin)
	keepOnScreen(monster)	 
	 	 
	

#6. Fill in the screen with a color (or image)
# blit takes 2 arguments...
# 1. what do you want to draw?
# 2. Where do you want to draw it?
	pygame_screen.blit(background_image, [0,0])
	font = pygame.font.Font(None, 25)
	wins_text = font.render("Wins: %d" % (hero["wins"]), True, (255,255,255))
	bigFont = pygame.font.Font(None, 40)	
	kill_text = bigFont.render("%s" % (hero["lives"]), True, (255,255,255))
	pygame_screen.blit(wins_text, [40,40])
	pygame_screen.blit(kill_text, [55,200])
	pygame_screen.blit(hero_image, [hero["x"], hero["y"]])
	pygame_screen.blit(goblin_image, [goblin["x"], goblin["y"]])
	pygame_screen.blit(monster_image, [monster["x"], monster["y"]])
#7. Repeat 6 over and over and over....
	pygame.display.flip() #clear the screen out and draw it again