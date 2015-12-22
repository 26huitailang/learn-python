# -*- coding: utf-8 -*-

people = 50
cats = 30
dogs = 60

if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"
    
dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."
    
if people <= dogs:
    print "People are less than or equal to dogs."
    
if people == dogs:
    print "People are dogs."
    
if 0 and 2:
    print "T"
    
if 1 and 2:
    print "T"

# What do you think the if does to the code under it? Condition judge, true runs it, false not
# Why does the code under the if need to be indented four spaces? typing style, codes belong to the certain if-statement, easy to look
# What happens if it isn't indented? doesn't matter
# Can you put other boolean expressions from Exercise 27 in the if-statement? Try it.
# What happens if you change the initial values for people, cats, and dogs?

    
