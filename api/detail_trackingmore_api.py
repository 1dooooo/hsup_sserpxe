import execjs
import requests
import time
import random
import json
import re
import os

headers = {
    "accept":
    "*/*",
    "accept-encoding":
    "gzip, deflate, br",
    "accept-language":
    "zh-CN,zh;q=0.9",
    # "cookie":
    # "acw_tc=ca6cf99d15664748960487885efc6ab2a93770740918201ea223089c40; _ga=GA1.2.1960427446.1566474897; cookieLang=cn; _gid=GA1.2.429958757.1566803819; normalTr0019=VXNVIlM6VjgFZgRtWjAJJgJvXHIHMFA2BzBQOAowWWtQZwlpAExRJgthVSdSIQ9gUmQJfAF5A2QDPVI7CicCLVUqVXVTLFYwBXUEbVo4CSYCb1xyB2lQZgdgUGUKNll4UCEJfgB4USALaFU2Uj8Pa1JrCWIBOgNoAyBSMwpKAnNVW1VoUzBWJQVuBGJaJQkmAm9ccgdhUHYHKw%3D%3D; PHPSESSID=s6sf8qjn91jvv2eaninpmttc03; _gat=1; express1=%7B%22china-post%22%3A1%7D; code+COO=ecyxJpjhbp2RlMiI6WyI2cjNoWSJdfQO0O0OO0O0O; Thekeytoken=a5da6a1b0c4ea979ed485650c8eb6780; trackingmore=a21032fb1aebdedcaa35c04b3b4c110b; verynginx_sign_cookie=7c5d114eef463733b2fae7e76cbbf360",
    # "referer":
    # "https://www.trackingmore.com/",
    "sec-fetch-mode":
    "no-cors",
    "sec-fetch-site":
    "same-origin",
    "Referer":
    "https://www.trackingmore.com/index",
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
}
params = {
    "lang": "cn",
    "callback": "",
    "tracknumber": "",
    "express": "",
    "express_amazon": "",
    #"track_number_orderId_ge": "",
    "pt": "1",
    "tracm": "",
    #"destination": "",
    #"track_account": "",
    "account": "",
    "multiple": "1",
    #"againtrack": "",
    #"exception": "0",
    "validate": "",
    #"_": "",
}


def build_parems(tracknumber, express):
    params["tracknumber"] = tracknumber
    params["express"] = express

    random_list = random.choices("0123456789", k=15)
    random_str_15 = "".join(random_list)
    str_time = str(time.time()).split(".")
    cur_time = str_time[0] + str_time[1][:3]
    cur_time_last_1 = str(int(cur_time) - 1)
    cur_time_last_2 = str(int(cur_time) - 2)

    params["callback"] = "jQuery19107" + random_str_15 + "_" + cur_time_last_2
    params["validate"] = encrypt(params["tracknumber"], params["express"],
                                 cur_time)
    params["_"] = cur_time_last_1


def encrypt(tracknumber, express, c_time):
    root_path = os.path.split(os.path.realpath(__file__))[0]
    ctx = execjs.compile(open(root_path + "/js/encryption.js", 'r').read())
    mi = ctx.call("encryption", tracknumber, express, c_time)
    return mi


def detail(tracknumber, express):
    build_parems(tracknumber, express)
    url = "https://www.trackingmore.com/gettracedetail.php"
    r = requests.get(url, params=params, headers=headers)
    jsonp = r.text.replace("\/", "//").encode('utf-8').decode('unicode_escape')
    result_json = re.search(r'jQuery.*\((.*)\)',jsonp , re.I).group(1)
    return json.loads(result_json)
    # print(r.text.replace("\/", "//").encode('utf-8').decode('unicode_escape'))
