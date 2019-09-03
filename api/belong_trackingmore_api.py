import requests
import json
import re
url = "https://www.trackingmore.com/index_ajax.php"
usual_code_list = [
    "京东快递", "顺丰国际", "顺丰速运", "申通快递", "圆通快递", "天天快递", "中通快递", "宅急送快递", "韵达快递",
    "德邦物流", "百世快递", "百世快运", "速通物流", "优速快递", "速尔快递", "中国 EMS", "TNT", "中国邮政",
    "中铁物流", "CNE国际快递", "捷买送", "递四方", "安骏物流", "J-NET捷网", "深圳淼信国际物流"
]
headers = {
    # "accept":
    # "*/*",
    # "accept-encoding":
    # "gzip, deflate, br",
    # "accept-language":
    # "zh-CN,zh;q=0.9",
    # "cookie":
    # "acw_tc=ca6cf99d15664748960487885efc6ab2a93770740918201ea223089c40; _ga=GA1.2.1960427446.1566474897; cookieLang=cn; _gid=GA1.2.429958757.1566803819; normalTr0019=VXNVIlM6VjgFZgRtWjAJJgJvXHIHMFA2BzBQOAowWWtQZwlpAExRJgthVSdSIQ9gUmQJfAF5A2QDPVI7CicCLVUqVXVTLFYwBXUEbVo4CSYCb1xyB2lQZgdgUGUKNll4UCEJfgB4USALaFU2Uj8Pa1JrCWIBOgNoAyBSMwpKAnNVW1VoUzBWJQVuBGJaJQkmAm9ccgdhUHYHKw%3D%3D; PHPSESSID=s6sf8qjn91jvv2eaninpmttc03; _gat=1; express1=%7B%22china-post%22%3A1%7D; code+COO=ecyxJpjhbp2RlMiI6WyI2cjNoWSJdfQO0O0OO0O0O; Thekeytoken=a5da6a1b0c4ea979ed485650c8eb6780; trackingmore=a21032fb1aebdedcaa35c04b3b4c110b; verynginx_sign_cookie=7c5d114eef463733b2fae7e76cbbf360",
    # "referer":
    # "https://www.trackingmore.com/",
    # "sec-fetch-mode":
    # "no-cors",
    # "sec-fetch-site":
    # "same-origin",
    "Referer":
    "https://www.trackingmore.com/index",
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
}
datas = {
    "lang": "cn",
    "tracknumber": "",
}


def is_usual(com_code):
    return com_code in usual_code_list


def belong(tracknumber):
    datas["tracknumber"] = tracknumber
    r = requests.post(url, data=datas, headers=headers)
    com_lsit = json.loads(r.text)
    for item in com_lsit:
        if is_usual(item["company_name"]):
            return item["company_code"]
    return com_lsit[0]["company_code"]