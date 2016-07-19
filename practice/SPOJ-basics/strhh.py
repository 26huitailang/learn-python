def ch_out(characters):
    chs = ''
    l = len(characters)/2
    n = 0
    while n <= l:
        chs += characters[n]
        n += 2
    return chs

t = int(input())

while t > 0:
    ch_in = raw_input()
    chs = ch_out(ch_in)
    print chs
    t -= 1
