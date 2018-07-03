import gevent

def win():
    return 'You win!'

def fail():
    raise Exception('You failed!')

winner = gevent.spawn(win)
loser = gevent.spawn(fail)

print(winner.started)  # True
print(loser.started)  # True

# 在Greenlet中发生的异常，不会被抛到Greenlet外面。
# 控制台会打出Stacktrace，但程序不会停止
try:
    gevent.joinall([winner, loser])
except Exception as e:
    # 这段永远不会被执行
    print('This will never be reached')

print(winner.ready()) # True
print(loser.ready())  # True

print(winner.value)  # 'You win!'
print(loser.value)  # None

print(winner.successful())  # True
print(loser.successful())  # False

# 这里可以通过raise loser.exception 或 loser.get()
# 来将协程中的异常抛出
print(loser.exception)
