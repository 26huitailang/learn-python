# print "How old are you?",
# age = raw_input() # raw_input with single-quotes, input without
# print "How tall are you?",
# height = raw_input()
# print "How much do you weigh?",
# weight = raw_input()
# sth = raw_input("Enter something here: ")

# other ways to use raw_input()
age = raw_input("How old are you?") # raw_input with single-quotes, input without
height = raw_input("How tall are you?")
weight = raw_input("How much do you weigh?")
#other ways to use raw_input()
sth = raw_input("Enter something here: ")
print "So, you're %r old, %r tall and %r heavy. Also, %r" % (
    age, height, weight, sth)