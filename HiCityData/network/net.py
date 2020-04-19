import json

import requests


class ForeCast:
    """
    天气预报网络请求
    """
    @staticmethod
    def get(code: str):
        """
        对requests的简单封装
        @param code: 城市代码
        @return: requests响应对象
        """
        return requests.get("http://wthrcdn.etouch.cn/weather_mini?citykey=" + code)

    @staticmethod
    def get_forecast(code: str):
        """
        @param code: 城市代码
        @return: 天气预报文本（String）
        """
        r = ForeCast.get(code)
        if r.status_code == 200:
            return True, ForeCast.regular_forecast(r.text)
        return False

    @staticmethod
    def regular_forecast(forecast: str):
        """
        解包天气预报json，返回天气预报文本（String）
        @param forecast: 天气预报json（String）
        @return: 天气预报文本（String）
        """
        js = json.loads(forecast)["data"]["forecast"]
        res = ""
        for i in js:
            for j in i.keys():
                res += i[j] + "\n"
            res += "\n"
        return res

    @staticmethod
    def get_forecast_json(code: str):
        """
        返回天气预报json对象
        @param code:城市代码
        @return: 天气预报json(<class map>)
        """
        r = ForeCast.get(code)
        if r.status_code == 200:
            return True, json.loads(r.text)["data"]
        return False
