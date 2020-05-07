if __name__ == '__main__':
    from gevent import monkey

    monkey.patch_all()
    from HiCityServer import app, ForeCastCache
    from HiCityData import SQL

    sql = SQL("city.db")
    ForeCastCache.read(sql)
    from gevent.pywsgi import WSGIServer

    print("server start in:", "http://127.0.0.1:8080")
    WSGIServer(("127.0.0.1", 8080), app).serve_forever()
