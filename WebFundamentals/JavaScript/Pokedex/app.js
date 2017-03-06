function makeHTML(url,i) {
	$.get(url, function(res) {
			
		var html_string = "";
		var name = res.name;
		var types = [];
		for(var j=0;j<res.types.length;j++) {
			//console.log(res.types[j].name);
			types.push(res.types[j].name);
		}
		var height = res.height;
		var weight = res.weight;
		var img_url = "http://pokeapi.co/media/img/" + i + ".png"
		html_string = "<div id='"+i+"' class='pokemon' "
		html_string += "data-name='"+ name +"' ";
		html_string += "data-height='" + height + "' ";
		html_string += "data-weight='" + weight + "' ";
		html_string += "data-types='" + types + "'> ";
		html_string += "<img src='" + img_url + "' alt='" + name + "'></div>";

		$('#poke-list').append(html_string);
	}, 'json');
}

$(document).ready(function() {
	for(var i=1;i<=151;i++) {
		var url = "http://pokeapi.co/api/v1/pokemon/" + i;
		makeHTML(url,i);	
	}

	$(document).on('click', '.pokemon', function() {
		var type_arr = $(this).attr('data-types').split(',');
		var height = $(this).attr('data-height');
		var weight = $(this).attr('data-weight');
		var html_str = "<h2>"+$(this).attr('data-name')+"</h2> ";
		html_str += "<img src='http://pokeapi.co/media/img/" + $(this).attr('id') + ".png'>";
		html_str += "<h3>Stats</h3>  <ul><h4>Types</h4>";
		for(var i=0;i<type_arr.length;i++) {
			html_str += "<li>" + type_arr[i] + "</li>";
		}
		html_str += "</ul>"
		html_str += "<h4>Height</h4><p>" + height + "</p>";
		html_str += "<h4>Weight</h4><p>" + weight + "</p>";
		
		$('#poke-stats').html(html_str);
	})

})