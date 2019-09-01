# import sys
# sys.path.append("..")
from api import belong_trackingmore_api, datail_cainiao_api, detail_trackingmore_api
import random


def detail_proxy(code, company=None):
    if _choice(100) and company != None:
        api_com = "tracking"
        result = detail_trackingmore_api.detail(code, company)
    else:
        api_com = "cainiao"
        result = datail_cainiao_api.detail(code)
    return api_com, result


def _choice(r):
    if random.randint(0, r):
        return True
    return False


# if __name__ == "__main__":
#     print(detail_proxy("75168316327377", "zto"))
