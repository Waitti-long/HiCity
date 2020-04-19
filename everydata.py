import requests
from HiCityData import Parser, Reader, SQL, MetaPrinter, Progressbar

if __name__ == '__main__':
    """
    每天执行一遍，确定数据库已经读入
    """
    sql = SQL("city.db")
    bar = Progressbar(MetaPrinter)
    reader = Reader(bar)
    parser = Parser(bar)
    city_map = parser.parse(reader.read_from_db(sql))
    for i in city_map:
        requests.get("localhost/" + city_map[i][0])
