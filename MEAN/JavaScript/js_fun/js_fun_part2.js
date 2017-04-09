function sumNums(start,end) {
	var sum  = 0;
	for(var i=start;i<=end;i++) {
		sum += i;
	}
	console.log(sum);
}

function findMin(arr) {
	var min = arr[0];
	for(var i=0;i<arr.length;i++) {
		if (arr[i] < min) {
			min = arr[i];
		}
	}
	return min;
}

function findAvg(arr) {
	var sum = 0;
	for(var i=0;i<arr.length;i++) {
		sum += arr[i];
	}
	var avg = sum / arr.length;
	return avg;
}
//var arr1 = [4,2,0,1];
//console.log(findAvg(arr1));

sumNums = function(x,y) {
	var sum  = 0;
	for(var i=x;i<=y;i++) {
		sum += i;
	}
	console.log(sum);
}

// person = {
// 	name: "Chris",
// 	distance_traveled: 0,
// 	say_name: function() {
// 		console.log(person.name);
// 		return person.name
// 	},
// 	say_something: function(something) {
// 		console.log(person.name + " says " + something);
// 	},
// 	walk: function(){
// 		person.distance_traveled += 3;
// 		console.log(person.say_name() + " is walking")
// 	},
// 	run: function(){
// 		person.distance_traveled += 10;
// 		console.log(person.say_name() + " is running")
// 	},
// 	crawl: function(){
// 		person.distance_traveled += 1;
// 		console.log(person.say_name() + " is crawling")
// 	},
// }

function personConstructor(name) {
	var person = {
					name: name,
					distance_traveled: 0,
					say_name: function() {
						console.log(person.name);
						return person.name
					},
					say_something: function(something) {
						console.log(person.name + " says " + something);
					},
					walk: function(){
						person.distance_traveled += 3;
						console.log(person.say_name() + " is walking")
					},
					run: function(){
						person.distance_traveled += 10;
						console.log(person.say_name() + " is running")
					},
					crawl: function(){
						person.distance_traveled += 1;
						console.log(person.say_name() + " is crawling")
					},
				}
	return person;
}

personConstructor('David');


function NinjaConstructor(name) {
	var ninja = {
		name: name,
		cohort: 'February',
		belt: 'Yellow Belt',
		levelUp: function() {
			if(ninja.belt == 'Yellow Belt') {
				ninja.belt = 'Red Belt';
			} else {
				ninja.belt = 'Black Belt';
			}
			return ninja;
		}
	}
}