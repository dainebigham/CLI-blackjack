
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
        card_value = single_card.value
        return single_card, card_value

class Player:
    def __init__(self, name):
        self.name = name
        self.value = 0
        self.hand = []

    def draw(self, deck):
        result = deck.deal()
        self.hand.append(result[0])
        self.value += result[1]
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

playing = True

def main(): 

    print("Welcome to Blackjack ♡ ♧ ♢ ♤\nGet as close as you can to 21 without going over.")
    print("House Rules:\n 1. Aces are 1 or 11\n 2. ")

    deck = Deck()
    deck.shuffle()

    dealer = Player("Dealer")
    dealer.draw(deck), dealer.draw(deck)
    player = Player("Player")
    player.draw(deck), player.draw(deck)

    credits = Credits()
    bet(credits)

    show_cards(dealer, player)

    while playing:
        hit_stand(player, deck)

        show_cards(dealer, player)

        if player.value > 21:
            print("Player busts!")
            credits.lose()
            break
        
    if player.value <= 21:
        while dealer.value < 21:
            dealer.draw(deck)

    show_cards(dealer, player)

    if dealer.value > 21:
        print("Dealer busts!")
        credits.win()
    elif dealer.value > player.value:
        print("Dealer wins!")
        credits.lose()
    elif player.value > dealer.value:
        print("Player wins!")
        credits.win()
    else:
        print("Push! Dealer and player tie.")

def show_cards(dealer, player):
    print("Dealer: ")
    dealer.dealer_hand()
    print("")
    print("Player: ")
    player.player_hand()

def hit_stand(player, deck):
    global playing

    while True:
        move = input("(H)it or (S)tand? ").lower()

        if move == 'h' or move == 'hit':
            player.draw(deck)
        elif move == 's' or move == 'stand':
            print("Player stands, dealer is still playing.")
            playing = False
        else:
            print("Sorry, try again.")
            continue
        break

def bet(credits):
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