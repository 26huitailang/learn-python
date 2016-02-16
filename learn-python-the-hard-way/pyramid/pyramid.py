#!/usr/bin/python
# -*- coding: utf-8 -*-

'''

'''
import random

class Cards(object):
    def a_pack_cards(self): # open a new pack of cards , it's in order
        cards = []
        faces = [chr(6), chr(3), chr(5), chr(4)] #['Spades', 'Hearts', 'Clubs', 'Diamonds']
        numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        for face in faces:
            for number in numbers:
                card = face + number
                cards.append(card)
                # print card
        return cards
        
    def to_shuffle(self,cards): #shuffle the card with 52 numbers, make a dict
        order = [i for i in range(0,52)]
        # print order
        random.shuffle(order)
        # print order
        new_order_cards = dict(zip(order, cards)) # make these a dict
        # print new_order_cards
        return new_order_cards
    
    def to_get_card(self):
        pass
        

class Pyramid(object):
    def __init__(self, start_hierarchy):
        # self.start_hierarchy = start_hierarchy
        pass
        
cards = Cards()
deck = cards.a_pack_cards()
shuffle_order_cards = cards.to_shuffle(deck)
new_deck = []
for i in range(0,len(shuffle_order_cards)):
    print "%d: %s" % (i, shuffle_order_cards[i])
    new_deck.append(shuffle_order_cards[i])
print new_deck