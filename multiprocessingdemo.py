import multiprocessing
import time
from random import randint

#countUp()
#countDown()

def countUp():
    i = 0
    while i<=3:
        print("Up: \t {}".format(i))
        time.sleep(randint(1,3))
        i+=1

def countDown():
    i = 3
    while i>=0:
        print("Count Down {} \t".format(i))
        time.sleep(randint(1,3))
        i-=1

if __name__=="__main___":
    # initiate the worker
    workdown = multiprocessing.Process(target=countDown())
    workup = multiprocessing.Process(target=countUp())

    # start this worker
    workdown.start()
    workup.start()

    #make worker to join
    workup.join()
    workdown.join()

"""
Pool : it is basically a class  which manage multiple process.

"""
from multiprocessing import Pool
def cube(x):
    return x**3

if __name__=="__main__":
    pool = Pool(5)
    result = pool.map(cube,[0,1,2,3,4,5])
    print(result)
