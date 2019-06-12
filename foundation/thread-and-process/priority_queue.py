"""
优先队列，队列可以用于线程通信
"""
import heapq
import threading


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._count = 0
        self._cv = threading.Condition()

    def put(self, item, priority):
        with self._cv:
            # 利用heapq实现优先队列
            heapq.heappush(self._queue, (-priority, self._count, item))
            self._count += 1
            self._cv.notify()  # 通知wait()的线程继续

    def get(self):
        with self._cv:
            while len(self._queue) == 0:
                self._cv.wait()  # 等待notify() 通知
            return heapq.heappop(self._queue)


def producer(out_q):
    running = list(range(100))
    while running:
        data = running.pop()
        out_q.put(data, data)


def consumer(in_q):
    while True:
        data = in_q.get()
        print(data)


def main():
    q = PriorityQueue()
    t1 = threading.Thread(target=consumer, args=(q,))
    t2 = threading.Thread(target=producer, args=(q,))
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()
