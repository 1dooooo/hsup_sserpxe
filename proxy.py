# import sys
# sys.path.append("..")
from api import belong_trackingmore_api, datail_cainiao_api, detail_trackingmore_api
import random


def _choice(r, company):
    if company:
        if company == "jd":
            return True
        if random.randint(0, r):
            return True
    return False


def detail_proxy(code, company=None):
    try:
        if _choice(2, company):
            api_com = "tracking"
            print("try with "+api_com)
            result = detail_trackingmore_api.detail(code, company)
            if not result['lastEvent']:
                raise RuntimeError('empty result')
        else:
            api_com = "cainiao"
            print("try with "+api_com)
            result = datail_cainiao_api.detail(code)
    except Exception as e:
        print("请求接口错误 with "+api_com)
        print(e)
        if not api_com == "cainiao":
            api_com = "cainiao"
            print("re-try with "+api_com)
            result = datail_cainiao_api.detail(code)
    
    return api_com, result


def belong_to_proxy(code):
    try:
        return belong_trackingmore_api.belong(code)
    except:
        return ""

