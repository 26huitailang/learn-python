#!/usr/bin/python
# -*- coding: utf-8 -*-

class Engine(object):

    def __init__(self, room_map):
        self.room_map = room_map

    def play(self):
        current_room = self.room_map.opening_room()
        last_room = self.room_map.next_room('testroom')

        while current_room != last_room:
            next_room_name = current_room.enter()
            current_room = self.room_map.next_room(next_room_name)

        # be sure to print out the last room
        current_room.choose()

class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

class StartRoom(Room):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {'west': 'trees', 'down': 'dungeon'}

    def choose(self):
        direction = raw_input("> ")

        if direction == "west":
            print self.go(direction)
            return self.go(direction)
        elif direction == "down":
            print self.go(direction)
            return self.go(direction)
        else:
            print self.go(direction)
            return 'startroom'

class Trees(Room):
    pass

class Dungeon(Room):
    pass

class GoldRoom(Room):
    pass

class TestRoom(Room):
    pass

class Map(object):
    rooms = {
        'startroom': StartRoom("StartRoom", "U are in Start Room. There's two ways: West or Down"),
        'trees': Trees("Trees", "U are in Start Room. There's two ways: West or Down"),
        'dungeon': Dungeon("Dungeon", "U are in Start Room. There's two ways: West or Down"),
        'goldroom': GoldRoom("GoldRoom", "U are in Start Room. There's two ways: West or Down"),
        'testroom': TestRoom("TestRoom", "U are in Start Room. There's two ways: West or Down")
    }

    def __init__(self, start_room):
        self.start_room = 'startroom'

    def next_room(self, room_name):
        val = Map.rooms.get(room_name)
        return val

    def opening_room(self):
        return self.next_room(self.start_room)