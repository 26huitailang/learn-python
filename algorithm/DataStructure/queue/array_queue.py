#!/usr/bin/env python
# coding=utf-8


class ArrayQueue(object):

    def __init__(self, max_length):
        self.items = [None for _ in range(max_length)]
        self.max_length = max_length
        self.head = 0
        self.tail = 0

    def enqueue(self, item) -> bool:
        # 入队
        if self.tail == self.max_length:
            if self.head == 0:  # 整个队列已经占满
                return False
            # 数据搬移，整体前移head下标个单位，head指向0
            for i in range(self.head, self.tail):
                self.items[i-self.head] = self.items[i]
            self.tail -= self.head
            self.head = 0
        # 如果前面有空
        self.items[self.tail] = item
        self.tail += 1
        return True

    def dequeue(self):
        # 出队
        if self.head == self.tail:
            return None
        item = self.items[self.head]
        self.head += 1  # 这里是移动head指针，如果去操作列表会导致额外的数据搬移，当tail到达队尾的时候才进行数据搬移
        return item


def test():
    q = ArrayQueue(5)
    for i in range(5):
        q.enqueue(i)
    print(q.items)
    assert q.dequeue() == 0
    assert q.head == 1
    assert q.tail == 5
    q.enqueue(5)
    print(q.items)
    return


if __name__ == '__main__':
    test()
