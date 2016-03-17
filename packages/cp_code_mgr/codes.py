class CpCodeMgrCode:
    stock_code_dic = {
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

    stock_market_code_dic = {
        "0": "구분없음",
        "1": "거래소",
        "2": "코스닥",
        "3": "프리보드",
        "4": "KRX"
    }

    stock_kospi_200_kind_dic = {
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

    stock_control_kind_dic = {
        "0": "정상",
        "1": "주의",
        "2": "경고",
        "3": "위험예고",
        "4": "위험"
    }

    stock_status_kind_dic = {
        "0": "정상",
        "1": "거래정지",
        "2": "거래중단"
    }

    stock_supervision_kind_dic = {
        "0": "일반종목",
        "1": "관리"
    }

    header_dic = {
        "0": "idx",
        "1": "코드",
        "2": "이름",
        "3": "부 구분코드",
        "4": "소속부",
        "5": "KOSPI200 종목명(코드)",
        "6": "증권전산업종명(코드)",
        "7": "상장일",
        "8": "감리구분",
        "9": "주식상태",
        "10": "관리구분"
    }

    def __init__(self):
        print("CpCodeMgrCode")

    @staticmethod
    def get_or_none(code, value):
        if value is None:
            value = 'NoneType(' + str(code) + ')'
        return value

    @classmethod
    def get_stock_code(cls, code):
        value = cls.stock_code_dic.get(code)
        return CpCodeMgrCode.get_or_none(code, value)

    @classmethod
    def get_stock_market_kind(cls, code):
        value = cls.stock_market_code_dic.get(code)
        return cls.get_or_none(code, value)

    @classmethod
    def get_stock_kospi_200_kind(cls, code):
        value = cls.stock_kospi_200_kind_dic.get(code)
        return cls.get_or_none(code, value)

    @classmethod
    def get_stock_control_kind(cls, code):
        value = cls.stock_control_kind_dic.get(code)
        return cls.get_or_none(code, value)

    @classmethod
    def get_stock_status_kind(cls, code):
        value = cls.stock_status_kind_dic.get(code)
        return cls.get_or_none(code, value)

    @classmethod
    def get_stock_supervision_kind(cls, code):
        value = cls.stock_supervision_kind_dic.get(code)
        return cls.get_or_none(code, value)

    @classmethod
    def get_header(cls, idx):
        return cls.header_dic.get(idx)

if __name__ == "__main__":
    header_keys = CpCodeMgrCode.header_dic.keys()
    stock_code_keys = CpCodeMgrCode.stock_code_dic.keys()
    stock_kospi_200_kind_keys = CpCodeMgrCode.stock_kospi_200_kind_dic.keys()
    stock_control_kind_keys = CpCodeMgrCode.stock_control_kind_dic.keys()
    stock_status_kind_dic_keys = CpCodeMgrCode.stock_status_kind_dic.keys()
    stock_supervision_kind_dic_keys = CpCodeMgrCode.stock_supervision_kind_dic.keys()
    
    for key in sorted(header_keys):
        print("header_dic key: {0}, value: {1}".format(key, CpCodeMgrCode.header_dic.get(key)))
    print("=========================")

    for key in sorted(stock_code_keys):
        print("stock_code_dic key: {0}, value: {1}".format(key, CpCodeMgrCode.stock_code_dic.get(key)))
    print("=========================")

    for key in sorted(stock_kospi_200_kind_keys):
        print("stock_kospi_200_kind_dic key: {0}, value: {1}".format(key, CpCodeMgrCode.stock_kospi_200_kind_dic.get(key)))
    print("=========================")

    for key in sorted(stock_control_kind_keys):
        print("stock_control_kind_dic key: {0}, value: {1}".format(key, CpCodeMgrCode.stock_control_kind_dic.get(key)))
    print("=========================")

    for key in sorted(stock_status_kind_dic_keys):
        print("stock_status_kind_dic key: {0}, value: {1}".format(key, CpCodeMgrCode.stock_status_kind_dic.get(key)))
    print("=========================")

    for key in sorted(stock_supervision_kind_dic_keys):
        print("stock_supervision_kind_dic key: {0}, value: {1}".format(key, CpCodeMgrCode.stock_supervision_kind_dic.get(key)))
    print("=========================")



    

