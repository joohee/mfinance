import __init__
import threading
from queue import Queue
import time
import datetime
from pythoncom import CoInitialize
from cyboplus.cp_stock_chart_with_option import StockChart

class CpThread:
    """CpStockChart API를 이용해서 thread로 데이터를 얻어오도록 한다. 
        
        Args:
            from_date : 조회 시작일
            to_date : 조회 종료일 

        Returns:
            cp_stock_chart_with_option.py 파일의 StockChart 를 호출하였으므로 
            종목별로 csv 파일로 저장한다. 
        
    """

    def __init__(self):
        self.print_lock = threading.Lock()
        self.q = Queue()

    def convert_date(self, date):
        return date.strftime('%Y%m%d')

    # 실제 작업하는 놈
    def stockChart(self, worker, from_date, to_date):
        time.sleep(0.5)

        with self.print_lock:
            print("name: {}, worker: {}, from_date: {}, to_date: {}".format(threading.current_thread().name, worker, from_date, to_date))
            CoInitialize()
            stockChart = StockChart('A067160', self.convert_date(from_date), self.convert_date(to_date))

    def threader(self, from_date, to_date):
        while True:
            worker = self.q.get()
            self.stockChart(worker, from_date, to_date)
            self.q.task_done()

    def work(self):
        now = datetime.datetime.now() 

        for x in range(10):
            from_date = now - datetime.timedelta(days=x)
            to_date = now - datetime.timedelta(days=(x+1))
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

