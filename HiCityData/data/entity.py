from sqlalchemy import Column, String, Integer
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
    id = Column(String, primary_key=True)
    city = Column(String)
    date = Column(Integer)
    data = Column(String)

    def __repr__(self) -> str:
        return super(Forecast, self).__repr__()
