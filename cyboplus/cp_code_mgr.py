import __init__
import win32com.client
import datetime
from packages.cp_code_mgr.codes import CpCodeMgrCode 

def passmein(func):
    def wrapper(*args, **kwargs):
        return func(func, *args, **kwargs)
    return wrapper

@passmein
def cp_code_mgr(me):
    """ CpUtil.CpCodeMgr module을 호출한 function입니다. 
        
        Args:
            없습니다. 

        Returns:
            File: 결과를 전부 조회하여 날짜+"_cpCodeMgr_detail_all.csv"로 저장합니다. 
            
            해당 파일의 row는 packages.cp_code.mgr.codes 아래 CpCodeMgrCode 에 dictionary를 설정하였습니다. 
            각각의 row는 아래와 같이 구성되어 있습니다. 
            
                idx - API 호출 결과값으로 리턴된 row 숫자입니다. 0부터 시작합니다. 
                코드- 6자리 코드
                이름- 종목명 
                부 구분코드 - 아래 값을 가진다.
                   "0": "구분없음",
                   "1": "주권",
		           "2": "투자회사",
		           "3": "부동산투자회사",
		           "4": "선박투자회사",
		           "5": "사회간접자본투융자회사",
		           "6": "주식예탁증서",
		           "7": "신주인수권증권",
		           "8": "신주인수권증서",
		           "9": "주식워런트증권",
		           "10": "상장지수펀드(ETF)",
		           "11": "수익증권",
		           "12": "해외ETF",
		           "13": "외국주권",
		           "14": "선물",
		           "15": "옵션",
		           "17": "ETN"
                 소속부 - 아래 값을 가진다. 
                    "0": "구분없음",
                    "1": "거래소",
                    "2": "코스닥",
                    "3": "프리보드",
                    "4": "KRX"
                 KOSPI200 종목명(코드) - KOSPI200 종목여부를 반환한다. 
                    "0": "미채용",
                    "1": "건설기계",
                    "2": "조선운송",
                    "3": "철강소재",
                    "4": "에너지화학",
                    "5": "정보통신",
                    "6": "금융",
                    "7": "필수소비재",
                    "8": "자유소비재"
                 증권전산업종명(코드) - 종목에 해당하는 증권전산코드 및 증권전산업종명을 조회한다. 
                 상장일 
                 감리구분 - 아래 값을 가진다. 
                    "0": "정상",
                    "1": "주의",
                    "2": "경고",
                    "3": "위험예고",
                    "4": "위험"
                 주식상태 - 아래 값을 가진다. 
                    "0": "정상",
                    "1": "거래정지",
                    "2": "거래중단"
                 관리구분 - 아래 값을 가진다. 
                    "0": "일반종목",
                    "1": "관리"
    """

    print(me.__doc__)

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

