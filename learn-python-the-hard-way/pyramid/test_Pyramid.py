hchy = int(raw_input())
rows = hchy
cols = hchy * 2 - 1

pyramid = [[0 for col in range(cols)] for row in range(rows)]        
# print pyramid
for row in range(0,rows):
    for col in range(0, cols):
        print pyramid[row][col]
    print '\n'