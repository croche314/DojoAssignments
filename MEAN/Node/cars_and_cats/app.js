var http = require('http');
var fs = require('fs');
var server = http.createServer(function(request,response) {
	console.log("-------------------------------------------");
	console.log("URL Request:",request.url);
	console.log("-------------------------------------------");
	// HTML Files
	if (request.url === '/') {
		fs.readFile('views/index.html','utf8',function(errors,contents) {
			response.writeHead(200,{'Content-Type':'text/html'});
			response.write(contents);
			response.end();
		});
	} else if (request.url === '/cars') {
		fs.readFile('views/cars.html','utf8',function(errors,contents) {
			response.writeHead(200,{'Content-Type':'text/html'});
			response.write(contents);
			response.end();
		});
	} else if (request.url === '/cats') {
		fs.readFile('views/cats.html','utf8',function(errors,contents) {
			response.writeHead(200,{'Content-Type':'text/html'});
			response.write(contents);
			response.end();
		});
	} else if (request.url === '/cars/new') {
		fs.readFile('views/new_car.html','utf8',function(errors,contents) {
			response.writeHead(200,{'Content-Type':'text/html'});
			response.write(contents);
			response.end();
		});
	// CSS File
	} else if (request.url === '/stylesheets/style.css') {
		fs.readFile('./stylesheets/style.css','utf8',function(errors,contents) {
			response.writeHead(200,{'Content-Type':'text/css'});
			response.write(contents);
			response.end();
		});
	// Image Files
	} else if (request.url === '/images/ford_mustang.jpg'){
		fs.readFile('./images/ford_mustang.jpg', function(errors,contents) {
			response.writeHead(200,{'Content-Type':'image/jpg'});
			response.write(contents);
			response.end();
		});
	} else if (request.url === '/images/porsche_911.jpg'){
		fs.readFile('./images/porsche_911.jpg', function(errors,contents) {
			response.writeHead(200,{'Content-Type':'image/jpg'});
			response.write(contents);
			response.end();
		});
	} else if (request.url === '/images/Ferrari_488.jpg'){
		fs.readFile('./images/Ferrari_488.jpg', function(errors,contents) {
			response.writeHead(200,{'Content-Type':'image/jpg'});
			response.write(contents);
			response.end();
		});
	} else if (request.url === '/images/ford_pos.jpg'){
		fs.readFile('./images/ford_pos.jpg', function(errors,contents) {
			response.writeHead(200,{'Content-Type':'image/jpg'});
			response.write(contents);
			response.end();
		});
	} else if (request.url === '/images/black_cat.jpg'){
		fs.readFile('./images/black_cat.jpg', function(errors,contents) {
			response.writeHead(200,{'Content-Type':'image/jpg'});
			response.write(contents);
			response.end();
		});
	} else if (request.url === '/images/sphynx_cat.jpg'){
		fs.readFile('./images/sphynx_cat.jpg', function(errors,contents) {
			response.writeHead(200,{'Content-Type':'image/jpg'});
			response.write(contents);
			response.end();
		});
	} else if (request.url === '/images/siamese_cat.jpg'){
		fs.readFile('./images/siamese_cat.jpg', function(errors,contents) {
			response.writeHead(200,{'Content-Type':'image/jpg'});
			response.write(contents);
			response.end();
		});
	} else if (request.url === '/images/grumpy_cat.jpg'){
		fs.readFile('./images/grumpy_cat.jpg', function(errors,contents) {
			response.writeHead(200,{'Content-Type':'image/jpg'});
			response.write(contents);
			response.end();
		});
	} else {
		response.writeHead(400);
		response.write('File not found!');
	}
});

server.listen(7077);
console.log("-------------------------------------------");
console.log("Listening on port 7077...")
console.log("-------------------------------------------");