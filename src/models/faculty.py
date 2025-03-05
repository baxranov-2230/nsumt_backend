from sqlalchemy import Column, Integer, String


from src.base.db import Base


class Faculty(Base):
    __tablename__ = 'faculties'

    id = Column(Integer, primary_key=True)
    name_uz=Column(String, nullable=False)
    name_ru=Column(String, nullable=False)
    name_en=Column(String, nullable=False)
    faculty_icon=Column(String, nullable=True)

