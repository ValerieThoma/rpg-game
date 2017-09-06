print "Hello, World"
print("Hello, World")

print """
triple
lines
print
"""
name = "valerie";

#Data types 
#strings - to read
#Numbers - digits (- or , or e)
#floats, integers
#-- float has a . in integers
#--integer - has no .
#Booleans - true or false, 1 or 0, off or on
#list - list of things. A single variable with a bunch of like parts
#dictionary - variable of variable
#objects - we will deal with this later


name = "Robert" + "Bunch" # + is a concatenate symbol with strings
first = "Robert" 
last = "Bunch"
fullName = first + " " + last
print first + last
print fullName
meaning_of_life = 40 + 2; 
print meaning_of_life
#python can not concatenate different data types
print "-" * 30


#By argument
first_name = "Valerie"
last_name = "Thoma"
print "Hello {} {}".format(first_name, last_name)
print "Hello %s" % "Valerie"

#Floats 
pi = 3.14
print type(pi)
makeMeAnInt = int(pi); #python converts to integer
print makeMeAnInt
print type(makeMeAnInt)
print .2 + .1 #python will round/unlike JavaScript
#Booleans
the_truth = True;
print type(the_truth)

addOneToMe = 1
addOneToMe = addOneToMe + 1
addOneToMe += 1
addOneToMe += 10

#Order of operations (PEMDAS)

#() overrides everything. Use ()

name = raw_input("What is your name?")
