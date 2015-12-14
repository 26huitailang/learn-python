x = "There are %d types of people." % 10 # format char's value in the end
binary = "binary" 
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) #format char can be the variables @a string is put inside a string

print x 
print y

print "I said: %r." % x # %r for what it stands for including the "", and " will be printed '" @a string is put inside a string
print "I also said: '%s'." % y #%s stands for the strings in y without "" @a string is put inside a string

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious #"Isn't that joke so funny?! %r" % hilarious @a string is put inside a string

w = "This is the left side of..."
e = "a string with a right side."

print w + e # This is the left side of...a string with a right side. 


# Go through this program and write a comment above each line explaining it.
# Find all the places where a string is put inside a string. There are four places.
# Are you sure there are only four places? How do you know? Maybe I like lying(说谎). No format characters used stand for the other strings.
# Explain why adding the two strings w and e with + makes a longer string. Python will judge the type of two variables, two stings + will make a longer string but no calculation.
