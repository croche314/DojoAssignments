function makeHTML(first_name, last_name, description) {
	return "<div class='card'><h2>"+first_name+" "+last_name+"</h2><h3 class='hide'>"+description+"</h3><p>Click for description</p></div>";
}

$(document).ready(function() {
	$('form').submit(function(event) {
		var htmlString = makeHTML($('#txt_first_name').val(),$('#txt_last_name').val(),$('#txt_description').val());
		$('#card-display').append(htmlString);
		event.preventDefault();
	})

	$(document).on("click", ".card", function() {
		console.log(".card has been clicked!");
		
		$(this).children().toggleClass('hide');
	});
})