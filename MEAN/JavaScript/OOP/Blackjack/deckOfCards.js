$(document).ready(function() {
	function DeckConstructor() {
		this.deck = [];
		this.suits = ['c','d','h','s'];
		// Make an array of cards that match the names of the images we're going to use
		// (h5 = 5 of hearts)
		this.resetDeck = function() {
			for(var i=0;i<this.suits.length;i++) {
				for(var j=1;j<14;j++) {
					num = j;
					if(num==11) {
						num = 'j';
					} else if (num==12) {
						num = 'q';
					} else if (num==13) {
						num = 'k';
					}
					this.deck.push(this.suits[i]+num);
				}
			}
			return this;
		}
		
		this.shuffle = function() {
			var array = this.deck;
			var copy = [];
			var length = array.length;
			var i;
			
			while (length) {
				i = Math.floor(Math.random() * array.length);
				
				if (i in array) {
					copy.push(array[i]);
					delete array[i];
					length--;
				}
			}
			this.deck = copy;
			return this;
		}

		this.deal = function() {
			var i = Math.floor(Math.random()*this.deck.length);
			var card = this.deck[i];
			this.deck.splice(i,1);

			return card;
		}
		this.resetDeck();
	
	}

	var PlayerContructor = function(name,deck) {
		this.name = name;
		this.myHand = [];
		this.deck = deck;
		
		this.takeACard = function() {
			var card = this.deck.deal();
			this.myHand.push(card);
			return card;
		}
		this.discard = function() {
			return this.myHand.pop();
		}
		this.showHand = function() {
			console.log(this.myHand);
			if (this.name == 'dealer') {
				$('#dealer_hand').html("<img src='cards-png/"+this.myHand[0]+".png' alt='card'>");
				for(var x=1;x<this.myHand.length;x++) {
					$('#dealer_hand').append("<img src='cards-png/"+this.myHand[x]+".png' alt='card'>");
				}
			} else {
				$('#player_hand').html("<img src='cards-png/"+this.myHand[0]+".png' alt='card'>");
				for(var i=1;i<this.myHand.length;i++) {
					$('#player_hand').append("<img src='cards-png/"+this.myHand[i]+".png' alt='card'>");
				}
			}
			return this.myHand;
		}

		this.calculateHandTotal = function() {
			
		}
	}

	var GameConstructor = function() {
		this.currentDeck = new DeckConstructor();
		this.currentDeck.shuffle();
		this.player = new PlayerContructor('player',this.currentDeck);
		this.dealer = new PlayerContructor('dealer',this.currentDeck);

		this.player.takeACard();
		this.player.takeACard();
		this.dealer.takeACard();
		this.dealer.takeACard();
		this.player.showHand();
	}

	// Start Game Instructions
	var thisGame = new GameConstructor()
	var player_card1 = thisGame.player.myHand[0];
	var player_card2 = thisGame.player.myHand[1];
	var dealer_card1 = thisGame.dealer.myHand[0];
	var dealer_card2 = thisGame.dealer.myHand[1];

	console.log('player card 1:',player_card1);
	console.log('player card 2:',player_card2);
	console.log('dealer card 1:',dealer_card1);
	console.log('dealer card 2:',dealer_card2);

	// Player Hand Display
	// $('#player_hand').append("<img src='cards-png/"+player_card1+".png' alt='card'>");
	// $('#player_hand').append("<img src='cards-png/"+player_card2+".png' alt='card'>");
	// Dealer Hand Display
	$('#dealer_hand').append("<img src='cards-png/"+dealer_card1+".png' alt='card'>");
	$('#dealer_hand').append("<img src='cards-png/b1pr.png' alt='card edge'>");

	$('#btn_hit').click(function() {
		thisGame.player.takeACard();
		thisGame.player.showHand();
	})

	$('#btn_stay').click(function() {
		var dealer = thisGame.dealer;
		dealer.showHand();

	})
	


}) // end ready


