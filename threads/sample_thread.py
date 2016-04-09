import threading
from queue import Queue
import time

print_lock = threading.Lock()

class SampleThread:
    def __init__(self):
        self.q = Queue()
        pass

    def exampleJob(self, worker):
        time.sleep(0.5)

        with print_lock:
            print("name: {}, worker: {}".format(threading.current_thread().name, worker))

    def threader(self):
        while True:
            worker = self.q.get()
            self.exampleJob(worker)
            self.q.task_done()

    def execute(self):
        for x in range(10):
            t = threading.Thread(target = self.threader)
            t.daemon = True
            t.start()

        self.start = time.time()

        for worker in range(20):
            self.q.put(worker)

        self.q.join()

if __name__ == '__main__':
    sf = SampleThread()
    sf.execute()
    print('Entire job took:', time.time()-sf.start)

