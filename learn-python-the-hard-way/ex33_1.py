i = 0
numbers = []

# while i < 6:
    # print "At the top i is %d" % i
    # numbers.append(i)

    # i = i + 1
    # print "Numbers now: ", numbers
    # print "At the bottom i is %d" % i
    
a = int(raw_input("Input a distance between 0 and 100: "))
# b = int(raw_input("Input the step distance: "))
for i in range(0, 100):
    if i < a:
        numbers.append(i)
        print "Numbers now: ", numbers


print "The numbers: "

for num in numbers:
    print num