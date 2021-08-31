from math import nan
from . import card
import random

class Deck:


    def __init__( self ):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.cards = []
        self.hands = {}
        self.usedCards = []

        for s in suits:
            for i in range(1,14):
                str_val = ""
                if i == 1:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append( card.Card( s , i , str_val ) )

    def refreshDeck(self):
        suits = ["spades", "hearts", "clubs", "diamonds"]
        self.cards = []

        for s in suits:
            for i in range(1, 14):
                str_val = ""
                if i == 1:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append(card.Card(s, i, str_val))

    def show_cards(self):
        for card in self.cards:
            card.card_info()

    def newHand(self, num, player):
        self.hands[player] = []
        self.hands[player + 'points'] = 0
        for x in range(0,num):
            currentCard = random.randint(0,len(self.cards)-1)
            # if currentCard in self.usedCards:
            #     num = num+1
            #     continue
            self.hands[player].append(self.cards[currentCard])
            self.cards.pop(currentCard)
            # self.usedCards.append(currentCard)
        # print(self.usedCards)
    def showHand(self, player):
        print(self.hands[player])
    def fight(self, player, currentCard):
        if(self.hands[player][currentCard].point_val > self.hands["computer"][currentCard].point_val):
            print("%s's %s of %s won against the enemy %s of %s!" %(
                player, self.hands[player][currentCard].string_val, self.hands[player][currentCard].suit, self.hands['computer'][currentCard].string_val, self.hands['computer'][currentCard].suit))
            self.hands[player + 'points'] += 1
            self.hands['computerpoints'] -= 1
        elif(self.hands[player][currentCard].point_val == self.hands["computer"][currentCard].point_val):
            print("%s's %s of %s tied against the enemy %s of %s!" %(
                player, self.hands[player][currentCard].string_val, self.hands[player][currentCard].suit, self.hands['computer'][currentCard].string_val, self.hands['computer'][currentCard].suit))
        else:
            print("%s's %s of %s lost against the enemy %s of %s!" % (
                player, self.hands[player][currentCard].string_val, self.hands[player][currentCard].suit, self.hands['computer'][currentCard].string_val, self.hands['computer'][currentCard].suit))
            self.hands[player + 'points'] -= 1
            self.hands['computerpoints'] += 1
        print(self.hands[player + 'points'])

