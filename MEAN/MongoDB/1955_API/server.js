var express = require('express');
var app = express();
var path = require('path');

var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({extended: true}));

app.use(express.static(path.join(__dirname, './client/static')));
app.use(bodyParser.json());

//*********** DB/MODELS ***********
require('./server/config/mongoose.js');

//*********** ROUTES ***********
var routes_setter = require('./server/config/routes.js');
routes_setter(app);

//*********** LISTEN ***********
app.listen(8000, function() {
	console.log("------------------------------------");
	console.log("LISTENING ON PORT 8000...");
	console.log("------------------------------------");
	
});