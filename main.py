from colorama import init, Fore
from random import shuffle, choice
import time
from os import system
from sys import platform

init()
resetcolor = Fore.RESET

facecards = [
    [1], # ACE
    [11], # JACK
    [12], # QUEEN
    [13] # KING
]

deck = []
playerHand = []
dealerHand = []

def clear():
    if platform == 'win32':
        system('cls')
    else:
        system('clear')

def generateDeck():
    deck.clear()
    playerHand.clear()
    dealerHand.clear()

    for x in range(13):
        for y in range(4):
            if y == 0: suit = 'Spades'
            elif y == 1: suit = 'Clubs'
            elif y == 2: suit = 'Hearts'
            elif y == 3: suit = 'Diamonds'

            if x == 0: deck.append([['A'], [suit]])
            elif x == 10: deck.append([['J'], [suit]])
            elif x == 11: deck.append([['Q'], [suit]])
            elif x == 12: deck.append([['K'], [suit]])
            else: deck.append([[x + 1], [suit]])

def shuffleDeck():
    shuffle(deck)

def dealCard(plr, side):
    suit = str(deck[0][1]).replace("[", "").replace("]", "").replace("'", "")
    rank = str(deck[0][0]).replace("[", "").replace("]", "").replace("'", "")

    if plr == 'Dealer':
        dealerHand.append([[suit], [rank], [side]])
    else: 
        playerHand.append([[suit], [rank], [side]])

    del deck[0]

def printHands(show):
    clear()

    print("Dealers Hand:")
    for i in dealerHand:
        cardcolor = resetcolor
        symbol = ''
        suit = str(i[0]).replace("[", "").replace("]", "").replace("'", "")
        rank = str(i[1]).replace("[", "").replace("]", "").replace("'", "")
        side = str(i[2]).replace("[", "").replace("]", "").replace("'", "")

        if suit  == "Spades": symbol = '♠'; cardcolor = Fore.BLACK
        elif suit == "Clubs": symbol = '♣'; cardcolor = Fore.BLACK
        elif suit == "Hearts": cardcolor = Fore.RED; symbol = '♥'
        elif suit == "Diamonds": cardcolor = Fore.RED; symbol = '♦'

        if show == True: 
            print(f'{rank} {cardcolor}{symbol}{resetcolor}')
        else:
            if side == "Down":
                print("? ?")
            else:
                print(f'{rank} {cardcolor}{symbol}{resetcolor}')

    if len(dealerHand) != 0:
        print(f"Dealer Has {getTotal('Dealer', False)}.")

    print("\nYour Hand:")
    for i in playerHand:
        cardcolor = resetcolor
        symbol = ''
        suit = str(i[0]).replace("[", "").replace("]", "").replace("'", "")
        rank = str(i[1]).replace("[", "").replace("]", "").replace("'", "")

        if suit  == "Spades": symbol = '♠'; cardcolor = Fore.BLACK
        elif suit == "Clubs": symbol = '♣'; cardcolor = Fore.BLACK
        elif suit == "Hearts": cardcolor = Fore.RED; symbol = '♥'
        elif suit == "Diamonds": cardcolor = Fore.RED; symbol = '♦'

        print(f'{rank} {cardcolor}{symbol}{resetcolor}')
    
    if len(playerHand) != 0:
        print(f"You have {getTotal('Player', False)}.")

    time.sleep(1)

def getTotal(plr, show):
    if plr == 'Dealer':
        dealerCount = 0
        strCount = False
        for i in dealerHand:
            rank = str(i[1]).replace("[", "").replace("]", "").replace("'", "")
            side = str(i[2]).replace("[", "").replace("]", "").replace("'", "")

            if side == "Up" or show == True:
                if rank in['J', 'Q','K']:
                    dealerCount += 10
                elif rank not in ['J', 'Q', 'K', 'A']:
                    dealerCount += int(rank)
                elif rank == 'A':
                    if dealerCount + 11 > 21: 
                        dealerCount += 1
                    else: dealerCount += 11
            elif side == "Down" and show != True:
                strCount = True

        if strCount:
            return f'? + {dealerCount}'
        else:
            return dealerCount
        
    else: 
        playerCount = 0
        for i in playerHand:
            rank = str(i[1]).replace("[", "").replace("]", "").replace("'", "")
            if rank in ['J', 'Q','K']:
                playerCount += 10
            elif rank not in ['J', 'Q', 'K', 'A']:
                playerCount += int(rank)
            elif rank == 'A':
                if playerCount + 11 <= 21:
                    playerCount += 11
                else: playerCount += 1

        return playerCount

def endGame(winner):
    printHands(True)
    if winner == 'Dealer': print("\nThe Dealer Has Won.")
    elif winner == 'Player': print('\nYou Have Won.')
    elif winner == 'Tie': print('\nYou and The Dealer Tied.')

def compare():
    if getTotal('Dealer') > getTotal('Player'): endGame('Dealer')
    elif getTotal('Dealer') == getTotal('Player'): endGame('Tie')
    else: endGame('Player')

def stand():
    if getTotal('Dealer') == 17: compare()

    while getTotal('Dealer') < 21:
        if getTotal('Player') > getTotal('Dealer'):
            dealCard('Dealer', 'Up')
        elif getTotal('Player') < getTotal('Dealer'): compare(); break

        choices = ['Hit', 'Stand']
        if getTotal('Dealer') <= 16:
            x = choice(choices)
            if x == 'Hit': dealCard('Dealer', 'Up')
            else: compare(); break

def hit():
    dealCard('Player', 'Up')
    choice()

def choice():
    print("\nType 'H' to Hit\nType 'S' to Stand")
    
    while True:
        key = input("> ")
        if key.lower() == 's': stand(); break
        if key.lower() == 'h': hit(); break

    printHands(False)
                
def start():
    printHands(False)

    dealCard('Player', 'Up') # 1 card UP to PLAYER
    printHands(False)

    dealCard('Dealer', 'Down') # 1 card DOWN to DEALER
    printHands(False)

    dealCard('Player', 'Up') # 1 card UP to PLAYER
    printHands(False)

    dealCard('Dealer', 'Up') # 1 card UP to DEALER
    printHands(False)

    choice()

    

generateDeck()
shuffleDeck()

start()

