#!/usr/bin/env python
# coding: utf-8


def get_coins(dollar):
    coins = (1, 5, 10, 25)
    nums = 0
    for coin in coins[::-1]:
        # print(coin)
        if dollar / coin > 0:
            nums += dollar / coin
            dollar = dollar % coin
        else:
            continue
    return nums


def test():
    dollar = input("Dollar: ")
    nums = get_coins(int(dollar))
    print("Min: %d" % nums)


if __name__ == '__main__':
    test()
