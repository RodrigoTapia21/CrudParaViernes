from sqlalchemy import Column, Integer, String
from database.db import Base


class ProductBase(Base):
    __tablename__= "product"
    id = Column(Integer, Primary_key=True)
    name = Column(String)
    detail = Column(String)
    price = Column(Integer)
    tags = Column(String)