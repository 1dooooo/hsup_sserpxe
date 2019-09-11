import os.path
import json

root_path = os.path.split(os.path.realpath(__file__))[0]


def get_all_user_phone():
    ids = []
    try:
        with open(root_path + "/phoneid.json", "r", encoding="utf8") as a:
            ids = json.loads(a.read())
    except Exception as e:
        open(root_path + "/phoneid.json", "w", encoding="utf8")
    return ids


def get_one_user_data(phoneid):
    data = []
    with open(root_path + "/data/" + phoneid + "_data.json", encoding="utf8") as a:
        data = json.loads(a.read())
    return data


def set_one_user_data(phoneid, data):
    with open(root_path + "/data/" + phoneid + "_data.json", "w", encoding="utf8") as a:
        a.write(json.dumps(data, ensure_ascii=False))
    return


def get_one_user_config(phoneid):
    config = []
    with open(root_path + "/config/" + phoneid + "_config.json", encoding="utf8") as b:
        config = json.loads(b.read())
    return config


def set_one_user_config(phoneid, config):
    with open(root_path + "/config/" + phoneid + "_config.json", "w", encoding="utf8") as b:
        b.write(json.dumps(config, ensure_ascii=False))
    return
