$(document).ready(function(){

	$('form').submit(function(){
		var first_name = $('#first_name').val();
		var last_name= $('#last_name').val();
		var email = $('#email').val();
		var contact_number = $('#contact_number').val();
		
		$('table').append('<tr><td>'+first_name+'</td><td>'+last_name+'</td><td>'+email+'</td><td>'+contact_number+'</td></tr>');

		return false;
	});
});