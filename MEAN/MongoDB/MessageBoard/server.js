var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var mongoose = require('mongoose');
var path = require('path');

app.use(bodyParser.urlencoded({extended:true}));
app.use(express.static(path.join(__dirname,'static')));
app.set('views', path.join(__dirname,'./views'));
app.set('view engine', 'ejs');

// DB Setup
mongoose.connect('mongodb://localhost/messageBoardDB/mongoose');
var Schema = mongoose.Schema;

var MessageSchema = new mongoose.Schema({
	name: {type: String, required: true},
	comments: {type: Schema.Types.ObjectId, ref: 'Comment'},
	message: {type: String, required: true}
}, {timestamps: true});

var CommentSchema = new mongoose.Schema({
	_messageID: {type: Schema.Types.ObjectId, ref: 'Message', required: true},
	comment: {type: String, required: true}
}, {timestamps: true});

// mongoose.model('User', UserSchema);
mongoose.model('Message', MessageSchema);
mongoose.model('Comment', CommentSchema);

// var User = mongoose.model('User');
var Message = mongoose.model('Message');
var Comment = mongoose.model('Comment');

// Routes
app.get('/', function(req,res) {
	Message.find({}, function(err,messages) {
		console.log("*********** ALL MESSAGES ***********");
		for (var i=0;i<messages.length;i++) {
			console.log("------------------------------------");
			console.log("****Message****");
			console.log(messages[i]);
			console.log("------------------------------------");

			res.render('index', {all_messages: messages});
		}
	});
});

app.post('/message/create', function(req,res) {
	var new_message = new Message({
		name: req.body.name,
		message: req.body.new_message
	});
	new_message.save(function(err) {
		if(err) {
			console.log("*********** ERROR ***********");
			console.log(err);
			console.log("^^^^^^^^^^^ ERROR ^^^^^^^^^^^");
			res.redirect('/');
		} else {
			console.log("*********** MESSAGE CREATED! ***********");
			res.redirect('/');
		}
	});
});

app.get('/delete/:id', function(req,res) {
	Message.remove({_id:req.params.id}, function(err) {
		if(err) {
			console.log("*********** ERROR ***********");
			console.log(err);
			console.log("^^^^^^^^^^^ ERROR ^^^^^^^^^^^");
			res.redirect('/');
		} else {
			console.log("*********** MESSAGE DELETED! ***********");
			res.redirect('/');
		}
	});
});

// Listen
app.listen(8000, function() {
	console.log("------------------------------------");
	console.log("Listening on port 8000...");
	console.log("------------------------------------");
	
})
