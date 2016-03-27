import win32com
import win32com.client
import pythoncom
import threading
import time
import datetime
import os
from packages.cp_template import CpClass
from packages.cp_stock_chart.codes import StockChart as StockChartCodes 

class StockChart:
    def __init__(self, code):
        self.code = code
        self.com_str = "CpSysDib.StockChart"
        self.today = datetime.datetime.now()
        self.fromdate = self.today - datetime.timedelta(days=7)

        self.yyyymmdd = self.today.strftime('%Y%m%d')
        self.fyyyymmdd = self.fromdate.strftime('%Y%m%d')
        self.count = 1440 

        print("today: {}".format(self.today))
        
    def request(self, reqObj):
        reqObj.SetInputValue(0, self.code)
        reqObj.SetInputValue(1, '2')        # by date
        reqObj.SetInputValue(2, '0')        # lastest
        reqObj.SetInputValue(3, self.yyyymmdd)
        reqObj.SetInputValue(6, ord('m'))        # minute
        
        reqObj.SetInputValue(4, self.count)        # request count
        reqObj.SetInputValue(5, [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 37])
        reqObj.SetInputValue(9, '1')
        ret = reqObj.Request()
        print ('rq [%s]'%self.__class__.__name__)
        print('count: {}'.format(self.count))

        codes = StockChartCodes()

        if ret == 0:
            str_list = []
            dirname = os.path.dirname(__file__)
            fullpath = os.path.join(dirname, self.yyyymmdd+'_StockChart_req_min.csv')
            num = reqObj.GetHeaderValue(3)
            print('received count: {}'.format(num))

            with open(fullpath, 'w', encoding='utf-8') as f:
                #for i in range(codes.get_header_count()):
	            #print("{0} = {1}".format(codes.header_dic.get(str(i)), reqObj.GetHeaderValue(i)))
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

                for i in range(num):
                    for idx in range(codes.get_stock_field_count()):
                        try:
	                    #print("\t{0}: {1}".format(codes.stock_field_dic.get(str(idx)), reqObj.GetDataValue(idx, i)))
	                    #print("\t==============")
                            str_list.append(str(reqObj.GetDataValue(idx, i)))
                        except:
                            print("error occured")
                            pass
                    #print("str_list: {}".format(str_list))
                    f.write('\t'.join(str_list))
                    f.write('\n')
                    del str_list[:]
        else:
                print("error...ret: {}".format(str(ret)))

if __name__ == '__main__':
    stockchart = CpClass.Bind(StockChart('A067160'))
    stockchart.Request()

