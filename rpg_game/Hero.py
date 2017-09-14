class Hero(object):
	def __init__(self, name = "Incongnito"):
		#setup the object to remember its name
		self.name = name
		self.health = 10
		self.power = 5
		self.coins = 50
		self.weapons = []

	def take_damage(self, amount_of_damage):
		self.health -= amount_of_damage	
	def cheer_for_hero(self):
		print "Fight hard, valiant %s" % self.name	
	def is_alive(self):
		return self.health > 0	
	def check_wallet(self):
		return self.coins 
	def take_potion(self):
		self.health = self.health + 5
		self.coins = self.coins - 5	

the_hero = Hero()	