#!/usr/bin/env python
# coding=utf-8

class ArrayStack(object):

    def __init__(self, max_length):
        self.items = [None for _ in range(max_length)]
        self.max_length = max_length
        self.count = 0

    def push(self, item) -> bool:
        if self.count == self.max_length:
            return False

        self.items.append(item)
        self.count += 1
        return True

    def pop(self):
        if self.count == 0:
            return None
        item = self.items.pop()
        self.count -= 1
        return item


def test():
    stack = ArrayStack(max_length=10)
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.pop() == 1

if __name__ == '__main__':
    test()

