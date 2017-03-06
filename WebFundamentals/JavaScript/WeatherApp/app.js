$(document).ready(function() {
	$.get("http://api.openweathermap.org/data/2.5/forecast/city?id=4887398%APPID=bcfc3b73bda636ebd5e2a90998292599", function(res) {
		console.log(res);
	}, 'json');
})