
import random

class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value
    
    def show(self):
        print("{} {}".format(self.rank, self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ['♡', '♧', '♢', '♤']:
            for r in range(1, 14):
                if r == 1:
                    self.cards.append(Card(s, 'A', 1))
                elif r == 11:
                    self.cards.append(Card(s, 'J', 10))
                elif r == 12:
                    self.cards.append(Card(s, 'Q', 10))
                elif r == 13:
                    self.cards.append(Card(s, 'K', 10))
                else:
                    self.cards.append(Card(s, r, r))
    
    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

def main(): 
    print("Welcome to Blackjack")
    print(f"Credits: ${credits}")
    bet = input("Enter bet: ")
    input("Hit ENTER to deal")

    # deck = Deck()
    # deck.shuffle()

    # dealer = Player("Dealer")
    # dealer.draw(deck)
    # dealer.showHand(), dealer.draw(deck)

    # bob = Player("Player")
    # bob.draw(deck), bob.draw(deck)
    # bob.showHand()
    
main()