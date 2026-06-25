import threading, time
from threading import Thread

def dummyFunction(nThread):
    print("dummy function in thread %i will sleep for 1 sec" % nThread)
    time.sleep(1)
    print("dummy function in thread %i awake" % nThread)

for i in range(10):
    thread = threading.Thread(target=dummyFunction, args=(i,))
    thread.start()
    print("Total threads: %i" % threading.active_count())