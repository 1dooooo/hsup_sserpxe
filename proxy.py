# import sys
# sys.path.append("..")
from api import belong_trackingmore_api,datail_cainiao_api,detail_trackingmore_api
import random

def detail_proxy(code,compony):
    if _choice(1):
        result = datail_cainiao_api.detail(code)
    else:
        result = detail_trackingmore_api.detail(code,compony)
    return result
def _choice(r):
    if random.randint(0,r):
        return True
    return False

if __name__ == "__main__":
    print(detail_proxy("75168316327377","zto"))