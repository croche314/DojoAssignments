import random

def generateGrade(num_scores):
	print "Scores and Grades"
	print "-----------------"
	for x in range(num_scores + 1):
		random_num = random.random()
		score = int(round(random_num * 40 + 60))
		if score >= 90:
			grade = "A!"
		elif score >= 80:
			grade = "B"
		elif score >= 70:
			grade = "C"
		else:
			grade = "D :-("
		print "Score: " + str(score) + "; Your grade is " + grade
	print "Apparently there are is no such thing as F anymore. Bye!"

generateGrade(10)