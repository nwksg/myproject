import requests


class HeFeng():
    def __init__(self):
        self.url="https://cdn.heweather.com/china-city-list.txt"

    def get_weather(self,city_code):
        url="https://free-api.heweather.net/s6/weather/now?location=" + city_code + "&key=34e4a8c077c9471fb68b3438726e93d4"
        info=requests.get(url)
        info.encoding='utf8'
        print(info.text)

    def get_city_code(self):
        cities = self.get_citys()
        for each in cities:
            yield each[2:13]

    def get_citys(self):
        html = requests.get(self.url)
        html.encoding='utf8'
        cities = html.text.split('\n')
        return cities[6:]


if __name__ == '__main__':
    hefeng = HeFeng()
    codes = hefeng.get_city_code()
    print(hefeng.get_weather(codes.__next__()))
