var express = require("express");
var bodyParser = require("body-parser");
var app = express();

app.use(express.static(__dirname + "/static"));
app.use(bodyParser.urlencoded({extended:true}));
app.set('view engine','ejs');

app.get('/', function(request,response) {
	response.send("<h1>Hello Express</h1>");
});

app.get("/users", function(request,response) {
	var users_array = [
		{name: "Michael", email: "michael@codingdojo.com"}, 
        {name: "Jay", email: "jay@codingdojo.com"}, 
        {name: "Brendan", email: "brendan@codingdojo.com"}, 
        {name: "Andrew", email: "andrew@codingdojo.com"}
	];
	response.render('users', {users: users_array,title: 'My Express Project'});
});

app.get("/users/:id", function(req,res) {
	console.log("The user id requested is:", req.params.id);
	console.log(req.params);
	res.send("You requested the user with id:" + req.params.id);
});

app.post('/users',function (req,res) {
	console.log("POST DATA \n\n", req.body);
	
	res.redirect('/');
});	

app.listen(8000,function() {
	console.log("-------------------------------------------");
	console.log("Listening on port 8000");
	console.log("-------------------------------------------");
})
