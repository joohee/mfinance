import threading
from queue import Queue
import time
import datetime
from packages.cp_stock_chart import StockChart

class CpThread:

    def __init__(self):
        self.print_lock = threading.Lock()
        self.q = Queue()

    def convert_date(date):
        return date.strftime('%Y%m%d')

    # 실제 작업하는 놈
    def stockChart(self, worker, from_date, to_date):
        time.sleep(0.5)

        with self.print_lock:
            print("name: {}, worker: {}, from_date: {}, to_date: {}".format(threading.current_thread().name, worker, from_date, to_date))
            stockChart = StockChart('A067160', convert_date(from_date), convert_date(to_date))

    def threader(self, from_date, to_date):
        while True:
            worker = self.q.get()
            self.stockChart(worker, from_date, to_date)
            self.q.task_done()

    def work(self):
        from_date = datetime.datetime.now() 

        for x in range(10):
            to_date = from_date - datetime.timedelta(days=x)
            t = threading.Thread(target = self.threader, args=[from_date, to_date])
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

