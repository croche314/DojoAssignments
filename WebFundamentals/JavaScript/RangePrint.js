function printRange(start,stop,skip) {

	console.log("start: ",start);
	console.log("stop: ",stop);
	console.log("skip: ",skip);

	if(!skip) {skip = 1;}
	if(!stop) {stop = start;  start = 0;}

	if(start < stop) {
		for(i=start;i<stop;i+=skip) {
			console.log(i);
		}
	}
	else {
		for(i=start;i>stop;i-=skip) {
			console.log(i);
		}
	}
	
}

printRange(2,10,2);
printRange(-20,1,1);
printRange(1,10);
printRange(15);


