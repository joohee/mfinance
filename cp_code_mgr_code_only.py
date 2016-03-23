import win32com.client
import datetime
from packages.cp_code_mgr.codes import CpCodeMgrCode 

def cp_code_mgr():
    instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
    codes = CpCodeMgrCode()

    print("=========================\n")
    today = datetime.datetime.now()
    with open(today.strftime('%Y%m%d')+'_cpCodeMgr_code_only.csv', 'w', encoding='utf-8') as f:
        header_list = []
        for i in range(len(codes.header_dic)):
            header_list.append(codes.get_header(str(i)))
        f.write('\t'.join(header_list))
        f.write('\n')

        for idx in range(len(codes.stock_market_code_dic)):
            codeList = instCpCodeMgr.GetStockListByMarket(idx)
            
            str_list = []
            for i, code in enumerate(codeList):
                name = instCpCodeMgr.CodeToName(code)

                #print(i, code, secondCode, name)
                str_list.append(str(i))
                str_list.append(code)
                f.write('\t'.join(str_list))
                f.write('\n')
                del str_list[:]

if __name__ == '__main__':
    print("====== CpCodeMgr =======")
    cp_code_mgr()

