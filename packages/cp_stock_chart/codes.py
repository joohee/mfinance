class StockChart:
    header_dic = {
        "0": "종목코드", 
        "1": "필드 개수",
        "2": "필드명의 배열",
        "3": "수신 개수",
        "4": "시간(hhmm)", 
        "5": "최근거래일",
        "6": "전일종가",
        "7": "현재가",
        "8": "대비부호",
        "9": "대비",
        "10": "거래량",
        "11": "매도호가",
        "12": "매수호가",
        "13": "시가",
        "14": "고가",
        "15": "저가",
        "16": "거래대금",
        "17": "종목상태",
        "18": "상장주식 수",
        "19": "자본금(백만)",
        "20": "전일거래량",
        "21": "최근갱신시간(long)",
        "22": "상한가",
        "23": "하한가"
    }

    # 대비부호 - header 8번 해석 용
    compare_mark_dic = {
        "1": "상한",
        "2": "상승",
        "3": "보합",
        "4": "하한",
        "5": "하락",
        "6": "기세상한",
        "7": "기세상승",
        "8": "기세하한",
        "9": "기세하락"
    }

    # 종목 상태 - header 17번 해석 용  
    stock_status_dic = {
        "0": "정상",
        "1": "투자위험",
        "2": "관리",
        "3": "거래정지",
        "4": "불성실공시",
        "5": "불성실공시&관리",
        "6": "불성실공시&거래정지",
        "7": "불성실공시&투자위험",
        "8": "투자위험&거래정지",
        "9": "관리&거래정지",
        "A": "불성실공시&관리&거래정지",
        "B": "불성실공시&투자위험&거래정지",
        "C": "투자위험예고",
        "D": "투자주의",
        "E": "투자경고",
        "F": "불성실공시&투자위험예고",
        "G": "불성실공시&투자주의",
        "H": "불성실공시&투자경고",
        "I": "투자위험예고&거래정지",
        "J": "투자주의&거래정지",
        "K": "투자경고&거래정지",
        "L": "불성실공시&투자위험예고&거래정지",
        "M": "불성실공시&투자주의&거래정지",
        "N": "불성실공시&투자경고&거래정지",
        "Z": "ETF종목"
    }

    stock_field_dic = {
        "0": "날짜",
        "1": "시간 - hhmm",
        "2": "시가",
        "3": "고가",
        "4": "저가",
        "5": "종가",
        "6": "전일대비- 주) 대비부호(37)과 반드시 같이 요청해야 함",
        "8": "거래량 - 주) 정밀도 만원 단위",
		"9": "거래대금",
		"10": "누적체결매도수량 - 호가비교방식 누적체결매도수량",
		"11": "누적체결매수수량 - 호가비교방식 누적체결매수수량",
		# (주) 10, 11 필드는 분,틱 요청일 때만 제공",
		"12": "상장주식수",
		"13": "시가총액",
		"14": "외국인주문한도수량",
		"15": "외국인주문가능수량",
		"16": "외국인현보유수량",
		"17": "외국인현보유비율",
		"18": "수정주가일자 - YYYYMMDD",
		"19": "수정주가비율",
		"20": "기관순매수",
		"21": "기관누적순매수",
		"22": "등락주선",
		"23": "등락비율",
		"24": "예탁금",
		"25": "주식회전율",
		"26": "거래성립률",
		"37": "대비부호"      # 수신값은 GetHeaderValue 8 대비부호와 동일"
    }

    @classmethod 
    def get_header_count(cls):
        return len(cls.header_dic)

    @classmethod
    def get_compare_mark_count(cls):
        return len(cls.compare_mark_dic)

    @classmethod
    def get_stock_status_count(cls):
        return len(cls.stock_status_dic)

    @classmethod
    def get_stock_field_count(cls):
        return len(cls.stock_field_dic)

    def __init__(self):
        pass

if __name__ == "__main__":
    stockChart = StockChart()

    header_keys = stockChart.header_dic.keys()
    compare_mark_keys = stockChart.compare_mark_dic.keys()
    stock_status_keys = stockChart.stock_status_dic.keys()
    stock_field_keys = stockChart.stock_field_dic.keys()

    for key in sorted(header_keys):
        print("header key:{0}, value: {1}".format(key, stockChart.header_dic.get(key)))
    print("====================")
    for key in sorted(compare_mark_keys):
        print("compare_mark key:{0}, value: {1}".format(key, stockChart.compare_mark_dic.get(key)))
    print("====================")
    for key in sorted(stock_status_keys):
        print("stock_status key:{0}, value: {1}".format(key, stockChart.stock_status_dic.get(key)))
    print("====================")
    for key in sorted(stock_field_keys):
        print("stock_field key:{0}, value: {1}".format(key, stockChart.stock_field_dic.get(key)))
    print("====================")


    

    


