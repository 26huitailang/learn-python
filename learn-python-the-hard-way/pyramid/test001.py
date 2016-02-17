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
        graph3 = {3: [1], 4: [1, 2], 5: [2], 1: [0], 2: [0]}
        graph4 = {3: [1], 4: [1, 2], 5: [2], 1: [0], 2: [0], 6: [3], 7: [3, 4], 8: [4, 5], 9: [5]}
        self.graph = graph4
        
    # def find_all_paths(self, graph, start, end, path=[]):
        # path = path + [start]
        # if start == end:
            # return [path]
        # if not graph.has_key(start):
            # return []
        # paths = []
        # for node in graph[start]:
            # if node not in path:
                # newpaths = find_all_paths(self, graph, node, end, path)
                # for newpath in newpaths:
                    # paths.append(newpath)
        # return paths
        
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

class Engine(object):
    def __init__(self, hierarchy, cards_order, cards):
    #初始化游戏参数
        self.init = {}
        # self.hierarchy = hierarchy
        self.cards_order = cards_order
        self.cards = cards
        self.hier = hierarchy * (hierarchy + 1) / 2
        # print h_temp
        self.next_card = [i for i in range(self.hier, 52)]
        r = [i for i in range(0 ,self.hier)]
        for i in r:
            self.init[i] = i
        print self.init
        
    def fail(self):
        print "Failed!"
        self.init[choose_id] = self.next_card.pop(0)
        print self.init
        print self.next_card
        pick_card()
        
    def success(self):
        print "Good, next stop."
        
    def finish(self):
        return False
        
    def pick_card(self):
        choose_id = int(raw_input("To pick one> "))
        choose_card = self.init[choose_id]
        card_face = self.cards_order[choose_card]
        card_value = self.cards.values[card_face]
        print card_value
        if card_value > 9:
            fail()
        # elif finish(self):
            # finish()
            # print "Finished!"
        else:
            success()
    

    
def test():
    cards = Cards()
    cards_order = cards.to_shuffle(cards.cards)
    print cards.cards
    print cards_order
    # print a_new_pack_cards.values
    for key in cards_order.keys():
        print "order %d, face %s, value %d" %(key, cards_order[key], cards.values[cards_order[key]])
    pyramid = Pyramid(4)
    paths = find_all_paths(pyramid.graph, 7, 0)
    print paths
    hierarchy = int(raw_input("Hierarchy u want> "))
    # pick_card(hierarchy, cards_order, cards)
    a_game = Engine(hierarchy, cards_order, cards)
    a_game.pick_card()
test()




