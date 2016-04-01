import __init__
import os

from packages.cp_template import CpClass
from packages.cp_stock_chart.codes import StockChart as StockChartCodes 
from weakref import proxy
from pythoncom import CoInitialize, PumpWaitingMessages
from win32com.client import gencache, DispatchWithEvents
from win32event import MsgWaitForMultipleObjects, QS_ALLEVENTS
import time
import datetime

class CpEvent(object):
    def OnReceived(self):
        self.parent.on_signal()
        
class StockChart:
    def __init__(self, code):
        self.code = code
        self.event = DispatchWithEvents("CpSysDib.StockChart", CpEvent)
        self.com = self.event._obj_
        self.event.parent = proxy(self)


        self.count = 400
        self.today = datetime.datetime.now()
        self.yyyymmdd = self.today.strftime('%Y%m%d')
        #self.yyyymmdd = '20160325'
        self.com.SetInputValue(0, self.code)
        self.com.SetInputValue(1, '2')        # by count
        self.com.SetInputValue(2, '0')        # lastest
        self.com.SetInputValue(3, self.yyyymmdd)
        self.com.SetInputValue(6, ord('m'))        # minute
        
        self.com.SetInputValue(4, self.count)        # request count
        self.com.SetInputValue(5, [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 37])
        self.com.SetInputValue(9, '1')

        self.com.Request()
        CoInitialize()

        print("today: {}".format(self.today))
        
    def on_signal(self):
        print ('rp [%s]'%self.__class__.__name__)        
        codes = StockChartCodes()

        str_list = []
        dirname = os.path.dirname(__file__)
        fullpath = os.path.join(dirname, self.yyyymmdd+'_StockChart_min.csv')
        num = self.com.GetHeaderValue(3)
        print('received count: {}'.format(num))
        
        with open(fullpath, 'w', encoding='utf-8') as f:
            print("[START] write header")
            for i in range(codes.get_stock_field_count()):
                header = codes.stock_field_dic.get(str(i))
                if header is None:
                    print("header {} is None".format(i))
                else:
                    str_list.append(header)

            #print("str_list: {}".format(str_list))
            f.write('\t'.join(str_list))
            f.write('\n')
            del str_list[:]
            print("[DONE] write header")

            print("[START] write data")
            for i in range(num):
                date = self.com.GetDataValue(0, i)
                if self.yyyymmdd != str(date):
                    print("{} is different with today {}.. continue".format(str(date), self.yyyymmdd))
                    continue
                
                for idx in range(codes.get_stock_field_count()):
                    try:
                        #print("\t{0}: {1}".format(codes.stock_field_dic.get(str(idx)), reqObj.GetDataValue(idx, i)))
                        #print("\t==============")
                        str_list.append(str(self.com.GetDataValue(idx, i)))
                    except:
                        print("error occured")
                        pass
                #print("str_list: {}".format(str_list))
                f.write('\t'.join(str_list))
                f.write('\n')
                del str_list[:]
            print("[END] write data")

if __name__ == '__main__':
    stockchart = StockChart('A067160')
  

