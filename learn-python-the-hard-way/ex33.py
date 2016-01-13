i = 0
numbers = []

a = int(raw_input("Input a distance: "))
b = int(raw_input("Input the step distance: "))

while i < a:
    print "At the top i is %d" % i
    numbers.append(i)

    i += b
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num