from nose.tools import *
from ex47.game import *

def test_room():
    startroom = StartRoom("StartRoom", "U are in Start Room. There's two ways: West or Down")
    assert_equal(startroom.name, "StartRoom")
    print "Room worked well!"
    assert_equal(startroom.paths, {'west': 'trees', 'down': 'dungeon'})
    print "Paths well: %s" % startroom.paths

def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)