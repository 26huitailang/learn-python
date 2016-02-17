# hier = [i for i in range(0,7)]
h_in = int(raw_input("1-7> "))
tree = {}
for i in range(0,7):
    temp = []
    if i == 0:
        tree[i+1] = [0]
    elif i == 1:
        tree[i+1] = [1, 2]
    else:
        first = i * (i + 1) / 2
        for j in range(0, i + 1):
            temp.append(first + j)
        tree[i + 1] = temp

for k in tree.keys():
    print tree[k]
        
