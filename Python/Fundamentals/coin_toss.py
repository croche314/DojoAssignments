import random

def coinToss(throws):
	heads_count = 0
	tails_count = 0
	for count in range(1,throws+1):
		num = round(random.random())
		if num < 1:
			result = "head"
			heads_count+=1
		else:
			result = "tail"
			tails_count+=1
		print "Attempt #" + str(count) + ": Throwing a coin... It's a " + str(result) + "! ... Got " + str(heads_count) + " head(s) so far and " + str(tails_count) + " tail(s) so far"
	print "Ending the program, thank you!"
	return heads_count

x = coinToss(10)
success = 0
tries = 0
nope = 0
countArr = []

for i in range(1,11):
	print "x = " + str(x)
	print "i = " + str(i)

	while x >= 4 and x <= 6:
		tries += 1
		x = coinToss(10)
	tries += 1	
	success += 1
	print "Got " + str(x) + "! in " + str(tries) + " tries"
	countArr.append(x)
	x = coinToss(10)

print str(countArr)
