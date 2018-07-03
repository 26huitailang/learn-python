from gevent import monkey; monkey.patch_all()
import gevent
from gevent.queue import Queue
 
products = Queue()
 
def consumer(name):
    while not products.empty():
        print('%s got product %s' % (name, products.get()))
        gevent.sleep(0)
 
    print('%s Quit' % name)
 
def a_con():
    t_list = []
    while True:
        a = products.get()
        t_list.append(a)
        print(len(t_list))

def producer():
    for i in range(1, 10):
        # products.put(i)
        pass

gevent.joinall([
    gevent.spawn(producer),
    gevent.spawn(a_con),
#    gevent.spawn(consumer, 'steve'),
#    gevent.spawn(consumer, 'john'),
#    gevent.spawn(consumer, 'nancy'),
])
