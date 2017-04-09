var http = require('http');
var fs = require('fs');
var server = http.createServer(function (request,response) {
	console.log('client request URL:',request.url);
	// Index
	if (request.url === '/') {
		fs.readFile('index.html','utf8',function(errors,contents) {
			response.writeHead(200,{'Content-Type': 'text/html'});
			response.write(contents);
			response.end();
		});
	// Ninjas (about ninjas)
	} else if (request.url === '/ninjas') {
		fs.readFile('ninjas.html','utf8',function(errors,contents) {
			response.writeHead(200,{'Content-Type': 'text/html'});
			response.write(contents);
			response.end();
		});
	// Dojos (form)
	} else if (request.url === '/dojos/new') {
		fs.readFile('dojos.html','utf8',function(errors,contents) {
			response.writeHead(200,{'Content-Type': 'text/html'});
			response.write(contents);
			response.end();
		});
	// route not found!
	} else {
		response.writeHead(404);
		response.end('File not found!');
	}
}); // end createServer

server.listen(8000)
console.log("-------------------------------------------");
console.log("Running in localhost at port 8000...")
console.log("-------------------------------------------");