function numbersOnly(arr) {

	var counter = 0;
	var newArray = [];
	
	for(var i=0;i<arr.length;i++) {
		if (typeof(arr[i]) === 'number') {
			newArray[counter] = arr[i];
			counter++;
		}
		
	}

	return newArray;
}

var newArray = numbersOnly([1,"apple",-3,"orange",0.5]);
console.log("numbersOnly function:",newArray);

function removeNonNumbers(arr) {
	for(var i=0;i<arr.length;i++) {
		if (typeof(arr[i]) != 'number') {
			arr.splice(i,1);
		}
	}
	return arr;
}

console.log("removeNonNumbers function:",removeNonNumbers([1,"apple",-3,"orange",0.5]));



