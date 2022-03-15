#!/usr/bin/env python
from ast import And
import numpy as np
import pandas as pd
import datetime
import requests
import json
import time

header={
        'Accept-Encoding':'gzip, deflate, br',
        'Connection':'keep-alive',
        'Referer':'https://data.stats.gov.cn/easyquery.htm?cn=A01',
        'Host':'data.stats.gov.cn',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.36',
        'X-Requested-With':'XMLHttpRequest'
       }

def random_timestamp():
    return str(int(round(time.time() * 1000)))

def stats_money_supply():
    url='https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgyd&rowcode=zb&colcode=sj&wds=[]&dfwds=[{"wdcode":"zb","valuecode":"A0D01"}]&k1='+random_timestamp()+'&h=1'
    requests.packages.urllib3.disable_warnings()
    r = requests.get(url,headers=header, verify=False)
    ret=r.json()
    if ret['returncode'] == 200 :
        for n in ret['returndata']['datanodes']:
            if n['data']['hasdata'] == True:
                print(n['wds'][0]['valuecode'],n['wds'][1]['valuecode'],n['data']['data'])

stats_money_supply() 