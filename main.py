#   crontab -e
#   (*/30 * * * * python3 /www/wwwroot/idooooo.tk/express/main.py >> /www/wwwroot/idooooo.tk/express/out.log 2>&1)
#

import json
import os.path
import time
import requests
import re

root_path = os.path.split(os.path.realpath(__file__))[0]
# server酱的推送地址(https://sc.ftqq.com/)
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366 MicroMessenger/6.7.3(0x16070321) NetType/WIFI Language/zh_CN',
}

def query(id):
    url = "https://api.m.sm.cn/rest?method=kuaidi.getdata&sc=express_cainiao&q="+id+"&bucket=&callback=jsonp1"
    r = requests.get(url, headers=headers)
    result = re.search(r'jsonp1\((.*)\);',r.text,re.I)
    result = json.loads(result.group(1))
    if result['status'] != 1:
        print(result)
        return False
    else:
        return result["data"]

def sc_noti(key, description, full):
    text = '!!{description}!!快递状态变化'.format(description=description)

    desp = ''
    for i in full:
        desp = desp + '{time} **{stat}**\n\n'.format(time=i.get('time'), stat=i.get('context'))

    print(text)

    sc_url = 'https://sc.ftqq.com/'+key+'.send'
    requests.post(sc_url, data={'text': text, 'desp': desp})


def send(phoneid):
    with open(root_path + "/data/" + phoneid +"_data.json", encoding="utf8") as a:
        data = json.loads(a.read())

    with open(root_path + "/config/" + phoneid +"_config.json", encoding="utf8") as b:
        config = json.loads(b.read())

    data_n = {}

    for i in config.get("post_list"):
        id = i.get('id')
        description = i.get('description')

        if not id or not description:
            print('\nconfig.py文件错误！', i, '\n')
            exit(0)

        # 如果是一个新的数据
        if not data.get(id):
            data[id] = {}
            data[id]['last_time'] = '0'

        # 状态已经是已签收
        if data.get(id).get('state', '0') == "已签收" or data.get(id).get('state', '0') == "\u5df2\u7b7e\u6536":
            data_n[id] = data[id]
            continue

        print("-----------"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"-----------")
        print("尝试读取{description}:{id}".format(description=description,id=id))
        result = query(id)
        

        if not result:
            print('获取api数据出错！', i, '\n')
            continue

        last_time = result.get('messages')[0].get('time')
        context = result.get('messages')[0].get('context')
        full = result.get('messages')

        if last_time != data.get(id).get('last_time'):
            data[id]['last_time'] = last_time
            data[id]['state'] = result.get('status')
            data[id]['description'] = description
            sc_noti(config.get("key"),description, full)
            print("更新数据为 : {context}\n".format(context=context))
        else :
            print("未更新数据")

        # 写入数据，舍弃旧数据
        data_n[id] = data[id]
        time.sleep(6)

    with open(root_path + "/data/" + phoneid +"_data.json", "w",encoding="utf8") as a:
        a.write(json.dumps(data_n,ensure_ascii=False))


with open(root_path + "/phoneid.json",encoding="utf8") as a:
    ids = json.loads(a.read())
    for phoneid in ids.get("phoneid"):
        print("+ = + = + = + ={phoneid} + = + = + = + = + =\n".format(phoneid=phoneid))
        send(phoneid)