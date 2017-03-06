$(document).ready(function() {
	$('img').hover(function() {
		var altImg = $(this).attr('data-alt-src'); // store alt image in variable
		$(this).attr('data-alt-src', $(this).attr('src')); // keep original src for use later in data-alt-src
		$(this).attr('src', altImg); // change src to altImg variable
	},
	function() {
		var altImg = $(this).attr('data-alt-src'); // store alt image in variable
		$(this).attr('data-alt-src', $(this).attr('src')); // keep original src for use later in data-alt-src
		$(this).attr('src', altImg); // change src to altImg variable
	})
});