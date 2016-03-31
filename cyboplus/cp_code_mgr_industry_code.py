import win32com.client
import datetime

def cp_code_mgr():
    """ Market 별 소속된 종목 코드 및 종목 명을 print 한다. 

        Args: 
            없습니다.

        Returns:
            code 명 - 산업명 
            code - 산업코드 
            groupName : 그룹명(계열사명)
            groupCode : 그룹코드 
            ex. 
                code: 대형(시가총액)(002), groupCode: BGF리테일(A027410)

    """
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

    codes1 = instCpCodeMgr.GetKosdaqIndustry2List()
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
