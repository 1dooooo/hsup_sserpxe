from push import sc_noti
import os
ERROR = ("ERROR_FAULT_CODE", "ERROR_NOT_CODE", "ERROR_UNKNOW")
SUCCESS = ("SUCCESS")
root_path = os.path.split(os.path.realpath(__file__))[0]




def handle(key,id,description,compony,status,result):
    if status in ERROR:
        print('快递单号数据出错！', i, '\n')
        data[id]['last_time'] = ""
        data[id]['state'] = "单号错误"
        data[id]['description'] = description
        sc_noti(key, description, "单号错误，请重新添加！")
    else:
        last_time = result.get('messages')[0].get('time')
        context = result.get('messages')[0].get('context')
        full = result.get('messages')

        if last_time != data.get(id).get('last_time'):
            data[id]['last_time'] = last_time
            data[id]['state'] = result.get('status')
            data[id]['description'] = description
            sc_noti(key, description, full)
            print("更新数据为 : {context}\n".format(context=context))
        else:
            print("未更新数据")