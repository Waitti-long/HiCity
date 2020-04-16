from .entity import Base, City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


class SQL:
    """
    SQL
    """

    def __init__(self, db_name: str):
        self.__session = None
        self.connect(db_name)

    def connect(self, db_name: str):
        engine = create_engine("sqlite:///" + db_name)
        Base.metadata.create_all(engine, checkfirst=True)
        self.__session = sessionmaker(bind=engine)

    def session(self):
        """
        获取会话
        会话结束后记得调用session.close()关闭会话
        """
        return self.__session()

    def sql_add(self, cities: [City]):
        """
        增
        """
        sen = self.session()
        sen.add_all(cities)
        sen.commit()
        sen.close()

    def sql_query(self):
        """
        查
        """
        sen = self.session()
        cities = sen.query(City).all()
        res = []
        for city in cities:
            res.append(city)
        sen.close()
        return res

    def sql_delete(self, a_city: City):
        """
        删
        """
        sen = self.session()
        sen.delete(a_city)
        sen.commit()
        sen.close()

    def sql_update(self, a_city: City, new_city: City):
        """
        改
        """
        sen = self.session()
        old_city = sen.query.filter(City.code == a_city.code).filter(City.name == a_city.name).query()
        old_city.name = new_city.name
        old_city.code = new_city.code
        sen.commit()
        sen.close()
