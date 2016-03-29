import threading
from queue import Queue
import time
from cp_stock_chart import cp_stock_chart

class CpThread:

    def __init__(self):
        self.print_lock = threading.Lock()
        self.q = Queue()

    def exampleJob(self, worker):
        time.sleep(0.5)

        with self.print_lock:
            print("name: {}, worker: {}".format(threading.current_thread().name, worker))

    def threader(self):
        while True:
            worker = self.q.get()
            self.exampleJob(worker)
            self.q.task_done()

    def work(self):

        for x in range(10):
            t = threading.Thread(target = self.threader)
            t.daemon = True
            t.start()

        start = time.time()

        for worker in range(20):
            self.q.put(worker)

        self.q.join()
        print('Entire job took:', time.time()-start)

if __name__ == '__main__':
    cpThread = CpThread()
    cpThread.work()

