import requests
url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
form_data = {
     'i': '我爱中国',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '15846832363666',
    'sign': '809144ef068d33d6c454d24cd8a0013e',
    'ts': '1584683236366',
    'bv': '0df9f5b4c71ae0497eb62f86d25ed05b',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME'
}
response = requests.post(url, form_data)
print(response.text)