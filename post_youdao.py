from random import random
import random
import requests
url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


def get_salt():
    t=get_ts()
    s= str(random.randint(0,10))
    # print(s)
    # print(t)
    # print(t+s)
    return t+s
    # return '15846832363666'


def get_sign():
    return '809144ef068d33d6c454d24cd8a0013e'


def get_ts():
    import time
    t = time.time()
    ts = str(int(round(t * 1000)))
    return ts


form_data = {
     'i': '我爱中国',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': get_salt(),
    'sign': get_sign(),
    'ts': get_ts(),
    'bv': '0df9f5b4c71ae0497eb62f86d25ed05b',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME'
}
response = requests.post(url, form_data)
print(response.text)