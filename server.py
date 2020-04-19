from HiCityServer import app, ForeCastCache
from HiCityData import SQL

if __name__ == '__main__':
    sql = SQL("city.db")
    ForeCastCache.read(sql)
    app.run(port=8080)
