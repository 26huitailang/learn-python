#-*-coding: utf8 -*-

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
target.write("%r\n%r\n%r\n" % (line1, line2, line3))

print "And finally, we close it."
target.close()

# If you open the file with 'w' mode, then do you really need the target.truncate()? Read the documentation(文件材料) for Python's open function and see if that's true.
# 1、使用'W'，文件若存在，首先要清空，然后（重新）创建，

# 2、使用'a'模式 ，把所有要写入文件的数据都追加到文件的末尾，即使你使用了seek（）指向文件的其他地方，如果文件不存在，将自动被创建。