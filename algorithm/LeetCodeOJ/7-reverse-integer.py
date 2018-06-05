def solution(x):
    if x > 2 ** 31 - 1 or x < -2 ** 31:
        return 0
    if x == 0:
        return x
    elif x > 0:
        r = int(str(x)[::-1])
        if r > 2 ** 31 - 1 or r < -2 ** 31:
            return 0
        return r
    elif x < 0:
        r = -int(str(-x)[::-1])
        if r > 2 ** 31 - 1 or r < -2 ** 31:
            return 0
        return r

if __name__ == '__main__':
    a = [(123, 321), (0, 0), (-123, -321), (210, 12), (1534236469, 0)]
    for item in a:
        r = solution(item[0])
        print(r, item[1])
