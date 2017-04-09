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

var PlayerContructor = function(name) {
	this.name = name;
	this.hand = [];
	this.myDeck = new DeckConstructor();
	
	this.takeACard = function() {
		var card = this.myDeck.deal();
		this.hand.push(card);
		return card;
	}
	this.discard = function() {
		return this.hand.pop();
	}
	this.showHand = function() {
		console.log(this.hand);
		return this.hand;
	}
}

var steve = new PlayerContructor('steve');
console.log(steve.takeACard());
console.log(steve.takeACard());
steve.showHand();
steve.discard();
steve.showHand();



// console.log('unshuffled deck:',newDeck.deck);
// newDeck.shuffle();
// console.log('shuffled deck:',newDeck.deck);
// console.log("-------------------------------------------");
// console.log('dealt card:',currentDeck.deal());
// console.log("-------------------------------------------");
//console.log(currentDeck.deck);
