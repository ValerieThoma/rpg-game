# print "I am thinking of a number between 1 and 10"
# # print "What is the number?"

# yourNum = int(raw_input(">"));
# myNum = 5;

# while myNum != 5:
# 	print "Try again!"
# 	if (myNum == yourNum): 
# 	print "Yes! You win!"	


# # while myNum : 
# # 	tryAgain = int(raw_input("Try again!"))
# # 	if tryAgain == 5:
# # 		break


# # while myNum:
# # 	myNum != yourNum 
# # 	myNum = False
# # if (myNum == yourNum):
# # 	print "Yes! You win!"				
# # else:
# # 	print "Nope, try again!"
import random 
correct_number = random.randint(1,10);

#print guess 
keep_guessing = True
while keep_guessing == True:
	guess = int(raw_input("Guess a number between 1 - 10\n"))
	if(guess == correct_number):
		print "You Win!"
	else:
		print "Try Again"	
