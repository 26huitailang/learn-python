from nose.tools import *
from ex47.game import *

a_map = Map()
def test_room():
    # startroom = Room("StartRoom", "You can go west and down a hole.")
    # trees = Room("Trees", "Trees room in the west.")
    # dungeon = Room("Dungeon", "It's dark down here, you can go up.")
    assert_equal(a_map.startroom.name, "StartRoom")
    assert_equal(a_map.trees.name, "Trees")
    # assert_equal(dungeon.name, "Dungeon")
    # assert_equal(goldroom.name, "GoldRoom")
    # print "Room worked well!"
    assert_equal(a_map.startroom.paths, {'west': 'Trees', 'down': 'Dungeon'})
    assert_equal(a_map.dungeon.paths,{'up': 'StartRoom'})
    # trees.add_paths({'east': 'StartRoom', 'up': 'GoldRoom'})
    # goldroom.add_paths({'north': 'TestRoom'})
    # print "Paths well: %s" % startroom.paths

def test_room_paths():
    # startroom = Room("StartRoom", "You can go west and down a hole.")
    # trees = Room("Trees", "Trees room in the west.")
    # goldroom = Room("GoldRoom", "Gold room in the up.")
    # south = Room("South", "Test room in the south.")

    # trees.add_paths({'up': goldroom, 'east': startroom})
    assert_equal(a_map.trees.go('up'), 'GoldRoom')
    # assert_equal(center.go('south'), south)
    # print "Room Paths worked well!"

def test_map():
    # startroom = Room("StartRoom", "You can go west and down a hole.")
    # trees = Room("Trees", "Trees room in the west.")
    # dungeon = Room("Dungeon", "It's dark down here, you can go up.")

    # startroom.add_paths({'west': trees, 'down': dungeon})
    # trees.add_paths({'east': startroom})
    # dungeon.add_paths({'up': startroom})

    assert_equal(a_map.next_room('GoldRoom'), a_map.goldroom)
    # assert_equal(a_map.startroom.go('west').go('east'), a_map.startroom)
    # assert_equal(a_map.startroom.go('down').go('up'), a_map.startroom)