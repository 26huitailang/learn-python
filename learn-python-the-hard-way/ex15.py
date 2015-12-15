# -*- coding: utf8 -*-
from sys import argv #import the sys module

script, filename = argv #unpack argv

txt = open(filename) # open a file object

print "Here's your file %r:" % filename #print prompt
print txt.read() # read the file object
txt.close()

print "Type the filename again:"
file_again = raw_input("> ") # input filename by raw_input

txt_again = open(file_again) #open the file object

print txt_again.read() # read and print it out
txt_again.close()

# Above each line, write out in English what that line does.
# If you are not sure ask someone for help or search online. Many times searching for "python(巨蟒) THING" will find answers to what that THING does in Python. Try searching for "python open."
# I used the word "commands" here, but commands are also called "functions" and "methods." You will learn about functions and methods later in the book.
# Get rid of the lines 10-15 where you use raw_input and run the script again. raw_input will interupt the program.
# Use only raw_input and try the script that way. Why is one way of getting the filename better than another? raw_input will interupt the program.
# Start python to start the python shell, and use open from the prompt(敏捷的) just like in this program. Notice how you can open files and run read on them from within python?
# Have your script also call close() on the txt and txt_again variables(变量). It's important to close files when you are done with them.
