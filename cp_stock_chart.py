import win32com
import win32com.client
import pythoncom
import threading
import time
import datetime
from packages.cp_template import CpClass
from packages.cp_stock_chart.codes import StockChart as StockChartCodes 

class StockChart:
    def __init__(self):
        self.com_str = "CpSysDib.StockChart"

    def request(self, reqObj):
        today = datetime.datetime.now()
        fromdate = today - datetime.timedelta(days=7)

        yyyymmdd = today.strftime('%Y%m%d')
        fyyyymmdd = fromdate.strftime('%Y%m%d')
        count = 20
        
        reqObj.SetInputValue(0, 'A067160')
        #reqObj.SetInputValue(1, '2')        # date
        #reqObj.SetInputValue(2, yyyymmdd)     # end date
        #reqObj.SetInputValue(3, fyyyymmdd)     # start date
        #reqObj.SetInputValue(6, ord('D'))        # day
        reqObj.SetInputValue(1, '1')        # count
        reqObj.SetInputValue(2, '0')        # lastest
        reqObj.SetInputValue(3, yyyymmdd)

        reqObj.SetInputValue(4, 10)        # request count
        reqObj.SetInputValue(5, [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 37])
        reqObj.SetInputValue(6, ord('m'))        # minute
        reqObj.SetInputValue(9, '1')
        reqObj.Request()
        print ('rq [%s]'%self.__class__.__name__)

    def response(self, reqObj):
        print ('rp [%s]'%self.__class__.__name__)
        
        codes = StockChartCodes()

        str_list = []
        dirname = os.path.dirname(__file__)
        fullpath = os.path.join(dirname, yyyymmdd+'_StockChart_all.csv')
        num = reqObj.GetHeaderValue(3)
        with open(fullpath, 'w', encoding='utf-8') as f:
            #for i in range(codes.get_header_count()):
                #print("{0} = {1}".format(codes.header_dic.get(str(i)), reqObj.GetHeaderValue(i)))
            for i in range(codes.get_stock_field_count()):
                str_list.append(codes.stock_field_dic.get(str(i)))
                
            del str_list[:]
            for i in range(num):
                for idx in range(codes.get_stock_field_count()):
                    try:
                        #print("\t{0}: {1}".format(codes.stock_field_dic.get(str(idx)), reqObj.GetDataValue(idx, i)))
                        #print("\t==============")
                        str_list.append(str(reqObj.GetDataValue(idx, i)))
                        f.write('\t'.join(str_list))
                        f.write('\n')
                    except:
                        print("error occured")
                        pass
                    del str_list[:]

if __name__ == '__main__':
    stockchart = CpClass.Bind(StockChart())
    stockchart.Request()

    while True:
        pythoncom.PumpWaitingMessages()
        time.sleep(0.01)

