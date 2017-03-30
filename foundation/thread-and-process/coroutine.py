import time


def consumer():
    r = ''
    while True:
        # 先执行yiled表达式，consumer暂停，n此时还未赋值
        # 跳转到produce的n=0继续执行，直到send的参数作为yield r的值赋给n
        n = yield r # yield 表达式接收send()函数发出的参数
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        time.sleep(1)
        r = '200 OK'


def produce(c):
    # 启动生成器，让它处于暂停的状态，跳转到consumer()，这样才能接受send的参数
    c.__next__()
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        # send()的参数作为yield表达式的值赋给等号左边
        # consumer再次执行到yield时，从send的下一行开始执行
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


if __name__ == '__main__':
    c = consumer()
    produce(c)
