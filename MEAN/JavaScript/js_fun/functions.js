// function runningLogger() {
// 	console.log("I am running!");
// }

// function multiplyByTen(num) {
// 	return num * 10;
// }

// console.log(multiplyByTen(5));

// function stringReturnOne() {
// 	return "String One!";
// }

// function stringReturnTwo() {
// 	return "String Two!";
// }

// function caller(x) {
// 	if (typeof x === 'function') {
// 		x();
// 	}
// }

function myDoubleConsoleLog(x,y) {
	if (typeof x === 'function') {
		console.log(x());
	}
	if (typeof y === 'function') {
		console.log(y());
	}
}

function caller2(x) {
	console.log('starting');
	setTimeout(function() {
		if (x === 'function') {
			x();
		}
	}, 2000);
	console.log('ending?');
	return 'interesting';
}
caller2(myDoubleConsoleLog);