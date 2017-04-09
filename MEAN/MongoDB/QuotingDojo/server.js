var express = require('express');
var app = express();
var path = require('path');
var bodyParser = require('body-parser');
var mongoose = require('mongoose');

app.use(bodyParser.urlencoded({extended:true}));
app.use(express.static(path.join(__dirname,'./static')));
app.set('views',path.join(__dirname,'./views'));
app.set('view engine','ejs');

// DB setup
mongoose.connect('mongodb://localhost/basic/mongoose');
var UserSchema = new mongoose.Schema({
	name: {type: String, required:true,maxlength:20},
	quote: {type: String,required:true,minlength:5}
}, {timestamps: true });
mongoose.model('Quote', UserSchema);
var Quote = mongoose.model('Quote');

// Routes
app.get('/', function(req,res) {
	res.render('index');
});

app.post('/quotes', function(req,res) {
	console.log("----------- POST DATA ------------");
	console.log(req.body);
	// create new document
	var quote = new Quote({
		name:req.body.name, 
		quote:req.body.quote
	});
	quote.save(function(err) {
		if(err) {
			console.log('something went wrong');
			console.log("*********** Errors ***********");
			console.log(err)
			var errorsArr = [];
			
			for(errName in err.errors) {
				console.log("------------------------------------");
				console.log("Result:",err.errors[errName].message);
				console.log("------------------------------------");
				errorsArr.push(err.errors[errName].message);
			}
			//res.redirect('/');
			res.render('errors', {errors:errorsArr});
		} else {
		 	console.log("------------------------------------");
		 	console.log("successfully added a quote!");
		 	console.log("redirecting to 'quotes'...")
		 	console.log("------------------------------------");
		 	res.redirect('/quotes');	 	
		}
	});
});

app.get('/quotes', function(req,res) {
	// find all quotes
	Quote.find({}).sort('-createdAt').exec(function(err,all_quotes) {
		if(err) {
			console.log("*********** Error: ***********");
			for(var i=0;i<err.length;i++) {
				console.log(err[i]);
			}
			// display errors
			res.render('quotes', {errors:err});
		} else {
			console.log("*********** All Quotes ***********");
			for(var i=0;i<all_quotes.length;i++) {
				console.log(all_quotes);
			}
			// display quotes
			res.render('quotes', {all_quotes: all_quotes});

		}
		
	});
	
})

// Listen
app.listen(8000, function() {
	console.log('listening on port 8000...');
});
