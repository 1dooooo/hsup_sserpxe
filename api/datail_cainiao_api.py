import requests
import json
import re
headers = {
    'User-Agent':
    'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366 MicroMessenger/6.7.3(0x16070321) NetType/WIFI Language/zh_CN',
}

ERROR = ("ERROR_FAULT_CODE", "ERROR_NOT_CODE", "ERROR_UNKNOW")
SUCCESS = ("SUCCESS")

def detail(id):
    url = "https://api.m.sm.cn/rest?method=kuaidi.getdata&sc=express_cainiao&q=" + id + "&bucket=&callback=jsonp1"
    r = requests.get(url, headers=headers)
    result = re.search(r'jsonp1\((.*)\);', r.text, re.I)
    result = json.loads(result.group(1))
    return result
    # if not result['data']["company"]:
    #     return "ERROR_FAULT_CODE", ""
    # elif result['status'] == 1:
    #     return "SUCCESS", result["data"]
    # elif result['status'] == 0:
    #     return "ERROR_NOT_CODE", ""
    # else:
    #     return "ERROR_UNKNOW", ""