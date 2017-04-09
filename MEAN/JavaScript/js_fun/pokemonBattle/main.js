var game = {
	players: [],
	addPlayer: function(playerName){
		var newPlayer = playerConstructor(playerName);
		game.players.push(newPlayer);
	},
};

function playerConstructor(name) {
	player = {};
	player.name = name;
	player.hand = [];
	player.addCard = function(card){
		url = "http://pokeapi.co/api/v1/pokemon/"+card;
		$.get(url,function(res){
			console.log(res)
			player.hand.push(res);

		},'json');
		console.log('Hand:',player.hand)
	};
	player.addCard(Math.floor(Math.random() * 151))
	return player;
}

game.addPlayer('Chris');
game.addPlayer('Phil');
// console.log(game.players[0].hand[0]);
// console.log(game.players[0].hand[0].readyState);
// console.log(game.players[0].hand[0].responseJSON);

