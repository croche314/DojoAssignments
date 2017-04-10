var mongoose = require('mongoose');
var Person = mongoose.model('Person');

module.exports = {
	showAll: function(req,res) {
		Person.find({}, function(err,people) {
			if(err) {
				console.log("*********** ERRORS ***********");
				console.log(err);
				console.log("^^^^^^^^^ END ERRORS ^^^^^^^^^")
			} else {
				console.log("*********** FOUND PEOPLE! ***********");
				console.log(people);
				res.json(people);
			}
		});
	},

	create: function(req,res) {
		var newPerson = new Person({name:req.params.name});
		newPerson.save(function(err) {
			if(err) {
				console.log("*********** ERRORS ***********");
				console.log(err);
				console.log("^^^^^^^^^ END ERRORS ^^^^^^^^^")
				res.redirect('/');
			} else {
				console.log("*********** NEW PERSON SAVED! ***********");
				res.redirect('/')
			}
		});
	},

	remove: function(req,res) {
		Person.remove({name:req.params.name}, function(err) {
			if(err) {
				console.log("*********** ERRORS ***********");
				console.log(err);
				console.log("^^^^^^^^^ END ERRORS ^^^^^^^^^")
				res.redirect('/');
			} else {
				console.log("*********** PERSON DELETED! ***********");
				console.log(req.params.name, "is no more")
				res.redirect('/');
			}
		});	
	},

	show: function(req,res) {
		Person.findOne({name: req.params.name}, function(err, person) {
			if(err) {
				console.log("*********** ERRORS ***********");
				console.log(err);
				console.log("^^^^^^^^^ END ERRORS ^^^^^^^^^")
				res.redirect('/');
			} else {
				console.log("*********** FOUND PERSON! ***********");
				res.json(person);
			}
		});
	}
}