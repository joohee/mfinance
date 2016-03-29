import win32com.client
import datetime

# CpStockCode : code, name, fullcode
class CPStockCode:
    def __init__(self):
        self.index_no = 3
        pass

    def exec(self, apiName):
        inst = win32com.client.Dispatch(apiName)

        print("=========================\n")
        today = datetime.datetime.now()
        with open(today.strftime('%Y%m%d')+'_stock_code.csv', 'w', encoding='utf-8') as f:
            count = inst.GetCount()          # count
            for i in range(count):
                line = str(i)
                for idx in range(0, self.index_no):
                    line += "\t{0}".format(inst.GetData(idx, i))
                f.write(line+"\n")
                
        print("=========================\n")

if __name__ == '__main__':
    apiName = 'CpUtil.CpStockCode'
    print("====== {}  =======".format(apiName))

    template = CPStockCode()
    template.exec(apiName)

