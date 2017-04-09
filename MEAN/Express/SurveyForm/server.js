var express = require('express');
var path = require('path');
var app = express();
var bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({extended:true}));
app.use(express.static(path.join(__dirname,'./static')));

app.set('views',path.join(__dirname,'./views'));
app.set('view engine','ejs');

// Routes
app.get('/', function(req,res) {
	console.log("-------------------------------------------");
	console.log("rendering 'index'...");
	console.log("-------------------------------------------");
	res.render('index');
})

app.post('/result', function(req,res) {
	data = req.body;
	res.render('result', {title:'Result',user:data});
})


app.listen(8000, function() {
	console.log("-------------------------------------------");
	console.log("listening on port 8000...")
	console.log("-------------------------------------------");
})