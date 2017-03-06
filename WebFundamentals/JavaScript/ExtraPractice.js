/**********************
var student = {
	name: "David Rayy",
	sclass: "VI",
	rollno: 12
};


// 1
for(step in student) {
	console.log(step);
}


// 2
delete student.rollno;

for(step in student) {
	console.log(step);
}


// 3
console.log(student.name.length);


var library = [
	{
		author: 'Bill Gates',
		title: 'The Road Ahead',
		readingStatus: true

	},
	{
		author: 'Steve Jobs',
		title: 'Walter Isaacson',
		readingStatus: true
	},
	{
		author: 'Suzanne Collins',
		title: 'Mockingjay: The Final Book of the Hunger Games',
		readingStatus: false
	}
];


// 4
for(var i=0;i<library.length;i++) {
	var obj = library[i];
	for(step in obj) {
		console.log(step,"->",obj[step]);
	}
}

// 5
var arr = [6,4,0,3,-2,1];

function sortArray(array) {
	var newArray = [];
	var counter = 0;
	var length = array.length;
	for(var i=0;i<length;i++) {
		// find the lowest number
		min = findMinimum(array);
		// add it to the new array
		newArray[counter] = min;
		counter++;
		//delete it from old array
		for(var j=0;j<array.length;j++) {
			if (array[j] == min) {
				array.splice(j,1);
			}
		}
	}
	


	return newArray;
} // sortArray

function findMinimum(array) {
	var min = array[0];
	for(var i=0;i<array.length;i++) {
		if (array[i] < min) {
			min = array[i];
		}
	}
	return min;
} // findMinimum

console.log(sortArray(arr));
console.log(arr);
i = 1
min = 4
newArray = []

*********************/

// 10
var library = [ 
   {
       title:  'The Road Ahead',
       author: 'Bill Gates',
       libraryID: 1254
   },
   {
       title: 'Walter Isaacson',
       author: 'Steve Jobs',
       libraryID: 4264
   },
   {
       title: 'Mockingjay: The Final Book of The Hunger Games',
       author: 'Suzanne Collins',
       libraryID: 3245
   }];

var sortedLibrary = [];

for(var i=0;i<library.length;i++) {
	sortedLibrary[i].author = library[i].author;
	sortedLibrary[i].libraryID = library[i].libraryID;
	sortedLibrary[i].title = library[i].title;
}

console.log(sortedLibrary);