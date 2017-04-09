function VehicleConstructor(name,numOfWheels,numOfPassengers,speed) {
	var self = this;
	// PRIVATE
	var distance_travelled = 0
	var updateDistanceTravelled = function() {
		distance_travelled += self.speed;
	}

	// PUBLIC
	this.name = name;
	this.numOfWheels = numOfWheels;
	this.numOfPassengers = numOfPassengers;
	this.speed = speed;

	this.makeNoise = function() {
		console.log('Honk! I am a ',this.name+'!');
	}
	this.move = function() {
		updateDistanceTravelled();
		this.makeNoise();
	}
	this.checkMiles = function() {
		console.log(distance_travelled)
	}
} // VehicleConstructor

var Bike = new VehicleConstructor('bicycle',2,1,20);
Bike.makeNoise();
Bike.makeNoise = function() {
	console.log('ring ring!');
}
Bike.makeNoise();

var Sedan = new VehicleConstructor('sedan',4,5,50);
Sedan.prototype.makeNoise = function() {
	console.log('Honk honk!');
}
Sedan.makeNoise();

var Bus = new VehicleConstructor('bus',4,20,40);
Bus.pickupPassengers = function(waitingAtBusStop) {
	Bus.numOfPassengers += waitingAtBusStop;
}
console.log(Bus.numOfPassengers);
Bus.pickupPassengers(10);
console.log(Bus.numOfPassengers);
Bus.move();
Bus.checkMiles();
Bus.makeNoise();


