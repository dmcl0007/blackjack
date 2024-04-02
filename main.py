import json
import colorama as color

color.init()
resetcolor = color.Fore.RESET

facecards = [
    [1], # ACE
    [11], # JACK
    [12], # QUEEN
    [13] # KING
]

data = []

for x in range(13):
    for y in range(4):
        if y == 0: suit = 'Spades'
        elif y == 1: suit = 'Clubs'
        elif y == 2: suit = 'Hearts'
        elif y == 3: suit = 'Diamonds'

        data.append([[x + 1], [suit]])

for i in data:
    cardcolor = resetcolor
    symbol = ''

    suit = str(i[1]).replace("[", "").replace("]", "").replace("'", "")
    rank = int(str(i[0]).replace("[", "").replace("]", ""))

    if suit  == "Spades": symbol = '♠'; cardcolor = color.Fore.BLACK
    elif suit == "Clubs": symbol = '♣'; cardcolor = color.Fore.LIGHTBLACK_EX
    elif suit == "Hearts": cardcolor = color.Fore.LIGHTRED_EX; symbol = '♥'
    elif suit == "Diamonds": cardcolor = color.Fore.RED; symbol = '♦'

    print(f'{rank} {cardcolor}{symbol}{resetcolor}')