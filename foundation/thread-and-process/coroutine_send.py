def gen():
    a = yield 1 # 这个yield等号左边的赋值是send发送的参数，yield后面的1,是返回给send表达式左边的赋值，或者next()的赋值
    print('yield a % s' % a)
    b = yield 2
    print('yield b % s' % b)
    c = yield 3
    print('yield c % s' % c)


r = gen()
x = next(r)
print('next x %s' % x)
y = r.send(10)
print('next y %s' %y)
z = next(r)
print('next z %s' % z)