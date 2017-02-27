var array = ["James", "Jill", "Jack", "Jane"];

var sepChar = prompt("Enter a character separator: ");

function fancyArray (arr, separator, reversed) {
	
	if (reversed) {
		for(var i=arr.length-1;i>=0;i--) {
			console.log(i, " ", separator," ", arr[i]);
		}
	} else {
		for(i=0;i<arr.length;i++) {
			console.log(i, " ", separator," ", arr[i]);
		}
	}

	
}

fancyArray(array, sepChar, true);

for(var i=0;i<arr.length;i++) {
	console.log(arr[i]);
	log
}