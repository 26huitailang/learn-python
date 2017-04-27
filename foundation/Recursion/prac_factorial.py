# coding: utf-8
def factorial(n):
    # 0! = 1! = 1
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == '__main__':
    factorial(5)
