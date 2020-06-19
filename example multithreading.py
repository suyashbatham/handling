# Queue: this module implements multi-producer,multi-consumer queues.It specially used in thread programming
    #    when information musst be exchanged safely between multiple thread.There are 3 types of queue:
    #   1.Queue    2. LifoQueue  3.PriorityQueue
    #   exception which could be come :
    # 1. Full(queue overflow)       2.Empty(queue Underflow)

from queue import Queue

question_queue = Queue()
for x  in range(1,10):
    temp_dict = ('key',x)
    question_queue.put(temp_dict)  # put to add element

while(not question_queue.empty()):
    item = question_queue.get()  # get all the element from the queue
    print(str(item))

# Program: let's say you want to download several pages of a website and compile them into a single page.

# request module is used to fetch the pages anywhere from your python file
import requests
from threading import Thread
from queue import Queue

q = Queue(maxsize=20)
def put_page_to_q(page_num):
    q.put(requests.get('http://google.com/page_%s.html'%page_num))

def compile(q):
    if not q.full():
        raise ValueError
    else:
        print("Don't compiling")

threads = []
for page_num in range(20):
    t = Thread(target=put_page_to_q,args=(page_num,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
compile(q)
print(threads)
