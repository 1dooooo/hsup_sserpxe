import json
import os.path
import time
import requests
import re

from handle import handle_data, handle_result
from proxy import detail_proxy, belong_to_proxy
from info import get_all_user_phone, get_one_user_config, get_one_user_data, set_one_user_data


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


def is_jd_express(id):
    if id.find("jd") >= 0 or id.find("JD") >= 0:
        return "jd"
    else:
        return None


def send(phoneid):

    data = get_one_user_data(phoneid)
    config = get_one_user_config(phoneid)

    data_new = {}
    key = config.get("key")
    for i in config.get("post_list"):
        id = i.get('id')
        company = i.get('company')
        if not company:
            company = is_jd_express(id)
            company = belong_to_proxy(id)
        description = i.get('description')

        if not id or not description:
            print('\nconfig.py文件错误！', i, '\n')
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
            print("请求接口错误\n")
            print(e)
            continue
        state, result = handle_result(api_com, result, company)
        data[id] = handle_data(data[id], key, description,
                               state, result, company=company)

        # 写入数据，舍弃旧数据
        data_new[id] = data[id]
        time.sleep(6)

    set_one_user_data(phoneid, data_new)


ids = get_all_user_phone()
for phoneid in ids.get("phoneid"):
    print(
        "+ = + = + = + = + ={phoneid} + = + = + = + = + =".format(phoneid=phoneid))
    send(phoneid)
