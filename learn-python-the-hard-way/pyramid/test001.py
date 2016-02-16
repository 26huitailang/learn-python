#!/usr/bin/python
# -*- coding: utf-8 -*-

'''

'''
import random

class Cards(object):
    def __init__(self):
        self.cards = []
        self.values = {}
        faces = [chr(6), chr(3), chr(5), chr(4)] #['Spades', 'Hearts', 'Clubs', 'Diamonds']
        numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        for face in faces:
            for number in numbers:
                card = face + number
                self.cards.append(card)
                if number == '2' or number == '3' or number == '4' or number == '5' or number == '6' or number == '7' or number == '8' or number == '9' or number == '10':
                    self.values[card] = int(number)
                elif number == 'J':
                    self.values[card] = 11
                elif number == 'Q':
                    self.values[card] = 12
                elif number == 'K':
                    self.values[card] = 13
                elif number == 'A':
                    self.values[card] = 14
                
    def to_shuffle(self, cards): #shuffle the card with 52 numbers, make a dict
        order = [i for i in range(0,52)]
        # print order
        random.shuffle(order)
        # print order
        cards_order = dict(zip(order, cards)) # make these a dict
        # print new_order_cards
        return cards_order
    
    def to_get_card(self):
        pass
        
    def to_judge(self):
        pass

class Pyramid(object):
    def __init__(self, hierarchy):
        self.hierarchy = hierarchy
        graph = {'D': ['B'], 'E': ['B', 'C'], 'F': ['C'], 'B': ['A'], 'C': ['A']}
    
    def find_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return None
        

a_new_pack_cards = Cards()
cards_order = a_new_pack_cards.to_shuffle(a_new_pack_cards.cards)
print a_new_pack_cards.cards
print cards_order
# print a_new_pack_cards.values
for key in cards_order.keys():
    print "order %d, face %s, value %d" %(key, cards_order[key], a_new_pack_cards.values[cards_order[key]])

# deck = cards.a_pack_cards()
# shuffle_order_cards = cards.to_shuffle(deck)
# new_deck = []
# for i in range(0,len(shuffle_order_cards)):
    # print "%d: %s" % (i, shuffle_order_cards[i])
    # new_deck.append(shuffle_order_cards[i])
# print new_deck



