var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var mongoose = require('mongoose');
var path = require('path');

app.use(bodyParser.urlencoded({extended:true}));
app.use(express.static(path.join(__dirname,'./client/static')));
app.set('views', path.join(__dirname,'./client/views'));
app.set('view engine', 'ejs');

//*********** DB/MODELS ***********
require('./server/config/mongoose.js');

//*********** ROUTES ***********
var routes_setter = require('./server/config/routes.js');
routes_setter(app);

// Listen
app.listen(8000, function() {
	console.log("------------------------------------");
	console.log("Listening on port 8000...");
	console.log("------------------------------------");
	
})
