class Hero(object):
	def __init__(self, name = "Incongnito"):
		#setup the object to remember its name
		self.name = name
		self.health = 10
		self.power = 5
		self.coins = 50
		self.weapons = []
		self.drinks = 0
		self.inhibitions = 20

	def take_damage(self, amount_of_damage):
		self.health -= amount_of_damage	
	def cheer_for_hero(self):
		print "Fight hard, valiant %s" % self.name	
	def is_alive(self):
		return self.health > 0	
	def check_wallet(self):
		return self.coins 
	def take_potion(self):
		self.health = self.health + 10
		self.coins = self.coins - 5	
	def sobriety_check(self):
		print "You've had %s drink(s). Your inhibitions are %s." % (self.drinks, self.inhibitions)
		if self.inhibitions > 1 :
			print "Miranda is on her way to getting you drunk. BE CAREFUL!"	
		if self.inhibitions <= 0 :
			print "Princess Miranda sees that you are intoxicated.\n'So, should I give you my ex-boyfriend's address?'"	

the_hero = Hero()	