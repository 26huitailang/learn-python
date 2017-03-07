def loop():
    for i in range(10):
        yield pp(i)
    for j in ['a', 'b', 'c', 'd', 'e']:
        yield pp(j)


def pp(param):
    print(param)


if __name__ == '__main__':
    f = loop()
    while True:
        f.__next__()

