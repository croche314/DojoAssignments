function displayHouseInfo(id) {
	$.get("http://anapioficeandfire.com/api/houses/"+id, function(res) {
		$('#display-house-stats').html(" ");

		var name = res.name;
		var words = res.words;
		var titles = res.titles;
		var title_str = "";
		var region = res.region;
		var coatOfArms = res.coatOfArms;
		var weapons = res.ancestralWeapons;
		var weapon_str = "";
		var members_urls = res.swornMembers;
		
		$('#display-house-stats').append("<h3>" + name + "</h3>");
		$('#display-house-stats').append("<p><b>Words</b> " + words + "</p>");
		$('#display-house-stats').append("<ul><b>Titles</b> ");
		for(var i=0;i<titles.length;i++) {
			title_str += "<li>" + titles[i]+ "</li>";
		}
		$("#display-house-stats").append(title_str + "</ul>");
		$('#display-house-stats').append("<p><b>Region</b> " + region + "</p>");
		$('#display-house-stats').append("<p><b>Coat of Arms</b> " + coatOfArms + "</p>");
		$("#display-house-stats").append("<ul><b>Ancestral weapons</b> ");
		if (weapons.length == 0) {
			weapon_str = "None";
		} else {
			for(var j=0;j<weapons.length;j++) {
				weapon_str += "<li>" + weapons[j] + "</li>";
			}
		}
		$("#display-house-stats").append(weapon_str + "</ul>");
		$("#display-house-stats").append("<ul><b>Sworn members</b> ");
		for(var x=0;x<members_urls.length;x++) {
			$.get(members_urls[x], function(data) {
				$('#display-house-stats').append("<li>");
				$('#display-house-stats').append(data.name);
				$('#display-house-stats').append("</li>");
			})
		}
		$("#display-house-stats").append(member_str + "</ul>");
	})
}

$(document).ready(function() {
	$("#stark").click(function() {
		displayHouseInfo(362);
	})
	$('#targaryen').click(function() {
		displayHouseInfo(378);
	})
	$('#lannister').click(function() {
		displayHouseInfo(229);
	})
	$('#baratheon').click(function() {
		displayHouseInfo(17);
	})
})
