#1 Hint 
#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

from art import logo
import random
from replit import clear 

#def cards list

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# ACE
def if_ace(hand):   
    while 11 in hand and sum(hand) > 21:
        x = hand.index(11)
        hand[x] = 1
    
    return hand

# check more that 21? True or false
''' If sum(hand) > 21 return True, if sum(hand) <= False '''
def check_21(hand):
    if sum(hand) > 21:
        return True
    else:
        return False

# Win condition
def win_codition(player,dealer):
    
    player = sum(player)
    dealer = sum(dealer)
    
    if player > 21:
        return f"You have over 21, you lose"

    if dealer > 21:
        return f"Dealer have over 21, you win"
    
    if player == dealer:
        return f"Draw !"
    
    if player == 21:
        return f"You have 21! You win!"
    
    if dealer == 21:
        return f"Dealer have 21, you lose"

    if dealer > player:
        return f"Dealer have more point, you lose"

    if player > dealer:
     return f"You have more point, you win"
 
def printing_score(player,dealer):
        return f'''
Player hand: {player} Player score: {sum(player)}
Dealer hand: {dealer} Dealer score: {sum(dealer)}
'''

    
def game_on():
    
    # Creating player and dealer hand
    clear()
    print(logo)
        
    player_hand = random.sample(cards,2)
    dealer_hand = random.sample(cards,2)
    
    while True:
        if sum(if_ace(dealer_hand)) < 17:
            
            dealer_hand.append(random.choice(cards))
            player_hand = if_ace(player_hand)
        else:
            break 
    
    while True:
    
        print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
        print(f"Computer's first card: {dealer_hand[0]}")
 
        new_card = input("Draw another card ? 'y' or 'n'\n").lower()
        if new_card == 'y':
            player_hand.append(random.choice(cards))
            player_hand = if_ace(player_hand)
                 
            if check_21(player_hand):
                print(f'You have {player_hand}, current score: {sum(player_hand)} (over 21), you lose')
                break
        elif new_card == 'n':
            print(printing_score(player_hand,dealer_hand))
            print(win_codition(player_hand,dealer_hand))
            break
        
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == 'y':
        game_on()

game_on()
