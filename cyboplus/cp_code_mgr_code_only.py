import win32com.client
import datetime
from cp_code_mgr.codes import CpCodeMgrCode 

def cp_code_mgr():
    instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
    codes = CpCodeMgrCode()

    print("=========================\n")
    today = datetime.datetime.now()
    with open(today.strftime('%Y%m%d')+'_cpCodeMgr_code_only.csv', 'w', encoding='utf-8') as f:
        for idx in range(len(codes.stock_market_code_dic)):
            codeList = instCpCodeMgr.GetStockListByMarket(idx)
            
            str_list = []
            for i, code in enumerate(codeList):
                name = instCpCodeMgr.CodeToName(code)
                #marketKindCode = instCpCodeMgr.GetStockMarketKind(code)
                
                #print(i, code, secondCode, name)
                str_list.append(str(i))
                str_list.append(code)
                str_list.append(name)
                str_list.append(str(idx))
                str_list.append(codes.get_stock_market_kind(str(idx)))
                
                f.write('\t'.join(str_list))
                f.write('\n')
                del str_list[:]

if __name__ == '__main__':
    print("====== CpCodeMgr =======")
    cp_code_mgr()

