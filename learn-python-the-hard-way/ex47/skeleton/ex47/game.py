#!/usr/bin/python
# -*- coding: utf-8 -*-

class Engine(object):

    def __init__(self, room_map):
        self.room_map = room_map

    def play(self):
        current_room = self.room_map.start_room
        last_room = self.room_map.rooms['TestRoom']

        while current_room != last_room:
            print current_room.name + ',' + current_room.description
            direction_choice = raw_input("direction choice> ")
            next_room_name = current_room.go(direction_choice)
            if next_room_name == None:
                continue
            current_room = self.room_map.next_room(next_room_name)

        # be sure to print out the last room
        print current_room.name + ',' + current_room.description
        print "U successedwest!"

class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    # 返回的是roomname
    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

class Map(object):

    startroom = Room("StartRoom", "You can go west and down a hole.")
    dungeon = Room("Dungeon", "UP")
    trees = Room("Trees", "East, UP")
    goldroom = Room("GoldRoom", "North")
    testroom = Room("TestRoom", "Finish")

    startroom.add_paths({'west': 'Trees', 'down': 'Dungeon'})
    dungeon.add_paths({'up': 'StartRoom'})
    trees.add_paths({'east': 'StartRoom', 'up': 'GoldRoom'})
    goldroom.add_paths({'north': 'TestRoom'})

    rooms = {
        'StartRoom': startroom,
        'Trees': trees,
        'Dungeon': dungeon,
        'GoldRoom': goldroom,
        'TestRoom': testroom
    }

    def __init__(self):
        self.start_room = self.rooms['StartRoom']

    # 返回rooms字典对应的函数
    def next_room(self, next_room_name):
        val = Map.rooms.get(next_room_name)
        return val

    # 打印描述信息
    # def opening_room(self, current):
    #     print current.description

# def run():
#     a_map = Map()
#     a_game = Engine(a_map)
#     a_game.play()
#
# run()