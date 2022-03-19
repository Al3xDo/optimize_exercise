from sqlalchemy import CHAR, Column, Date, Enum, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from project.extensions import db


class Employee(db.Model):
    __tablename__ = 'employees'

    emp_no = Column(Integer, primary_key=True)
    birth_date = Column(Date, nullable=False)
    first_name = Column(String(14), nullable=False)
    last_name = Column(String(16), nullable=False)
    gender = Column(Enum('M', 'F'), nullable=False)
    hire_date = Column(Date, nullable=False)
    
    @staticmethod
    def get(id: int):
        """Get db entity that match the id"""
        return Employee.query.get(id)
    @staticmethod
    def get_all():
        return Employee