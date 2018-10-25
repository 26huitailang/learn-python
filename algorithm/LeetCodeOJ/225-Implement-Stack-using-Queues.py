#!/usr/bin/env python
# coding=utf-8
"""
队列实现栈，FILO

两个队列，实现一个size方法，pop和peek时，将一个队列放入另外一个，pop在最后一个元素时，不放入并弹出，peek返回后继续放入
"""


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        # 放入不为空的队列，如果都为空放入1
        if self.queue1:
            self.queue1.append(x)
        else:
            self.queue2.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.empty():
            return
        if self.queue1:
            self.queue2 = self.queue1[:-1]  # 切片是新的对象引用，不用copy
            val = self.queue1[-1]
            self.queue1.clear()
            return val
        elif self.queue2:
            self.queue1 = self.queue2[:-1]  # 切片是新的对象引用，不用copy
            val = self.queue2[-1]
            self.queue2.clear()
            return val

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.empty():
            return
        if self.queue1:
            self.queue2 = self.queue1[:]  # 切片是新的对象引用，不用copy
            val = self.queue1[-1]
            self.queue1.clear()
            return val
        elif self.queue2:
            self.queue1 = self.queue2[:]  # 切片是新的对象引用，不用copy
            val = self.queue2[-1]
            self.queue2.clear()
            return val

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.queue1 and not self.queue2


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
