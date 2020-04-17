from .entity import City


class Parser:
    """
    将数据拼装成字典
    @param progressbar: 简易进度条
    """

    def __init__(self, progressbar):
        self.bar = progressbar

    def parse(self, lines: [str]) -> {}:
        """
        处理数据的每一行
        @return {城市名->[城市代码]}
        """
        city_map = {}
        self.bar.set_target(len(lines))
        self.bar.start()
        for i, line in enumerate(lines):
            line = line[:-1]
            db = line.split(",")
            if len(db) == 2:
                if db[0] not in city_map:
                    city_map[db[0]] = []
                city_map[db[0]].append(db[1])
            self.bar.update(i)
        return city_map


class Reader:
    """
    从文件和数据库中读取数据
    @param progressbar: 简易进度条
    """

    def __init__(self, progressbar):
        self.bar = progressbar

    def read_from_file(self, file: str) -> [str]:
        """
            从文件中读取数据
            @param file: 文件名
            @return 文件的所有行构成的列表
            """
        self.bar.set_target(1)
        self.bar.start()
        with open(file, "r", encoding="utf-8") as f:
            lines = f.readlines()
        self.bar.update(1)
        self.bar.end()
        return lines

    def read_from_db(self, sql) -> [str]:
        """
        从数据库中读取数据
        @param sql: 封装过的数据库对象 <class SQL>
        @return 数据库的所有行构成的列表
        """
        res = []
        sen = sql.session()
        cities = sen.query(City).all()
        self.bar.set_target(len(cities))
        self.bar.start()
        i = 0
        for city in cities:
            res.append(city.name + "," + city.code + "\n")
            i += 1
            self.bar.update(i)
        self.bar.end()
        sen.close()
        return res


class Writer:
    """
    将数据存储到数据库
     @param progressbar: 简易进度条
     @param logger: 实现MetaPrinter的接口 写入过程出现的一些小错误会输出到这里
    """

    def __init__(self, progressbar, logger):
        self.bar = progressbar
        self.printer = logger

    def save_file_to_db(self, city_map, sql):
        """
        将数据储存到数据库
        """
        sen = sql.session()
        self.bar.set_target(len(city_map))
        self.bar.start()
        i = -1
        for city in city_map:
            for code in city_map[city]:
                try:
                    a_city = City(name=city, code=code)
                    sen.add(a_city)
                    sen.commit()
                except Exception:
                    self.printer.write(city, " ", code, "has existed")
            i += 1
            self.bar.update(i)
        sen.close()
