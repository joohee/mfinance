import win32com.client
import datetime 
from packges.cp_code_mgr.codes import CpCodeMgrCode

def cp_code_mgr():
    codes = CpCodeMgrCode()
    today = datetime.datetime.now()

    instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
    for i in range(1, len(codes.stock_market_code_dic)):
        codeList = instCpCodeMgr.GetStockListByMarket(i)
        # industryList: 증권전산업종 코드 리스트를 반환한다.
        industryList = instCpCodeMgr.GetIndustryList()
        for idx in range(len(industryList)):
            industryName = instCpCodeMgr.GetIndustryName(codes[idx])
            print("code: {0}, name: {1}".format(codes[idx], industryName))

            # GetGroupCodeList: 관심종목(700 ~799 ) 및 업종코드(GetIndustryList 참고)에 해당하는 종목배열을 반환한다.
            #groupCodeList = instCpCodeMgr.GetGroupCodeList(codes[idx])
            #for j in range(len(groupCodeList)):
                #groupCode = groupCodeList[j]
                #groupName = instCpCodeMgr.CodeToName(groupCode)
                #print("code: {}({}), groupCode: {}({})".format(industryName, codes[i], groupName, groupCodeList[j]))
        
        # KosdaqIndustry1List: 코스닥산업별 코드리스트를 반환한다.
        codes1 = instCpCodeMgr.GetKosdaqIndustry1List()
        for idx in range(len(codes1)):
            print("index: {}, code: {}".format(idx, codes1[idx]))
        print("============")
        # GetKosdaqIndustry2List: 코스닥지수업종 코드리스트를 반환한다.
        codes2 = instCpCodeMgr.GetKosdaqIndustry2List()
        for idx in range(len(codes2)):
            print("index: {}, code: {}".format(idx, codes2[idx]))
        print("============")

if __name__ == '__main__':
    print("====== CpCodeMgr =======")
    cp_code_mgr()

