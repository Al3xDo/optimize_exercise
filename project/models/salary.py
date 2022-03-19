from sqlalchemy import CHAR, Column, Date, Enum, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from project.extensions import db


class Salary(db.Model):
    __tablename__ = 'salaries'

    emp_no = Column(ForeignKey('employees.emp_no', ondelete='CASCADE'), primary_key=True, nullable=False)
    salary = Column(Integer, nullable=False)
    from_date = Column(Date, primary_key=True, nullable=False)
    to_date = Column(Date, nullable=False)

    employee = relationship('Employee')