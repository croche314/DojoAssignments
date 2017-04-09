var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var path = require('path');
var mongoose = require('mongoose');

app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static(path.join(__dirname,'./static')));
app.set('views',path.join(__dirname,'./views'));
app.set('static', path.join(__dirname,'./static'));
app.set('view engine','ejs');

// Mongoose DB setup
mongoose.connect('mongodb://localhost/basic/mongoose');
var UserSchema = new mongoose.Schema({
	name: String,
	age: Number
})
mongoose.model('User',UserSchema);
var User = mongoose.model('User');

// Routes
app.get('/', function(request,response) {
	User.find({}, function(err,users) {
		console.log('users:',users);
		response.render('index',{users:users});
	});
	
});

app.post('/users', function(request,response) {
	console.log("-------- POST DATA ---------");
	console.log(request.body);

	var user = new User({
		name: request.body.name, 
		age: request.body.age
	});
	user.save(function(err) {
		if(err) {
			console.log("something went wrong");
		} else {
			console.log("successfully added a user!");
			console.log("redirecting to '/'...")
			response.redirect('/');
		}
	})

	//console.log("redirecting to '/'...")
	//response.redirect('/');
});
	


// Start server
app.listen(8000,function() {
	console.log('listening on port 8000...')
});
