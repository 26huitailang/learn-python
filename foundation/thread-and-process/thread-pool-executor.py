import time
import random
import queue
from concurrent.futures import ThreadPoolExecutor

q = queue.Queue()


def task(name):
    count = 0
    while True:
        if count > 5:
            break
        # print('{} {}'.format(name, count))
        q.put((name, count))
        # time.sleep(random.randint(0, 5))
        time.sleep(random.random())
        count += 1
    return


def get_all_items_in_queue():
    while not q.empty():
        print(q.get())


def main():
    max_workers = 5
    with ThreadPoolExecutor(max_workers) as executor:  # 使用with，相当于executor.shutdown(wait=True)
        c = 0
        for i in range(20):
            exe = executor.submit(task, 'task-{}'.format(c))
            c += 1
        # tasks = list(range(20))
        # executor.map(task, tasks)
    get_all_items_in_queue()
    print('finish')


if __name__ == "__main__":
    main()
