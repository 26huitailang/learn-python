# 练习极客时间的算法与数据结构

## 细节

- 在写链表的各种操作时，一定要搞清楚引用（指针）关系，否则始终是理解不了的
  - 比如p.next.next，应该是p节点下一个节点的引用
  - 很多操作引用的操作都会引入中间变量，避免操作引用之后链表结构变化带来后续的不可知的错误

## 关于链表反转的尾递归

pyhton没有真正的尾递归，网上有人用装饰器实现了类似的效果。[参考](http://python.jobbole.com/86937/)

也看到一个用generator特性来实现的方法，觉得更易理解一些。思路就是将尾递归中的`return`改为`yield`，这样函数的返回变成了一个迭代器，再构建一个方法来返回迭代器最后的结果即可。

```py
import types


def tramp(gen, *args, **kwargs):
    # 执行generator到最后的结果
    # 这里是用来实现尾递归的效果
    g = gen(*args, **kwargs)
    while isinstance(g, types.GeneratorType):
        g = next(g)  # python3 version, python2 is g.next()
    return g
```

e.g., 详见[./single_linked_list.py](./single_linked_list.py)

    link = tramp(tail_recursion, None, head)
