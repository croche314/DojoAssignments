# Part One
'''students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

for student in students:
	print student['first_name'], student['last_name']
'''

# Part Two
users = {
	'Students': [
		{'first_name': 'Michael', 'last_name': 'Jordan'},
		{'first_name': 'John', 'last_name': 'Rosales'},
		{'first_name': 'Mark', 'last_name': 'Guillen'},
		{'first_name': 'KB', 'last_name': 'Tonel'}
	],
	'Instructors': [
		{'first_name': 'Michael', 'last_name': 'Choi'},
		{'first_name': 'Martin', 'last_name': 'Puryear'}
	]
}



for key, user in users.items():
	counter = 1
	print key
	for name in user:
		length = len(name['first_name'] + name['last_name'])
		print counter, "-", name['first_name'].upper(), name['last_name'].upper(), "-", length
		counter += 1





	
