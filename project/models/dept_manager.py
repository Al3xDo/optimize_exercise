from sqlalchemy import CHAR, Column, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from project.extensions import db


class DeptManager(db.Model):
    __tablename__ = 'dept_manager'

    emp_no = Column(ForeignKey('employees.emp_no', ondelete='CASCADE'), primary_key=True, nullable=False)
    dept_no = Column(ForeignKey('departments.dept_no', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
    from_date = Column(Date, nullable=False)
    to_date = Column(Date, nullable=False)

    department = relationship('Department')
    employee = relationship('Employee')