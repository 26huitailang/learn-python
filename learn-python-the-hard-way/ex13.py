from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

#python ex13.py first second 3rd forth
#ValueError: too many values to unpack

#python ex13.py first
#ValueError: need more than 2 value to unpack