# print "Hello, World"
# print("Hello, World")

# print """
# triple
# lines
# print
# """
# name = "valerie";

# #Data types 
# #strings - to read
# #Numbers - digits (- or , or e)
# #floats, integers
# #-- float has a . in integers
# #--integer - has no .
# #Booleans - true or false, 1 or 0, off or on
# #list - list of things. A single variable with a bunch of like parts
# #dictionary - variable of variable
# #objects - we will deal with this later


# name = "Robert" + "Bunch" # + is a concatenate symbol with strings
# first = "Robert" 
# last = "Bunch"
# fullName = first + " " + last
# print first + last
# print fullName
# meaning_of_life = 40 + 2; 
# print meaning_of_life
# #python can not concatenate different data types
# print "-" * 30


# #By argument
# first_name = "Valerie"
# last_name = "Thoma"
# print "Hello {} {}".format(first_name, last_name)
# print "Hello %s" % "Valerie"

# #Floats 
# pi = 3.14
# print type(pi)
# makeMeAnInt = int(pi); #python converts to integer
# print makeMeAnInt
# print type(makeMeAnInt)
# print .2 + .1 #python will round/unlike JavaScript
# #Booleans
# the_truth = True;
# print type(the_truth)

# addOneToMe = 1
# addOneToMe = addOneToMe + 1
# addOneToMe += 1
# addOneToMe += 10

# #Order of operations (PEMDAS)

# #() overrides everything. Use ()
# print "What is your name?"
# name = raw_input(">")


# print "What is your age?"
# age = raw_input(">")
# print "Your age is %d" % int(age)

# # CONDITIONALS 
# # == -compare left and right
# # === -compare left and right AS WELL AS data type
# # 16 == "16" True
# # 16 === "16" False

# if (1 == 2):
# 	print "True"
# elif(2 == 3):
# 	print "Second one is true"	
# else: 
# 	print "False"	

# if (16 == "16"):
# 	print "True"

# classSize = 19;
# question = "How big is your class?";
# print question
# response = raw_input(">")
# #Remember, raw input is always converted as a string
# response_as_an_int	= int(response)
# if(response_as_an_int != classSize):
# 	print "You must not be in the September class."
# else: 
# 	print "Let's learn to code!"

# import this
# print this 

# #Random is a python module, that comes with python.
# import random;
# rand_number = random.randint(1, 10)
# print rand_number

Loops
a while loop, will run fover or until the condition is false. 
keep_going = True
while keep_going
	get_answer = raw_input("Please hit any key")
	keep_going = False 
print "You are no longer in the loop."	