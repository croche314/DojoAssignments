# Multiples
'''
for x in range(1,1000,2):
	print x

for i in range(5,1000000,5):
	print i
'''

# Sum List
a = [1,2,5,10,255,3]
sum = 0
for num in a:
	sum += num
print "sum: " + str(sum)

# Average List
length = len(a)
avg = sum / length
print "average: " + str(avg)