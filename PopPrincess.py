from Character import Character

class PopPrincess(Character):
	def __init__(self):
		super(PopPrincess,self).__init__("Miranda", "50", "50")
		self.drinks = 0


	def persuade(other,self):
		self.drinks = self.drinks + 1
		print "'Another round, bartender.' Miranda orders another round."	
		self.inhibitions = self.inhibitions - 5
		print "Without thinking, you agree to another drink."

		
		
	# def persuade_loop(self):
	# 	self.persuade(the_hero)
	# 	print "You agree to another drink"
	# 	print the_hero.sobriety_check()

