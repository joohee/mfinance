import win32com.client
import datetime
from packages.cp_code_mgr.codes import CpCodeMgrCode 

def cp_code_mgr():
    instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
    codes = CpCodeMgrCode()

    print("=========================\n")
    today = datetime.datetime.now()
    with open(today.strftime('%Y%m%d')+'_cpCodeMgr_detail_all.csv', 'w', encoding='utf-8') as f:
        header_list = []
        for i in range(len(codes.header_dic)):
            header_list.append(codes.get_header(str(i)))
        f.write('\t'.join(header_list))
        f.write('\n')

        for idx in range(len(codes.stock_market_code_dic)):
            codeList = instCpCodeMgr.GetStockListByMarket(idx)
            
            str_list = []
            for i, code in enumerate(codeList):
                secondCode = instCpCodeMgr.GetStockSectionKind(code)
                marketKindCode = instCpCodeMgr.GetStockMarketKind(code)
                kospi200Code = instCpCodeMgr.GetStockKospi200Kind(code)
                controlCode = instCpCodeMgr.GetStockControlKind(code)
                listedDate = instCpCodeMgr.GetStockListedDate(code)
                industryCode = instCpCodeMgr.GetStockIndustryCode(code)
                industryName = instCpCodeMgr.GetIndustryName(industryCode)
                statusKind = instCpCodeMgr.GetStockStatusKind(code)
                supervisionKind = instCpCodeMgr.GetStockSupervisionKind(code)
                name = instCpCodeMgr.CodeToName(code)

                #print(i, code, secondCode, name)
                str_list.append(str(i))
                str_list.append(code)
                str_list.append(name)
                str_list.append(codes.get_stock_code(str(secondCode)))
                str_list.append(codes.get_stock_market_kind(str(marketKindCode)))
                str_list.append(codes.get_stock_kospi_200_kind(str(kospi200Code))+"("+str(kospi200Code)+")")
                str_list.append(industryName+"("+str(industryCode)+")")
                str_list.append(str(listedDate))
                str_list.append(codes.get_stock_control_kind(str(controlCode)))
                str_list.append(codes.get_stock_status_kind(str(statusKind)))
                str_list.append(codes.get_stock_supervision_kind(str(supervisionKind)))
                f.write('\t'.join(str_list))
                f.write('\n')
                del str_list[:]

if __name__ == '__main__':
    print("====== CpCodeMgr =======")
    cp_code_mgr()

