var HOUR = 8;
var MINUTE = 50;
var PERIOD = "AM";
var string = "It's ";

if (MINUTE < 30) {
	string += "just after " + HOUR + " in the ";
}
else {
	string += "almost " + (HOUR+1) + " in the ";
}

if (PERIOD == "AM") {
	string += "morning.";
} else {
	string += "evening.";
}

console.log(string);