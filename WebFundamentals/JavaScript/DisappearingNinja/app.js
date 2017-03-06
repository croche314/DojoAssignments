$(document).ready(function(){
	
	$('img').click(function(){
		$(this).css('opacity', '0');
	})

	$('#restore').click(function() {
		$('img').css('opacity', '100');
	})
});