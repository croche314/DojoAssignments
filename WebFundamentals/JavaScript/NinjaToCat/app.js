$(document).ready(function() {
	$('img').click(function() {
		var altImage = $(this).attr('data-alt-src'); // store alt image in variable
		$(this).attr('data-alt-src', $(this).attr('src')); // switch src and data-alt-src attributes
		$(this).attr('src', altImage); // insert alt image into src attribute
	})
});