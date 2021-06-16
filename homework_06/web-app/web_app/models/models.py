from sqlalchemy import Column, Integer, String

from .database import db


class Users(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
