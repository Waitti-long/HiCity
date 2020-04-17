import json

import requests


class ForeCast:
    @staticmethod
    def get(code: str):
        return requests.get("http://wthrcdn.etouch.cn/weather_mini?citykey=" + code)

    @staticmethod
    def get_forecast(code: str):
        r = ForeCast.get(code)
        if r.status_code == 200:
            return True, ForeCast.regular_forecast(r.text)
        return False

    @staticmethod
    def regular_forecast(forecast: str):
        js = json.loads(forecast)["data"]["forecast"]
        res = ""
        for i in js:
            for j in i.keys():
                res += i[j] + "\n"
            res += "\n"
        return res

    @staticmethod
    def get_forecast_json(code: str):
        r = ForeCast.get(code)
        if r.status_code == 200:
            return True, json.loads(r.text)["data"]
        return False
