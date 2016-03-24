import json
import os
import datetime
import requests
import re
import time
from collections import Counter

class Crawl:
    def __init__(self):
        self.dirname = os.path.dirname(__file__)
        pass

    def parse_code(self, filename):
        target = open('wics_count.csv', 'w', encoding='utf-8')
        try:
            counter = Counter()
            str_list = []
            #fullpath = os.path.join(self.dirname, filename)
            fullpath = os.path.join(os.path.dirname(__file__), filename)
            print("fullpath: ", fullpath)

            with open(fullpath, 'r', encoding='utf-8') as f:
                count = 0
                for line in f.readlines():
                    strings = line.split('\t')
                    code = strings[1]
                    print(code)

                    count += 1
                    if count % 10 == 0:
                        print("count: {}".format(str(count)))

                    if count % 500 == 0:
                        print("sleep 1 sec...")
                        time.sleep(1)

                    with open('downloads/'+code+".html", 'r', encoding='utf-8') as ff:
                        for candidate in ff.readlines():
                            found = ''
                            if 'WICS :' in candidate:
                                m = re.search('(?<=<dt class="line-left">).+', candidate)
                                found = m.group(0).replace('</dt>', '').replace(' ', '')
                                print(found)
                                counter[found] += 1
                                break

            for k, v in counter.most_common():
                result = "{} {}\n".format(k, v)
                target.write(result)

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
    crawl.parse_code(today+'_stock_codes.csv')

