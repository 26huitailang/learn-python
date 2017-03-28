# coding: utf-8

def calc(expression):
    if '+' in expression:
        n1, n2 = expression.split('+')
        n1 = int(n1)
        n2 = int(n2)
        return print("n1 + n2 = %d" % (n1 + n2))
    if '-' in expression:
        n1, n2 = expression.split('-')
        n1 = int(n1)
        n2 = int(n2)
        return print("n1 - n2 = %d" % (n1 - n2))
    if '**' in expression:
        n1, n2 = expression.split('**')
        n1 = int(n1)
        n2 = int(n2)
        return print("n1 ** n2 = %d" % (n1 ** n2))
    if '*' in expression:
        n1, n2 = expression.split('*')
        n1 = int(n1)
        n2 = int(n2)
        return print("n1 * n2 = %d" % (n1 * n2))
    if '/' in expression:
        n1, n2 = expression.split('/')
        n1 = int(n1)
        n2 = int(n2)
        return print("n1 / n2 = %d" % (n1 / n2))


if __name__ == '__main__':
    e = input("expression> ")
    calc(e)
