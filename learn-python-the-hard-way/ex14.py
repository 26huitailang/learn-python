#-*- coding: utf8 -*-
from sys import argv

script, user_name, password = argv
prompt = 'ans: '

if password != "123456":
    print "Wrong Password."
else:
    print "Go on!"

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

# 1. Find out what Zork and Adventure were. Try to find a copy and play it. A game use cmd.
# 2. Change the prompt variable(变量的) to something else entirely.
# 3. Add another argument and use it in your script, the same way you did in the previous exercise with first, second = ARGV.
# 4. Make sure you understand how I combined a """ style multiline string with the % format activator(催化剂) as the last print.
