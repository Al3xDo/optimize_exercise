from sqlalchemy import CHAR, Column, Date, Enum, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from project.extensions import db


class Department(db.Model):
    __tablename__ = 'departments'

    dept_no = Column(CHAR(4), primary_key=True)
    dept_name = Column(String(40), nullable=False, unique=True)