# 天气查询脚本

import requests
import json
import time


class Query():
    def __init__(self):
        self.url1 = 'http://api.map.baidu.com/weather/v1/?district_id={}&data_type=all&ak=Nh0mbwMGOETmqe2B1jWvAQK4Hk88szAX'
        self.url2 = 'http://www.weather.com.cn/data/sk/{}.html'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }

    def get_data(self, city_name):
        results = {}
        # part1
        res = requests.get(self.url1.format(self.code(city_name)), headers=self.headers)
        # res = requests.get(self.url1.format(city_name), headers=self.headers)
        try:
            data1 = json.loads(res.text)
        except:
            print('[Error]Cannot find the city weather info...')
            return None
        try:
            date = data1["result"]["forecasts"][0]["date"]
        except:
            date = None
        try:
            rh = data1["result"]["now"]["rh"]
        except:
            rh = None
        try:
            Htemperature = str(data1["result"]["forecasts"][0]["high"])
            Ltemperature = str(data1["result"]["forecasts"][0]["low"])
        except:
            Htemperature, Ltemperature = None, None
        try:
            weather = data1["result"]["forecasts"][0]["text_day"]
        except:
            weather = None
        # part2
        # param = str(time.time()).split('.')[0]
        try:
            res = requests.get(self.url2.format(self.city2code(city_name)), headers=self.headers)
            res.encoding = 'utf-8'
            data2 = json.loads(res.text)
        except:
            print('[Error]Cannot find the city weather info...')
            return None
        try:
            SD = data2["weatherinfo"]['SD']
        except:
            SD = None
        try:
            QY = data2['weatherinfo']['qy']
        except:
            QY = None
        # part3
        results['date'] = date
        results['Htemperature'] = Htemperature
        results['Ltemperature'] = Ltemperature
        results['weather'] = weather
        results['rh'] = rh
        results['SD'] = SD
        results['QY'] = QY
        return results

    def code(self, city_name):
        with open('code.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        f.close()
        try:
            return data[city_name + "市"]
        except:
            print('[ERROR]:City name error...')
            return None

    def city2code(self, city_name):
        with open('city_code.json', 'r') as f:
            data = json.load(f)
        f.close()
        try:
            return data[city_name]
        except:
            print('[ERROR]:City name error...')
            return None


if __name__ == '__main__':
    Query().get_data('南京')
# Query().city2code('上海')
