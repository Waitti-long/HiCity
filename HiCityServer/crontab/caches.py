from .tools import Tool
from HiCityData import entity
import json


class ForeCastCache:
    data = {}
    __sql = None

    @staticmethod
    def add(city_code, all_forecast):
        json_class = all_forecast[0]
        time = Tool.get_regular_now()
        ds = {"high": json_class["high"],
              "fengli": json_class["fengli"],
              "low": json_class["low"],
              "fengxiang": json_class["fengxiang"],
              "type": json_class["type"],
              "all": json.dumps(all_forecast)}
        if city_code not in ForeCastCache.data:
            ForeCastCache.data[city_code] = {}
        ForeCastCache.data[city_code][time] = json.dumps(ds)
        ForeCastCache.store(ForeCastCache.__sql)

    @staticmethod
    def store(sql):
        """
        持久化数据
        @param sql: HiCityData.SQL
        """
        session = sql.session()
        for i in ForeCastCache.data:
            for j in ForeCastCache.data[i]:
                key = i + str(j)
                alls = []
                ddd = ForeCastCache.data
                k = json.loads(ForeCastCache.data[i][j])
                ds = entity.Forecast()
                ds.id = key
                ds.data = ForeCastCache.data[i][j]
                ds.code = i
                ds.date = j
                alls.append(ds)
                try:
                    session.add_all(alls)
                    session.commit()
                except Exception as err:
                    session.rollback()
        session.close()

    @staticmethod
    def read(sql):
        """
        从数据库中加载数据
        @param sql: HiCityData.SQL
        """
        ForeCastCache.__sql = sql
        session = sql.session()
        fs = session.query(entity.Forecast).all()
        for i in fs:
            if i.code not in ForeCastCache.data:
                ForeCastCache.data[i.code] = {}
            ForeCastCache.data[i.code][i.date] = i.data
        session.close()
