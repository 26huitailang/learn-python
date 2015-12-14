formatter = "%r %r %r %r" # four format chars in it

print formatter % (1, 2, 3, 4) #"%r %r %r %r" % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four") #"%r %r %r %r" % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)# %r in first formatter stands for one formatter followed
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)


# Do your checks, write down your mistakes, and try not to make the same mistakes on the next exercise.
# Notice that the last line of output uses both single-quotes and double-quotes for individual pieces. Why do you think that is?
# I recongonize that it is single-quotes while there is no ' or " in the word. 
