var express = require('express');
var app = express();
var path = require('path');
var bodyParser = require('body-parser');
var mongoose = require('mongoose');


app.use(bodyParser.urlencoded({extended:true}));
app.use(express.static(path.join(__dirname,'static')));
app.use('/llama', express.static(path.join(__dirname,'static')));
app.use('/edit', express.static(path.join(__dirname,'static')));
app.set('views', path.join(__dirname,'./views'));
app.set('view engine','ejs');

// DB Setup
mongoose.connect('mongodb://localhost/dashboard_db/llama');
var LlamaSchema = new mongoose.Schema({
	name: {type:String,required:true},
	country: {type:String,required:true},
	age: {type:Number,required:true},
	img_url: {type: String}
}, {timestamps:true});
mongoose.model('Llama',LlamaSchema);
var Llama = mongoose.model('Llama');

// Routes
app.get('/', function(req,res) {
	Llama.find({}, function(err,all_llamas) {
		if(err) {
			console.log("*********** ERROR ***********");
			console.log(err);
			res.render('index');

		} else {
			console.log("------------------------------------");
			console.log("dirname:", __dirname);
			console.log("------------------------------------");
			
			console.log("*********** FOUND LLAMAS! ***********");
			for(var i=0;i<all_llamas.length;i++) {
				console.log(all_llamas[i].name);
			}
			res.render('index', {llamas:all_llamas});
		}
	});
});

app.get('/new', function(req,res) {
	res.render('new_llama');
});

app.post('/create', function(req,res) {
	var post = req.body;
	var newLlama = new Llama({
		name: post.name,
		country: post.country,
		age: post.age,
		img_url: post.img_url
	});
	newLlama.save(function(err) {
		if(err) {
			console.log("*********** ERRORS ***********");
			console.log(err);
			
		} else {
			console.log("------------------------------------");
			console.log("successfully added llama!");
			console.log("------------------------------------");
		}
		res.redirect('/');
	});
});

app.get('/llama/:id', function(req,res) {
	// Get id
	var id = req.params.id;
	console.log("------------------------------------");
	console.log("Llama id:", id);
	console.log("------------------------------------");

	// Find llama in database
	Llama.find({_id:id}, function(err, thisLlama) {
		if(err) {
			console.log("*********** ERROR! ***********");
			console.log(err);
			res.redirect('/');
		} else {
			console.log("*********** FOUND LLAMA! ***********");
			console.log(thisLlama);
			res.render('view_llama', {llama:thisLlama[0]});
		}
	});
	
});	

app.get('/edit/:id', function(req,res) {
	var id = req.params.id;
	Llama.find({_id:id}, function(err,thisLlama) {
		if(err) {
			console.log("*********** ERRORS ***********");
			console.log(err);
			res.redirect('/');
		} else {
			console.log("*********** FOUND LLAMA TO EDIT ***********");
			console.log(thisLlama);
			res.render('edit_llama',{llama:thisLlama[0]});
		}
	});
});

app.post('/update/:id', function(req,res) {
	Llama.findOne({_id:req.params.id}, function(err,llama){
		llama.name = req.body.name;
		llama.country = req.body.country;
		llama.age = req.body.age;
		llama.img_url = req.body.img_url;
		
		llama.save(function(err) {
			if(err) {
				console.log("*********** ERROR ***********");
				console.log(err);
				res.redirect('/')
			} else {
				console.log("*********** LLAMA UPDATED ***********");
				res.redirect('/llama/' + req.params.id);
			}
		});
	});
});

app.get('/destroy/:id', function(req,res) {
	Llama.remove({_id:req.params.id},function(err) {
		if(err) {
			console.log("*********** ERROR ***********");
			console.log(err);
			console.log("^^^^^^^^^^^ ERROR ^^^^^^^^^^^");
			res.redirect('/');
		} else {
			console.log("*********** LLAMA REMOVED ***********");
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