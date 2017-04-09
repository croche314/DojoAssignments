// x = [3,5,"Dojo","rocks","Michael","Sensei"];
	// for(key in x){
	// 	console.log(x[key]);
	// };
	// x.push(100);
	// console.log(x);

	// x.push(["hello","world","JavaScript is Fun"]);
	// console.log(x);
	// var sum = 0;
	// for(var i=1;i<=500;i++) {
	// 	sum += i;
	// }
	// console.log(sum);
	var arr = [1, 5, 90, 25, -3, 0];
	// var min = arr[0]
	// for(var i=0;i<arr.length;i++) {
	// 	if (arr[i] < min) {
	// 		min = arr[i];
	// 	}
	// console.log("Minimum:",min);
	// }
	// var sum = 0;
	// for(var i=0;i<arr.length;i++) {
	// 	sum += arr[i];
	// }
	// avg = sum / arr.length;
	// console.log(avg);

var newNinja = {
	name: 'Jessica',
	profession: 'coder',
	favorite_language: 'JavaScript', //like that's even a question!
	dojo: 'Dallas'
}

for (key in newNinja) {
	console.log(newNinja[key]);
}
