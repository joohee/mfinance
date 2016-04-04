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
    """StockChart library를 이용하여 특정 종목의 분봉 값을 얻습니다.

        Args:
            code - 주식코드. (ex. A000020)

            StockChart.__init__() function에서 아래 값을 설정한다. 
                0 - 종목코드(string): 주식(A003540), 업종(U001), ELW(J517016)의 종목코드
                1 - 요청구분(char):
                    '1' 기간으로 요청
                    '2' 개수로 요청
                2 - 요청종료일(ulong): YYYYMMDD형식으로 데이터의 마지막(가장 최근) 날짜 Default(0) - 최근 거래날짜
                3 - 요청시작일(ulong): YYYYMMDD형식으로 데이터의 시작(가장 오래된) 날짜
                4 - 요청개수(ulong): 요청할 데이터의 개수
                5 - 필드(long or long array): 필드 또는 필드 배열
                    위 값은 packsges.cp_stock_code.codes 의 header_dic 값이 된다. 
                6 - 차트구분(char)
                    'D' 일
                    'W' 주
                    'M' 월
                    'm' 분
                    'T' 틱
            7 - 주기(ushort): Default-1
            8 - 갭보정여부(char)
                '0' 갭무보정 [Default]
                '1' 갭보정
            9 - 수정주가(char)
                '0' 무수정주가 [Default]
                '1' 수정주가
            10 - 거래량구분(char)
                '1' 시간외거래량 모두 포함[Default]
                '2' 장종료시간외거래량만 포함
                '3' 시간외거래량 모두 제외
                '4' 장전시간외거래량만 포함

            * 대비부호는 아래 값을 의미한다. 
            8 - 대비부호(char)
                '1' 상한
                '2' 상승
                '3' 보합
                '4' 하한
                '5' 하락
                '6' 기세상한
                '7' 기세상승
                '8' 기세하한
                '9' 기세하락

        Returns:
            요청일 '%Y%m%d'+'_StockChart_min.csv' 파일로 저장한다.
    """

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
  

