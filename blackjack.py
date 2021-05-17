
import os
import random

class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value
    
    # function to display the card on screen
    def show(self):
        print("{} {}".format(self.rank, self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    # function to build a deck of 52 cards, 4 suits
    def build(self):
        for s in ['♡', '♧', '♢', '♤']:
            for r in range(1, 14):
                # change the cards 11-14 to letters for royal suits and ace
                if r == 1:
                    self.cards.append(Card(s, 'A', 11))
                elif r == 11:
                    self.cards.append(Card(s, 'J', 10))
                elif r == 12:
                    self.cards.append(Card(s, 'Q', 10))
                elif r == 13:
                    self.cards.append(Card(s, 'K', 10))
                else:
                    self.cards.append(Card(s, r, r))
    
    # function to print the cards array that's holding the deck to screen
    def show(self):
        for c in self.cards:
            c.show()

    # shuffle the deck
    def shuffle(self):
        random.shuffle(self.cards)

    # function to deal a card from the deck, returning the card itself, its rank, and its value
    def deal(self):
        single_card = self.cards.pop()
        card_value = single_card.value
        card_rank = single_card.rank
        return single_card, card_value, card_rank

class Player:
    def __init__(self, name):
        self.name = name
        self.value = 0
        self.hand = []

    # function to draw a card from the deck
    def draw(self, deck):
        # variable to hold list of values from Decks deal method
        result = deck.deal()
        # place the card drawn in the players hand
        self.hand.append(result[0])
        # if the card drawn is an ace, check if adding it to hand causes value to go over 21
        # if not, Ace is 11, else it is 1
        if result[2] == 'A':
            if self.value + result[1] > 21:
                self.value += 1
            else:
                self.value += result[1]
        else:
            self.value += result[1]

        return self

    # function to display the dealers hand, keeping one hidden from player
    def dealer_hand(self):
        for i, card in enumerate(self.hand):
            if i == 0:
                print("<hidden>")
            else:
                card.show()

    # function print players hand to screen
    def player_hand(self):
        for card in self.hand:
            card.show()

# credits class to hold the players total credits and their bet
# removing bet from total if hand loses, else adding bet to total
class Credits:
    def __init__(self):
        self.total = 2000
        self.bet = 0

    def win(self):
        self.total += self.bet

    def lose(self):
        self.total -= self.bet

# global variable for game loop
playing = True

def main(): 
    global playing

    clear()
    print("Welcome to Blackjack ♡ ♧ ♢ ♤\nGet as close as you can to 21 without going over.")
    print("House Rules:\n 1. Aces are 1 or 11\n 2. Dealer draws until 18\n 3. Player starts with 2000 credits")

    # create and shuffle the duck
    deck = Deck()
    deck.shuffle()

    # initialize credits
    credits = Credits()

    # infinite game loop
    while True:
        # variable to check if this is the final hand 
        final = False

        # create player and dealer and draw two cards each
        dealer = Player("Dealer")
        dealer.draw(deck), dealer.draw(deck)
        player = Player("Player")
        player.draw(deck), player.draw(deck)

        # get players bet
        bet(credits)
        # print player and dealers cards to screen
        show_cards(dealer, player, final)

        # start game loop
        while playing:
            # ask player if they want to hit or stand
            hit_stand(player, deck)
            show_cards(dealer, player, final)

            # if player has gone over 21 player busts, loses their bet, and all cards are shown
            # else if player gets exactly 21 player wins their bet and all cards are shown
            if player.value > 21:
                final = True
                show_cards(dealer, player, final)
                print("Player busts!")
                credits.lose()
                break
            elif player.value == 21:
                final = True
                show_cards(dealer, player, final)
                print("Player wins!")
                credits.win()
                break
        
        # if player has stood on their hand the dealer draws until their value is over 18
        # once they're over 18, reveal all cards
        if player.value < 21:
            while dealer.value < 18:
                dealer.draw(deck)

                if dealer.value > 18:
                    final = True

                show_cards(dealer, player, final)

        # conditional block to check different win/lose scenarios
        if dealer.value > 21:
            print("Dealer busts!")
            credits.win()
        elif dealer.value > player.value:
            print("Dealer wins!")
            credits.lose()
        elif dealer.value < player.value and player.value < 21:
            print("Player wins!")
            credits.win()
        elif dealer.value == player.value:
            print("Push! Dealer and player tie.")

        # print player current winnings to screen
        print(f"Player winnings: {credits.total}")

        # if player is out of credits they lose and game ends
        # else ask if they want to play again
        if credits.total > 0:
            new_game = input("Would you like to play again? (y/n)").lower()
        else:
            print("You are out of credits. Thanks for playing.")
            break

        # continue infinite loop if new game selected, else break
        if new_game == 'y' or new_game == 'yes':
            clear()
            playing = True
            continue
        else:
            print("Thanks for playing.")
            break

# function to display current hands on screen
def show_cards(dealer, player, final):
    clear()
    print("Dealer: ")
    # check if it is the final hand and dealer needs to display all cards
    if final == True: 
        dealer.player_hand()
    else:
        dealer.dealer_hand()
    print("")
    print("Player: ")
    player.player_hand()

# function that asks if the player would like to hit or stand
def hit_stand(player, deck):
    global playing

    while True:
        move = input("(H)it or (S)tand? ").lower()

        # draw another card if hit, or exit if stand
        if move == 'h' or move == 'hit':
            player.draw(deck)
        elif move == 's' or move == 'stand':
            print("Player stands, dealer is still playing.")
            playing = False
        else:
            print("Sorry, try again.")
            continue
        break

# function to ask player for their bet
def bet(credits):
    while True:
        # ensure that player enter an integer and that they have enough remaining credits to make their bet
        try:
            credits.bet = int(input("How much would you like to bet? "))
        except ValueError:
            print("Sorry, you must enter an integer")
        else:
            if credits.bet > credits.total:
                print("Sorry, you do not have enough credits to make this bet")
            else:
                break

# function to clear the screen 
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
main()