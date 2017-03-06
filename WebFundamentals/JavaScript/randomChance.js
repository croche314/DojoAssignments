function playSlots(quarters, cashOut) {

	console.log("Starting quarters: ", quarters);
	if (cashOut) {
		console.log("Your cash-out threshold: ", (cashOut), ".  Good Luck!");
	}

	while ((quarters > 0)  && (quarters <= cashOut)) {
		var roll = Math.floor(Math.random() * 100); //47
		if (roll === 50) {
			prize = Math.floor((Math.random() * 50)) + 50;
			quarters += prize;
			console.log("You won ", prize, " quarters!");
			console.log("Quarters remaining: ",quarters);
		} else {
			console.log("Sorry, you didn't win... =(");
			quarters--;
			console.log("Quarters now remaining:", quarters);
		}
	}

	if (quarters >= cashOut) {
		console.log("You've reached your cash-out threshold of", cashOut, "quarters!  Bye!")
	} else {
		console.log("Out of quarters! Please enter more quarters to keep playing...");
	}
} // playSlots

playSlots(90, 200);
