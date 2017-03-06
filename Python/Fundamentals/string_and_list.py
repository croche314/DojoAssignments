# Find and Replace
'''
str1 = "If monkeys like bananas, then I must be a monkey!"
print str1.find("monkey")
str2 = str1.replace("monkey","alligator")
print str2
'''
# Min and Max
'''
x = [2,54,-2,7,12,98]
print min(x)
print max(x)
'''

# First and Last
'''
x = ["hello",2,54,-2,7,12,98,"world"]
print x.pop(-1)
print x.pop(0)
print x[0:-1]
'''

# New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
# [-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]
length = len(x)
y = x[0:length / 2]
x[0:length/2] = []
x.insert(0,y)
print x