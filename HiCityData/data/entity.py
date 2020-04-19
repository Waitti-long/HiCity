from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    __tablename__ = "city"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    code = Column(String, unique=True)

    def __repr__(self) -> str:
        return super(City, self).__repr__()


class Forecast(Base):
    __tablename__ = "forecast"
    # id为citycode和时间戳的拼接
    id = Column(String, primary_key=True)
    code = Column(String)
    date = Column(Float)
    data = Column(String)

    def __repr__(self) -> str:
        return super(Forecast, self).__repr__()
