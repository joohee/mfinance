import json
import os
import datetime
import requests
import re
import time

class Crawl:
    def __init__(self):
        self.dirname = os.path.dirname(__file__)
        pass

    def parse_code(self, filename):
        config = self.parse_json()
        prefix = config.get('prefix_url')

        target = open('output.csv', 'w', encoding='utf-8')
        try:
            str_list = []
            fullpath = os.path.join(os.path.dirname(__file__), filename)
            print("fullpath: ", fullpath)

            with open(fullpath, 'r', encoding='utf-8') as f:
                count = 0
                for line in f.readlines():
                    count += 1
                    if count % 10 == 0:
                        print("count: {}".format(str(count)))

                    if count % 500 == 0:
                        print("sleep 1 sec...")
                        time.sleep(1)

                    columns = line.split('\t')
                    #print(columns)
                    code = columns[1]
                    name = columns[2]
                    market_code = columns[3]
                    market_name = columns[4].replace('\n', '')

                    str_list.append(code)
                    str_list.append(name)
                    str_list.append(market_code)
                    str_list.append(market_name)
                    
                    #print(prefix.format(code[1:len(code)]))
                    response = requests.get(prefix.format(code[1:len(code)]))

                    if response.status_code == 200:
                        with open('downloads/'+code+".html", 'w', encoding='utf-8') as ff:
                            ff.write(response.text)

                        existWICS = False 
                        for rline in response.iter_lines():
                            #print(rline)
                            candidate = rline.decode()
                            found = ''
                            if 'WICS :' in candidate:
                                m = re.search('(?<=<dt class="line-left">).+', candidate)
                                found = m.group(0)
                                #print(found.replace('</dt>', ''))
                                str_list.append(found.replace('</dt>', ''))
                                target.write('\t'.join(str_list))
                                target.write('\n')
                                del str_list[:]
                                existWICS = True
                                break

                        if existWICS == False:
                            target.write('\t'.join(str_list))
                            target.write('\n')
                            del str_list[:]
                                
                    else:
                        print('error...')
            target.close()

        except IOError as e:
            print("[IOError] {0} not found...{1}".format(filename, e))

    def parse_json(self):
        fullpath = os.path.join(self.dirname, 'config.json')

        try:
            with open(fullpath, 'r', encoding='utf-8') as f:
                config = json.loads(f.read())
                return config
        except IOError as e:
            print("File not found...", e);
            return

if __name__ == '__main__':
    crawl = Crawl()
    config = crawl.parse_json()
    #print(config)
    print(config.get('prefix_url'))

    today = datetime.datetime.now().strftime('%Y%m%d')
    crawl.parse_code(today+'_stock_codes_test.csv')
