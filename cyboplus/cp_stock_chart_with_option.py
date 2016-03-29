from weakref import proxy
from pythoncom import CoInitialize, PumpWaitingMessages
from win32com.client import gencache, DispatchWithEvents
from win32event import MsgWaitForMultipleObjects, QS_ALLEVENTS
import time
import datetime
import os
from packages.cp_template import CpClass
from packages.cp_stock_chart.codes import StockChart as StockChartCodes 

class CpEvent(object):
    def OnReceived(self):
        self.parent.on_signal()
        
class StockChart:
    def __init__(self, code, from_yyyymmdd, to_yyyymmdd):
        self.code = code
        self.event = DispatchWithEvents("CpSysDib.StockChart", CpEvent)
        self.com = self.event._obj_
        self.event.parent = proxy(self)

        self.count = 400
        self.today = datetime.datetime.now()
        #self.yyyymmdd = self.today.strftime('%Y%m%d')
        #self.yyyymmdd = '20160325'
        self.from_yyyymmdd = from_yyyymmdd
        self.to_yyyymmdd = to_yyyymmdd

        self.com.SetInputValue(0, self.code)
        self.com.SetInputValue(1, '1')        # by count
        self.com.SetInputValue(2, self.from_yyyymmdd)        # lastest
        self.com.SetInputValue(3, self.to_yyyymmdd)
        self.com.SetInputValue(6, ord('m'))        # minute
        
        self.com.SetInputValue(4, self.count)        # request count
        self.com.SetInputValue(5, [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 37])
        self.com.SetInputValue(9, '1')

        self.com.Request()
        CoInitialize()

        print("today: {}, from: {}, to: {}".format(self.today, from_yyyymmdd, to_yyyymmdd))
        
    def on_signal(self):
        print ('rp [%s]'%self.__class__.__name__)        
        codes = StockChartCodes()

        print("yyyymmdd: {}".format(self.from_yyyymmdd))
        str_list = []
        dirname = os.path.dirname(__file__)
        fullpath = os.path.join(dirname, str(self.from_yyyymmdd)+'_StockChart_2016_min.csv')
        num = self.com.GetHeaderValue(3)
        print('received count: {}'.format(num))

        if num == 0:
            print("there's no data of date {}".format(from_yyyymmdd))

        with open(fullpath, 'w', encoding='utf-8') as f:
            print("[START] write header of {}".format(self.from_yyyymmdd))
            for i in range(codes.get_stock_field_count()):
                header = codes.stock_field_dic.get(str(i))
                if header is None:
                    print("header {} is None".format(i))
                    str_list.append("header_"+str(i))
                else:
                    str_list.append(header)

            #print("str_list: {}".format(str_list))
            f.write('\t'.join(str_list))
            f.write('\n')
            del str_list[:]
            print("[DONE] write header of {}".format(self.from_yyyymmdd))

            print("[START] write data of {}".format(self.from_yyyymmdd))
            for i in range(num):
                date = self.com.GetDataValue(0, i)
                if self.from_yyyymmdd != date:
                    print("{} is different with today {}.. continue".format(str(date), self.from_yyyymmdd))
                    #continue
               
                for idx in range(codes.get_stock_field_count()):
                    try:
                        #print("\t{0}: {1}".format(codes.stock_field_dic.get(str(idx)), reqObj.GetDataValue(idx, i)))
                        #print("\t==============")
                        str_list.append(str(self.com.GetDataValue(idx, i)))
                    except e:
                        print(e)
                        pass

                #print("str_list: {}".format(str_list))
                f.write('\t'.join(str_list))
                f.write('\n')
                del str_list[:]
            print("[END] write data of {}".format(self.from_yyyymmdd))
       
if __name__ == '__main__':
    from_yyyymmdd = datetime.datetime.now().strftime('%Y%m%d')
    #to_yyyymmdd = '20160101'
    to_yyyymmdd = str(int(from_yyyymmdd) - 3)
    
    for day in range(int(from_yyyymmdd), int(to_yyyymmdd), -1):
        print('start..{}'.format(day))
        stockchart = StockChart('A067160', day, day-1)
        #print('sleep...')
        #time.sleep(3)
