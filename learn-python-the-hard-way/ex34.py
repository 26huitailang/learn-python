animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
i = 0
for a in animals:
    print "%d: %s" % (i, a)
    i += 1

print """The animal at 1. %r
print "The third (3rd) animal. %r
print "The first (1st) animal. %r
The animal at 3. %r
The fifth (5th) animal. %r
The animal at 2. %r
The sixth (6th) animal. %r
The animal at 4. %r""" % (animals[1], animals[2], animals[0], animals[3], animals[4], animals[2], animals[5], animals[4])
