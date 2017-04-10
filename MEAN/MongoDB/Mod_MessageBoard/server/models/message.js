var mongoose = require('mongoose');
//var Schema = mongoose.Schema;

var MessageSchema = new mongoose.Schema({
	name: {type: String, required: true},
	message: {type: String, required: true}
}, {timestamps: true});

var Message = mongoose.model('Message', MessageSchema);