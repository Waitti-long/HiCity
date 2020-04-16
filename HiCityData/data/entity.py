from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class City(Base):
    __tablename__ = "city"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    code = Column(String, unique=True)

    def __repr__(self) -> str:
        return super().__repr__()
