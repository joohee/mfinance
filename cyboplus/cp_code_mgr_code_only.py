import __init__
import win32com.client
import datetime
from packages.cp_code_mgr.codes import CpCodeMgrCode 

def cp_code_mgr():
    """ cp_code_mgr.py 의 요약버전입니다. 

    Args:
        없습니다.

    Returns:
        조회한 날짜+"_cpCodeMgr_code_only.csv" 로 저장합니다. 
        row는 아래와 같이 구성되어 있습니다.

            idx - API 호출 결과값 line 수 - 1 (0부터 시작합니다.)
            code - 종목코드(A+6자리)
            name - 종목명
            marketCode - 주식시장코드명 
                "0": "구분없음",
                "1": "거래소",
                "2": "코스닥",
                "3": "프리보드",
                "4": "KRX"
            marketName - 시장명
    """
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

