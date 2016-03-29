import win32com.client
import datetime

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
