tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print "\r"
print "\r"
print "\r"
print persian_cat
print backslash_cat
print fat_cat

# Remember the %r format? Combine %r with double-quote and single-quote escapes and print them out. Compare %r with %s. Notice how %r prints it the way you'd write it in your file, but %s prints it the way you'd like to see it?
goodday = "I said: \"What a good day!\""
print "I said: \"What a good day!\""
print "%r" % goodday

# comma after print makes the print continuous, \r go back to the first col of the same line
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i, #comma after print makes the print continuous, \r go back to the first col of the same line