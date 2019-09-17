import os.path
import json

root_path = os.path.split(os.path.realpath(__file__))[0]


def get_all_user_phone():
    '''
    return: list contain all phoneids, or None if file not exist
    '''
    phoneid_path = root_path + "/phoneid.json"
    if not os.path.exists(phoneid_path):
        fp = open(phoneid_path, "w", encoding="utf-8")
        fp.write("{}")
        fp.close()
        return None
    phoneids = json.load(open(phoneid_path, encoding="utf-8"))
    if not phoneids.__contains__("phoneid"):
        return None
    return phoneids.get("phoneid")


def get_one_user_data(phoneid):
    '''
    return: dict or None if file not exist
    '''
    user_path = root_path + '/data/' + str(phoneid) + '_data.json'
    if not os.path.exists(user_path):
        return None
    return json.load(open(user_path, encoding="utf-8"))


def set_one_user_data(phoneid, data):
    json.dump(data, open(root_path + '/data'+str(phoneid) +
                         '_data.json', "w", encoding="utf-8"), ensure_ascii=False)
    return


def get_one_user_config(phoneid):
    '''
    return: dict or None
    // TODO Will the file be empty?
    '''
    config_path = root_path + "/config/" + phoneid + "_config.json"
    if not os.path.exists(config_path):
        return None
    return json.load(open(config_path, encoding="utf-8"))


def set_one_user_config(phoneid, config):
    json.dump(config, open(root_path + "/config/" + phoneid +
                           "_config.json", "w", encoding="utf8"), ensure_ascii=False)
