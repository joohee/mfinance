import win32com
import win32com.client
import pythoncom
import threading
import time
from packages.cp_template import CpClass
from packages.cp_stock_chart.codes import StockChart as StockChartCodes 

class StockChart:
    def __init__(self):
        self.com_str = "CpSysDib.StockChart"

    def request(self, com_obj):
        com_obj.SetInputValue(0, 'A067160')
        com_obj.SetInputValue(1, '1')        # count
        com_obj.SetInputValue(2, '0')        # lastest 
        com_obj.SetInputValue(3, '20160310')
        com_obj.SetInputValue(4, 10)        # request count
        com_obj.SetInputValue(5, [0, 1, 2, 3, 4, 5, 6, 8, 9, 37])
        com_obj.SetInputValue(6, ord('m'))        # minute
        com_obj.SetInputValue(9, '1')
        com_obj.Request()
        print ('rq [%s]'%self.__class__.__name__)

    def response(self, com_obj):
        print ('rp [%s]'%self.__class__.__name__)
        
        codes = StockChartCodes()
        for i in range(codes.get_header_count()):
            print("{0} = {1}".format(codes.header_dic.get(str(i)), com_obj.GetHeaderValue(i)))

        num = com_obj.GetHeaderValue(3)
        for i in range(num):
            for idx in range(codes.get_stock_field_count()):
                try:
                    print("\t{0}: {1}".format(codes.stock_field_dic.get(str(idx)), com_obj.GetDataValue(idx, i)))
                    print("\t==============")
                except:
                    print("error occured")
                    pass

if __name__ == '__main__':
    stockchart = CpClass.Bind(StockChart())
    stockchart.Request()

    while True:
        pythoncom.PumpWaitingMessages()
        time.sleep(0.01)

