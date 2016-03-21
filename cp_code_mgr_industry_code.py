import win32com.client
Import datetime

def get_or_none(code, value):
    if value is None:

        value = 'NoneType(' + str(code) + ')'
    return value

def get_code_dic(code):
    code_dic = {
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
    }

    value = code_dic.get(code)
    return get_or_none(code, value)

def get_stock_market_kind(code):
    code_dic = {
        "0": "구분없음",
        "1": "거래소",
        "2": "코스닥",
        "3": "프리보드",
        "4": "KRX"
    }

    value = code_dic.get(code)
    return get_or_none(code, value)

def get_stock_kospi_200_kind(code):
    code_dic = {
        "0": "미채용",
        "1": "건설기계",
        "2": "조선운송",
        "3": "철강소재",
        "4": "에너지화학",
        "5": "정보통신",
        "6": "금융",
        "7": "필수소비재",
        "8": "자유소비재"
    }
    value = code_dic.get(code)
    return get_or_none(code, value)

def get_stock_control_kind(code):
    code_dic = {
        "0": "정상",
        "1": "주의",
        "2": "경고",
        "3": "위험예고",
        "4": "위험"
    }

    value = code_dic.get(code)
    return get_or_none(code, value)

def get_header(idx):
    header_dic = {
        "0": "idx",
        "1": "코드",
        "2": "이름",
        "3": "부 구분코드",
        "4": "소속부",
        "5": "KOSPI200 종목여부",
        "6": "감리구분",
        "7": "상장일",
        "8": "증권전산업종코드"
    }
    return header_dic.get(idx)

def cp_code_mgr():
    instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
    codeList = instCpCodeMgr.GetStockListByMarket(1)
    today = datetime.datetime.now()

    codes = instCpCodeMgr.GetIndustryList()
    for i in range(len(codes)):
        groupCodeList = instCpCodeMgr.GetGroupCodeList(codes[i])
        industryName = instCpCodeMgr.GetIndustryName(codes[i])
        for j in range(len(groupCodeList)):
            groupCode = groupCodeList[j]
            groupName = instCpCodeMgr.CodeToName(groupCode)
            print("code: {}({}), groupCode: {}({})".format(industryName, codes[i], groupName, groupCodeList[j]))

    codes1 = instCpCodeMgr.GetKosdaqIndustry1List()
    for i in range(len(codes1)):
        print("index: {}, code: {}".format(i, codes1[i]))
    print("============")
    codes2 = instCpCodeMgr.GetKosdaqIndustry2List()
    for i in range(len(codes2)):
        print("index: {}, code: {}".format(i, codes2[i]))
    print("============")

if __name__ == '__main__':
    print("====== CpCodeMgr =======")
    cp_code_mgr()
