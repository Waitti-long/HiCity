from HiCityData import SQL
from HiCityServer import app, ForeCastCache

if __name__ == '__main__':
    sql = SQL("city.db")
    ForeCastCache.read(sql)
    app.run(port=8080, debug=True)
