"""
用栈实现队列的效果。

思路：用两个栈，一个input，一个output，入栈的时候放入input，出栈的时候检查output，为空的话将input的元素入栈到output，这样出去的顺序就是FIFO。
"""


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._input = []
        self._output = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self._input.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.move()
        if not self._output:
            return None
        return self._output.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        self.move()
        if not self._output:  # 出的栈为空，要从input栈调入
            return None
        return self._output[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self._input and not self._output

    def move(self):
        if not self._output:
            while self._input:
                self._output.append(self._input.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
