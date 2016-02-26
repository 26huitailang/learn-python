#!/usr/bin/python
# -*- coding: utf-8 -*-

'''

'''
import random

# 定义类：扑克牌，具有一些扑克牌的属性，如洗牌、发牌、大小判断等
class Cards(object):

    # 初始化52张扑克牌，cards表示牌面，values表示牌对应的大小
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

    # 洗牌，shuffle the card with 52 numbers, make a dict
    def to_shuffle(self, cards):

        order = [i for i in range(0,52)]
        # print order
        random.shuffle(order)
        # print order
        cards_order = dict(zip(order, cards)) # make these a dict
        # print new_order_cards
        return cards_order

    # 发牌
    def to_get_card(self):
        pass

    #判定大小
    def to_judge(self):
        pass

# 金字塔类，
class Pyramid(object):

    # 初始化金字塔形状，依据用户输入的hierarchy
    def __init__(self, user_input_hierarchy, cards_order, cards):
        # self.hierarchy = hierarchy
        self.graph = {}
        self.graph[3] = {3: [1], 4: [1, 2], 5: [2], 1: [0], 2: [0]}
        self.graph[4] = {6: [3], 7: [3, 4], 8: [4, 5], 9: [5], 3: [1], 4: [1, 2], 5: [2], 1: [0], 2: [0]}
        self.pyramid = self.graph[user_input_hierarchy]

        self.start_stage = user_input_hierarchy

        self.init = {}
        self.cards_order = cards_order
        self.cards = cards
        self.counts = user_input_hierarchy * (user_input_hierarchy + 1) / 2 # 金字塔中的卡数
        self.rest_cards = [i for i in range(self.counts, 52)]
        r = [i for i in range(0 ,self.counts)]
        for i in r:
            self.init[i] = i
        print self.init

    # 游戏失败，并判定游戏是发牌继续，还是牌不够完成
    def fail(self, choose_id):
        print "Failed!"
        self.init[choose_id] = self.rest_cards.pop(0)
        print self.init
        print self.rest_cards
        self.pick_card()

    # 某次翻牌成功，游戏完成是finish
    def success(self):
        print "Good, next stop."

    # 游戏完成，通过顶端
    def finish(self):
        print "Congratulation!"
        return False

    # 一次游戏的行为，完成后判定成功、失败、完成三个状态
    def pick_card(self):
        choose_id = int(raw_input("To pick one> "))
        choose_card = self.init[choose_id]
        card_face = self.cards_order[choose_card]
        card_value = self.cards.values[card_face]
        print card_value
        if card_value > 9:
            self.fail(choose_id)
        # elif finish(self):
            # finish()
            # print "Finished!"
        else:
            self.success()

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

# 找到用户下一次的路径
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

# 引擎，判断游戏的运行状态
class Engine(object):
    def __init__(self, hierarchy):
        self.stage = hierarchy

# 测试函数，所有测试语句在这里，调用test()来执行
def test():
    cards = Cards()
    cards_order = cards.to_shuffle(cards.cards)
    print cards.cards
    print cards_order
    # print a_new_pack_cards.values
    for key in cards_order.keys():
        print "order %d, face %s, value %d" %(key, cards_order[key], cards.values[cards_order[key]])
    pyramid = Pyramid(4, cards_order, cards)
    paths = find_all_paths(pyramid.pyramid, 7, 0)
    print paths
    hierarchy = int(raw_input("Hierarchy u want> "))
    # pick_card(hierarchy, cards_order, cards)
    # a_game = Engine(hierarchy)
    # a_game.pick_card()
    pyramid.pick_card()

if __name__ == '__main__':
    test()





