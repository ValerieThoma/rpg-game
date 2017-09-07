# 5. Work or Sleep In? 
#if Sun-Sat is set equal to 0 - 6
today = int(raw_input("Pick a number between 0 and 6: "))

if (today == 0 or today == 6):
	print "Sleep, sweet child!"
else:
	print "You better go to work!"