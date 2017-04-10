var mongoose = require('mongoose');
var Message = mongoose.model('Message');

module.exports = {
	show: function(req,res) {
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
	},
	create: function(req,res) {
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
	},
	delete: function(req,res) {
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
	}
}

