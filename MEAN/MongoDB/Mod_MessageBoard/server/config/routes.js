var mongoose = require('mongoose');
var Message = mongoose.model('Message');
var messages = require('../controllers/messages.js');

module.exports = function(app) {
	app.get('/', function(req,res) {
		messages.show(req,res);
	});
	app.post('/message/create', function(req,res) {
		messages.create(req,res);
	});
	app.get('/delete/:id', function(req,res) {
		messages.delete(req,res);
	});
}