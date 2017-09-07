# 8 Tip Calculator 2
# There is a special place in hell for bad tippers
bill = int(raw_input("What is the total of your bill?\n>"))
service_rating = raw_input("Was the service: 'Good', 'Fair', or 'Poor'?\n>")
service = service_rating.upper()
guests = int(raw_input("How many ways would you like your check split?\n>"))
if (service == "GOOD"):
	tip = .30 * bill
 	print "Come back soon!"
elif (service == "FAIR"):
	tip = .20 * bill
 	print "We'll try harder next time."
else:  	
	tip = .15 * bill
	print "Sorry you had such a miserable time #notsorry."	
print "That will be $ " "{:.2f}".format((bill + tip) / guests)
print "Thank you so much!"