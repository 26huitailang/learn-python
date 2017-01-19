t = int(input())
for i in range(t):
    ss = ''
    s = raw_input()
    for j in range(0, int(len(s) / 2), 2):
        ss += s[j]
    print ss
