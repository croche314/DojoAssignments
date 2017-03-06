def odd_even():
	for i in range(1,2001):
		if i % 2 == 0:
			x = "even"
		else:
			x = "odd"
		print  "Number is " + str(i) + ". This is an " + x + " number."

#odd_even()

a = [2,4,10,16]

def multiply(my_list,multiplier):
	for index,n in enumerate(my_list):
		my_list[index] = n * multiplier
	return my_list

# print multiply(a,5)

b = [2,4,5]
# [6,12,15]

def layered_multiples(arr):
	answer = []

	for z in arr:
		print "z: " + str(z)
		newArr = []
		for r in range(0,z):
			newArr.append(1)
		answer.append(newArr)
	return answer

x = layered_multiples(multiply([2,4,5],3))
print x
