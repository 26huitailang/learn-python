#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint

# class Engine(object):
#
#     def __init__(self, start_scene):
#         self.start_scene = start_scene
#         print self.start_scene.name
#         print self.start_scene.description
#
#     def play(self):
#         current_scene = self.start_scene
#         # choice = raw_input('> ')
#
#         while current_scene.name != "The End":
#             if current_scene.name == "death":
#                 break
#             choice = raw_input('> ')
#             try:
#                 num = int(choice)
#                 if current_scene.name == "Laser Weapon Armory":
#                     if num == 132:
#                         current_scene = current_scene.go(choice)
#                         print current_scene.name
#                         print current_scene.description
#                     else:
#                         current_scene = current_scene.go('*')
#                         print current_scene.name
#                         print current_scene.description
#                 elif current_scene.name == "Escape Pod":
#                     if num == 2:
#                         current_scene = current_scene.go(choice)
#                         print current_scene.name
#                         print current_scene.description
#                     else:
#                         current_scene = current_scene.go('*')
#                         print current_scene.name
#                         print current_scene.description
#
#             except ValueError:
#                 if choice in current_scene.paths.keys():
#                     current_scene = current_scene.go(choice)
#                     print current_scene.name
#                     print current_scene.description


class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

central_corridor = Room("Central Corridor",
"""
The Gothons of Planet Percal #25 have invaded your ship and destroyed
your entire crew.  You are the last surviving member and your last
mission is to get the neutron destruct bomb from the Weapons Armory,
put it in the bridge, and blow the ship up after getting into an
escape pod.

You're running down the central corridor to the Weapons Armory when
a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume
flowing around his hate filled body.  He's blocking the door to the
Armory and about to pull a weapon to blast you.
""")

laser_weapon_armory = Room("Laser Weapon Armory",
"""
Lucky for you they made you learn Gothon insults in the academy.
You tell the one Gothon joke you know:
Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.
The Gothon stops, tries not to laugh, then busts out laughing and can't move.
While he's laughing you run up and shoot him square in the head
putting him down, then jump through the Weapon Armory door.

You do a dive roll into the Weapon Armory, crouch and scan the room
for more Gothons that might be hiding.  It's dead quiet, too quiet.
You stand up and run to the far side of the room and find the
neutron bomb in its container.  There's a keypad lock on the box
and you need the code to get the bomb out.  If you get the code
wrong 10 times then the lock closes forever and you can't
get the bomb.  The code is 3 digits.
""")

the_bridge = Room("The Bridge",
"""
The container clicks open and the seal breaks, letting gas out.
You grab the neutron bomb and run as fast as you can to the
bridge where you must place it in the right spot.

You burst onto the Bridge with the netron destruct bomb
under your arm and surprise 5 Gothons who are trying to
take control of the ship.  Each of them has an even uglier
clown costume than the last.  They haven't pulled their
weapons out yet, as they see the active bomb under your
arm and don't want to set it off.
""")

escape_pod = Room("Escape Pod",
"""
You point your blaster at the bomb under your arm
and the Gothons put their hands up and start to sweat.
You inch backward to the door, open it, and then carefully
place the bomb on the floor, pointing your blaster at it.
You then jump back through the door, punch the close button
and blast the lock so the Gothons can't get out.
Now that the bomb is placed you run to the escape pod to
get off this tin can.

You rush through the ship desperately trying to make it to
the escape pod before the whole ship explodes.  It seems like
hardly any Gothons are on the ship, so your run is clear of
interference.  You get to the chamber with the escape pods, and
now need to pick one to take.  Some of them could be damaged
but you don't have time to look.  There's 5 pods, which one
do you take?
""")

the_end_winner = Room("The End",
"""
You jump into pod 2 and hit the eject button.
The pod easily slides out into space heading to
the planet below.  As it flies to the planet, you look
back and see your ship implode then explode like a
bright star, taking out the Gothon ship at the same
time.  You won!
""")

the_end_loser = Room("The End",
"""
You jump into a random pod and hit the eject button.
The pod escapes out into the void of space, then
implodes as the hull ruptures, crushing your body
into jam jelly.
"""
)

good_pod = randint(1,5)
# guess = raw_input("[pod #]> ")

escape_pod.add_paths({
    good_pod: the_end_winner,
    '*': the_end_loser
})

quips = [
        "You died.  You kinda suck at this.",
         "Your mom would be proud...if she were smarter.",
         "Such a luser.",
         "I have a small puppy that's better at this."
    ]

generic_death = Room("death", quips)

the_bridge.add_paths({
    'throw the bomb': generic_death,
    'slowly place the bomb': escape_pod
})

code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
# guess = raw_input("[keypad]> ")
# guesses = 0
#
# while guess != code and guesses < 10:
#             print "BZZZZEDDD!"
#             guesses += 1
#             guess = raw_input("[keypad]> ")
# guesses = 0
laser_weapon_armory.add_paths({
    code: the_bridge,
    '*': generic_death
})

central_corridor.add_paths({
    'shoot!': generic_death,
    'dodge!': generic_death,
    'tell a joke': laser_weapon_armory
})



START = central_corridor