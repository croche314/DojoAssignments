$(function() {
	$('.datepicker').datepicker();
});

$(function() {
	$('.dialog').dialog();
});

var dateFrom;
var dateTo;
var name;

$(document).ready(function() {
	$('#date-from, #date-to').change(function() {
		dateFrom = $('#date-from').val();
		dateTo = $('#date-to').val();
		
	})

	$('#btn-submit').click(function(event) {
		event.preventDefault();
		console.log("working...");
		console.log(dateFrom, dateTo);
		if ($('#txt-name').val() == "") {
			$('#invalid-name').removeClass('hide');
			alert("Please fill out all required fields");
		} else {
			name = $('#txt-name').val();
			console.log(name);
			alert("Thanks "+name+"!  Your cruise leaves on "+dateFrom+" and returns on "+dateTo+"!");
		}
	})

	$('#txt-name').hover(function() {
		$('#invalid-name').addClass('hide');
	})
});

