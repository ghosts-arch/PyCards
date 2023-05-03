from sqlalchemy import Column, Integer, String
from .base import Base


class Card(Base):
    __tablename__ = "card"
    id = Column(Integer, autoincrement=True, primary_key=True)
    question = Column(String(255), nullable=False)
    answer = Column(String(255), nullable=False)
