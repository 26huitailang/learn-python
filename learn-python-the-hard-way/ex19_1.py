# Write at least one more function of your own design, and run it 10 different ways.
def appending_txt(new_txt, filename):
    indata = open(filename, 'a')
    indata.write("\n")
    indata.write(new_txt)
    indata.close()

file = raw_input("What's the filename?\n> ")
user_input = raw_input("What do U want to appending?\n> ")

appending_txt(user_input, file)