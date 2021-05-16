
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
                    self.cards.append(Card(s, 'A', [1, 11]))
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
        random.shuffle(self.cards)

    def deal(self):
        single_card = self.cards.pop()
        return single_card

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.deal())
        return self

    def dealer_hand(self):
        for i, card in enumerate(self.hand):
            if i == 0:
                print("<hidden>")
            else:
                card.show()

    def player_hand(self):
        for card in self.hand:
            card.show()

    def ace(self):
        pass

class Credits:
    def __init__(self):
        self.total = 2000
        self.bet = 0

    def win(self):
        self.total += self.bet

    def lose(self):
        self.total -= self.bet

def main(): 

    # print("Welcome to Blackjack")
    # print(f"Credits: ${credits}")
    
    # bet = input("Enter bet: ")
    
    # input("Hit ENTER to deal")

    deck = Deck()
    deck.shuffle()
    # deck.show()
    

    dealer = Player("Dealer")
    dealer.draw(deck), dealer.draw(deck)
    dealer.dealer_hand()

    # # bob = Player("Player")
    # # bob.draw(deck), bob.draw(deck)
    # # bob.show_hand()

def take_bet(credits):
    while True:
        try:
            credits.bet = int(input("How much would you like to bet? "))
        except ValueError:
            print("Sorry, you must enter an integer")
        else:
            if credits.bet > credits.total:
                print("Sorry, you do not have enough credits to make this bet")
            else:
                break
    
main()