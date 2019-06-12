"""
直接运行异步函数，会返回一个coroutine对象，需要send方法来返回结果，因为生成器/协程在正常返回退出时会抛出一个StopIteration异常，而原来的返回值会存放在StopIteration对象的value属性中，通过except捕获可以获取协程真正的返回值。

所以，写一个run方法来驱动协程函数
"""
def run(coroutine):
    try:
        coroutine.send(None)
    except StopIteration as e:
        return e.value


async def async_function():
    return 1


async def await_coroutine():
    result = await async_function()
    print(result)


run(await_coroutine())
