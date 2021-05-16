
import os
import random

class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value
    
    def show(self):
        print("{} {} {}".format(self.rank, self.suit, self.value))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ['♡', '♧', '♢', '♤']:
            for r in range(1, 14):
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
    
    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        random.shuffle(self.cards)

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

    def reset(self):
        self.value = 0
        self.hand = []

    def draw(self, deck):
        result = deck.deal()
        self.hand.append(result[0])
        if result[2] == 'A':
            if self.value + result[1] > 21:
                self.value += 1
        else:
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
    global playing

    clear()
    print("Welcome to Blackjack ♡ ♧ ♢ ♤\nGet as close as you can to 21 without going over.")
    print("House Rules:\n 1. Aces are 1 or 11\n 2. Dealer draws until 18\n 3. Start with 2000 credits")

    deck = Deck()
    deck.shuffle()

    credits = Credits()

    while True:
        final = False
        dealer = Player("Dealer")
        dealer.draw(deck), dealer.draw(deck)
        player = Player("Player")
        player.draw(deck), player.draw(deck)

        bet(credits)

        show_cards(dealer, player, final)

        while playing:
            hit_stand(player, deck)

            show_cards(dealer, player, final)

            if player.value > 21:
                print("Player busts!")
                credits.lose()
                break
            elif player.value == 21:
                print("Player wins!")
                credits.win()
            
        if player.value < 21:
            while dealer.value < 18:
                dealer.draw(deck)

                if dealer.value > 18:
                    final = True

                show_cards(dealer, player, final)

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

        print(f"Player winnings: {credits.total}")

        if credits.total > 0:
            new_game = input("Would you like to play again? (y/n)").lower()
        else:
            print("You are out of credits. Thanks for playing.")
            break

        if new_game == 'y' or new_game == 'yes':
            clear()
            playing = True
            continue
        else:
            print("Thanks for playing.")
            break

def show_cards(dealer, player, final):
    clear()
    print(credits)
    print("Dealer: ")
    print(dealer.value)
    if final == True: 
        dealer.player_hand()
    else:
        dealer.dealer_hand()
    print("")
    print("Player: ")
    print(player.value)
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

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
main()