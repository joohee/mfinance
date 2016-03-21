import win32com.client
import datetime

# Template => 실제 호출할 API 이름으로 변경해서 사용.
class CPTemplate:
    def __init__(self):
        pass

    def exec(self, apiName):
        inst = win32com.client.Dispatch(apiName)

        print("=========================\n")
        today = datetime.datetime.now()
        with open(today.strftime('%Y%m%d')+'_template.csv', 'w', encoding='utf-8') as f:
            f.write('\n')

if __name__ == '__main__':
    apiName = 'ApiName'
    print("====== {}  =======".format(apiName))

    template = CPTemplate()
    template.exec(apiName)

