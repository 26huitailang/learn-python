# coding: utf-8
"temperature_trans.py -- 一个温度装换的程序，支持C2F和F2C"


def c2f(temp):
    "摄氏度转华氏度"
    temp_transed = float(temp) * 9 // 5 + 32
    return temp_transed


def f2c(temp):
    "华氏度转摄氏度"
    temp_transed = (float(temp) - 32) * 5 // 9
    return temp_transed


def test():
    "test case"
    while 1:
        print("1. C2F")
        print("2. F2C")
        opt = input("Which? ")
        temp = int(input("How much? "))
        if opt == '1':
            temp_transed = c2f(temp)
        elif opt == '2':
            temp_transed = f2c(temp)
        else:
            print("Wrong choice.")
            continue
        print("After switching: %s" % temp_transed)


if __name__ == '__main__':
    test()
