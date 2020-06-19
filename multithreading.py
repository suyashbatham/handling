# Multi Threading : it allows python programs to handle multiple functions at once as  opposed to running a
#                   sequence of command individually.

import threading

def foo():
    print("hello threading!")

my_thread = threading.Thread(target=foo)

# start a thread
my_thread.daemon = True
my_thread.start()


# threading.Thread (Thread is a class)

from threading import Thread
import time

class Sleepy(Thread):
    def run(self):
        time.sleep(5)
        print("Hello from this thread")

if __name__=="__main__":
    t = Sleepy()
    t.start()
    t.join()
    print("the main progrm countinues to run in the foreground")

import multiprocessing
import time

def someFun(i):
    return i*i

def otherFun(m,i):
    return m + i

def process():
    for i in range(100):
        result = 0
        for j in range(100000):
            result = otherFun(result,someFun(i))

if __name__=="__main":
    start = time.time()
    process()
    process()
    process()
    process()
    print("without using multi process took %.2fs"%(time.time()-start))

    start = time.time()
    processes = [multiprocessing.Process(target=process) for _ in range(4)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print("four multi process takes %.2fs" %(time.time()-start))


























