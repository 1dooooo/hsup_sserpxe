from push import serverjiang_push
import os
import time
ERROR = ("ERROR_FAULT_CODE", "ERROR_NOT_CODE", "ERROR_UNKNOW")
SUCCESS = ("SUCCESS")
root_path = os.path.split(os.path.realpath(__file__))[0]


def fix_time(to_fix_time, to_add):
    '''
    Add specific seconds to a given time, return the result time\n
    to_fix_time: str presented time\n
    to_add: seconds needed to add\n
    return str presented result time
    '''
    # 2019-09-03 05:34:29
    fixed_time_stamp = int(time.mktime(time.strptime(
        to_fix_time, "%Y-%m-%d %H:%M:%S"))) + int(to_add)
    fixed_time = time.strftime(
        "%Y-%m-%d %H:%M:%S", time.localtime(fixed_time_stamp))
    return fixed_time


def handle_result(api_com, result_json, company=None):
    track = []
    state = None
    if api_com == "cainiao":
        if str(result_json["status"]) == "1":
            track = result_json["data"]["messages"]
            if result_json["data"]["status"] != "已签收":
                state = "运输中"
            else:
                state = "已签收"
    elif api_com == "tracking":
        if str(result_json["originCountryData"]["infoState"]) == "2":
            original_track = result_json["originCountryData"]["trackinfo"]
            for item in original_track:
                temp_item = {}
                temp_item["time"] = item["Date"]
                if company == "jd":
                    temp_item["time"] = fix_time(item["Date"], 60*60*8)
                temp_item["context"] = item["StatusDescription"]
                track.append(temp_item)
            if str(result_json["originCountryData"]["stausDataNum"]) != "4":
                state = "运输中"
            else:
                state = "已签收"
    else:
        pass
    return state, track


def handle_data(data, key, description, state, result, company=None):
    if not(state and result):
        return data
    last_time = result[0].get('time')
    context = result[0].get('context')
    if last_time != data.get('last_time'):
        data['last_time'] = last_time
        data['state'] = state
        data['description'] = description
        data['company'] = company
        serverjiang_push(key, description, result)
        print("更新数据为 : {context}\n".format(context=context))
    else:
        print("未更新数据."+"in\t "+last_time+"\n")
    return data
    # if status in ERROR:
    #     print('快递单号数据出错！', i, '\n')
    #     data[id]['last_time'] = ""
    #     data[id]['state'] = "单号错误"
    #     data[id]['description'] = description
    #     sc_noti(key, description, "单号错误，请重新添加！")
    # else:
    #     last_time = result.get('messages')[0].get('time')
    #     context = result.get('messages')[0].get('context')
    #     full = result.get('messages')

    #     if last_time != data.get(id).get('last_time'):
    #         data[id]['last_time'] = last_time
    #         data[id]['state'] = result.get('status')
    #         data[id]['description'] = description
    #         sc_noti(key, description, full)
    #         print("更新数据为 : {context}\n".format(context=context))
    #     else:
    #         print("未更新数据")
