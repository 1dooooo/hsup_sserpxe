import json
import os.path
import time
import requests
import re

# from logger import logger
from handle import handle_data, handle_result
from proxy import detail_proxy, belong_to_proxy
from info import get_all_user_phone, get_one_user_config, get_one_user_data, set_one_user_data,set_one_user_config


ERROR = ("ERROR_FAULT_CODE", "ERROR_NOT_CODE", "ERROR_UNKNOW")
SUCCESS = ("SUCCESS")
root_path = os.path.split(os.path.realpath(__file__))[0]


def is_signed(state):
    flag = False
    if state == "已签收" or state == "\u5df2\u7b7e\u6536":
        flag = True
    if state == "单号错误":
        flag = True
    if state == "不支持":
        flag = True
    return flag


def get_express_from_id(id):
    if id.find("jd") >= 0 or id.find("JD") >= 0:
        return "jd"
    if id.find("YT") >= 0 or id.find("yt") >= 0:
        return "yto"
    if id.find("TT") >= 0 or id.find("tt") >= 0:
        return "ttkd"
    if id.find("SF") >= 0 or id.find("sf") >= 0:
        return "sf-express"
    else:
        return belong_to_proxy(id)


def send(phoneid):
    data = get_one_user_data(phoneid)
    config = get_one_user_config(phoneid)
    config_hash = hash(str(config))

    data_new = {}
    key = config.get("key")
    items = config.get("items")
    for id,info in items.items():
        company = info.get('company')
        if not company:
            company = get_express_from_id(id)
            config["items"][id]["company"] = company
        description = info.get('description')
        if not id or not description:
            print('\nconfig.py文件错误！', id, '\n')
            return

        # 如果是一个新的数据
        if not data.get(id):
            data[id] = {}
            data[id]['last_time'] = '0'

        # 状态已经是已签收
        if is_signed(data.get(id).get('state', '0')):
            data_new[id] = data[id]
            continue

        print("---------------{time}---------------".format(
            time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        print("尝试读取{description}:{id}".format(description=description, id=id))
        try:
            api_com, result = detail_proxy(id, company)
        except Exception as e:
            print("请求接口错误 with "+e)
            continue
        state, result = handle_result(api_com, result, company)
        data[id] = handle_data(data[id], key, description,
                               state, result, company=company)

        # 写入数据，舍弃旧数据
        data_new[id] = data[id]
        time.sleep(1)

    set_one_user_data(phoneid, data_new)
    if not config_hash == hash(str(config)):
        set_one_user_config(phoneid,config)

phoneids = get_all_user_phone()
for phoneid in phoneids.get("phoneid"):
    print("+ = + = + = {t} = + = + ={phoneid}+ = + = + = {t} = + = + =".format(
        phoneid=phoneid, t=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
    send(phoneid)
