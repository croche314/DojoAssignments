var students = [
	{first_name: 'Michael', last_name : 'Jordan'},
	{first_name: 'John', last_name : 'Rosales'},
	{first_name: 'Mark', last_name : 'Guillen'},
	{first_name: 'KB', last_name : 'Tonel'}
];

var users = {
	'Students' : [
		{first_name: 'Michael', last_name : 'Jordan'},
		{first_name: 'John', last_name : 'Rosales'},
		{first_name: 'Mark', last_name : 'Guillen'},
		{first_name: 'KB', last_name : 'Tonel'}
	],
	'Instructors': [
		{first_name: 'Michael', last_name : 'Choi'},
		{first_name: 'Martin', last_name : 'Puryear'}
	]
};

function printNames(arr) {
	for(var i=0;i<arr.length;i++) {
		console.log(arr[i].first_name, arr[i].last_name);
	}
}

function printUsers(users) {
	var counter = 1;

	for(user in users) {
		console.log(user);
		var arr = users[user];
		for(var i=0;i<arr.length;i++) {
			var name = (arr[i].first_name + " " + arr[i].last_name).toUpperCase();
			var nameLength = name.length;
			console.log(counter,"-",name,"-",nameLength);
			counter++;
		}
	}
}

console.log("Part One:");
printNames(students);

console.log("Part Two:");
printUsers(users);