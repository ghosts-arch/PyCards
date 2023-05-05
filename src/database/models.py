from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Column, Integer, String


class Base(DeclarativeBase):
    pass


class Card(Base):
    __tablename__ = "cards"
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    question: Mapped[str] = mapped_column(String(255), nullable=False)
    answer: Mapped[str] = mapped_column(String(255), nullable=False)
