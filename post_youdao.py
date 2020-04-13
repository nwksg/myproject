from random import random
import random
import requests

# url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
# content = " 我爱中国 "


class Youdao():
    def __init__(self, content):
        self.content = content
        self.url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        self.ts = self.get_ts()
        self.salt = self.get_salt()
        self.sign = self.get_sign()

    def get_salt(self):
        s = str(random.randint(0, 10))
        t = self.ts
        return t + s

    def get_md5(self, value):
        import hashlib
        m = hashlib.md5()
        m.update(value.encode("utf-8"))
        return m.hexdigest()

    def get_sign(self):
        e = self.content
        i = self.salt
        s = "fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj"
        return self.get_md5(s)

    def get_ts(self):
        import time
        t = time.time()
        ts = str(int(round(t * 1000)))
        return ts

    def yield_form_data(self):
        form_data = {
            'i': self.content,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': self.salt,
            'sign': self.sign,
            'ts': self.ts,
            'bv': '0df9f5b4c71ae0497eb62f86d25ed05b',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }
        return form_data

    def get_headers(self):
        headers = {
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-891979111@10.108.160.17; OUTFOX_SEARCH_USER_ID_NCOO=1761989640.4588385; _ntes_nnid=86bc47b67c933d9fce4a2e4cb11e8ae1,1583465980374; JSESSIONID=aaaizOhDuuIQAbNQkLXfx; SESSION_FROM_COOKIE=unknown; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcij4oWdK2hB_yRTSXfx; ___rl__test__cookies=1586762011753',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.204 Safari/537.36'
        }
        return headers

    def fanyi(self):
        response = requests.post(self.url, data=self.yield_form_data(), headers=self.get_headers())
        return response.text


if __name__ == '__main__':
    youdao = Youdao('南即离马')
    print(youdao.fanyi())