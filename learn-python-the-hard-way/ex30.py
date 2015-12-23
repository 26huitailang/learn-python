people = 30
cars = 40
trucks = 10

if cars > people and trucks * 2 < people:
    print "We should take the cars, also the trucks are not enough."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."
