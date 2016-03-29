import win32com.client
import datetime 
from cp_code_mgr.codes import CpCodeMgrCode

def cp_code_mgr():
    codes = CpCodeMgrCode()
    today = datetime.datetime.now()

    today = datetime.datetime.now()
    with open(today.strftime('%Y%m%d')+'_cpCodeMgr_industryList.csv', 'w', encoding='utf-8') as f:
        instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
        for i in range(1, len(codes.stock_market_code_dic)):
            codeList = instCpCodeMgr.GetStockListByMarket(i)
            # industryList: 증권전산업종 코드 리스트를 반환한다.
            industryList = instCpCodeMgr.GetIndustryList()

            for idx in range(len(industryList)):
                industryName = instCpCodeMgr.GetIndustryName(industryList[idx])
                #line = "market: {3}({2}),  code: {0}, name: {1}".format(industryList[idx], industryName, i, codes.get_stock_market_kind(str(i)))
                #print(line)
                #f.write(line+'\n')
            # GetGroupCodeList: 관심종목(700 ~799 ) 및 업종코드(GetIndustryList 참고)에 해당하는 종목배열을 반환한다.
                groupCodeList = instCpCodeMgr.GetGroupCodeList(industryList[idx])
                for j in range(len(groupCodeList)):
                    groupCode = groupCodeList[j]
                    groupName = instCpCodeMgr.CodeToName(groupCode)
                    #print("\ncode: {}({}), groupCode: {}({})".format(industryName, industryList[idx], groupName, groupCodeList[j]))
                    line = "{0}\t{1}\t{2}\t{3}\n".format(industryList[idx], industryName, groupCodeList[j], groupName)
                    f.write(line)
            #memberList = instCpCodeMgr.GetMemberList()
            #for idx in range(len(memberList)):
            #    memberName = instCpCodeMgr.GetMemberName(memberList[idx])
            #    line = "\tmember code: {0}, name: {1}".format(memberList[idx], memberName)
            #    print(line)
            #    f.write(line+'\n')
            # KosdaqIndustry1List: 코스닥산업별 코드리스트를 반환한다.
            #codes1 = instCpCodeMgr.GetKosdaqIndustry1List()
            #for idx in range(len(codes1)):
            #    print("index: {}, code: {}".format(idx, codes1[idx]))
            #print("============")
            # GetKosdaqIndustry2List: 코스닥지수업종 코드리스트를 반환한다.
            #codes2 = instCpCodeMgr.GetKosdaqIndustry2List()
            #for idx in range(len(codes2)):
            #    print("index: {}, code: {}".format(idx, codes2[idx]))
            #print("============")

if __name__ == '__main__':
    print("====== CpCodeMgr =======")
    cp_code_mgr()

