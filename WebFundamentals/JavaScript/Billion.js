var start_amount = 0.01;
var sum = 0;

for(var i=1;i<=30;i++) {
	sum += start_amount;
	start_amount*=2;
}

console.log("Total after 30 days: ", sum);

var start_amount= 0.01;
var sum = 0;

for(var i=0;sum<10000;i++) {
	sum += start_amount;
	start_amount*=2;
}

console.log("It takes ", i+1, " days to reach $10,000.")

var start_amount= 0.01;
var sum = 0;

for(var i=0;sum<1000000000000;i++) {
	sum += start_amount;
	start_amount*=2;
}

console.log("It takes ", i+1, " days to reach $1,000,000,000.");

var start_amount= 0.01;
var sum = 0;

for(var i=0;sum<Infinity;i++) {
	sum += start_amount;
	start_amount*=2;
}

console.log("It takes ", i+1, " days to reach infinity.")