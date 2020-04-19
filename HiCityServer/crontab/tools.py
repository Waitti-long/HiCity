import time


class Tool:
    @staticmethod
    def get_regular_now():
        """
        @return: 今日零点的时间戳
        """
        ds = time.gmtime(time.time())
        return time.mktime((ds.tm_year, ds.tm_mon, ds.tm_mday, 0, 0, 0, ds.tm_wday, ds.tm_yday, ds.tm_isdst))
