import requests

headers = {
    'User-Agent':
    'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366 MicroMessenger/6.7.3(0x16070321) NetType/WIFI Language/zh_CN',
}


def sc_noti(key, description, full):
    text = '!-{description}-!快递状态变化'.format(description=description)

    desp = ''
    for i in full:
        desp = desp + '{time} **{state}**\n\n'.format(time=i.get('time'),
                                                      state=i.get('context'))
    print(text)

    if key =="test":
        return
    sc_url = 'https://sc.ftqq.com/' + key + '.send'
    requests.post(sc_url, data={'text': text, 'desp': desp})