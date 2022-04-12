# project/api/v1/users.py

from ast import arg
from asyncio.log import logger
from time import time
from flask import Blueprint, request
from flask_sqlalchemy import Pagination
from project.models.employees import Employee
from project import cache

employees_blueprint = Blueprint('employees', __name__)

@employees_blueprint.route('/employee/lib', methods=['GET'])
@cache.cached(timeout=50,query_string=True)
def get_employees_lib_paginate():
    args = request.args.to_dict()
    page= int(args.get('page'))
    employees_query = Employee.query.paginate(page=page, error_out=False, max_per_page=20)
    result = dict(data=[{
        "emp_no" : creator.emp_no,
        "birth_date" : creator.birth_date,
        "first_name" : creator.first_name,
        "last_name" : creator.last_name,
        "gender" : creator.gender,
        "hire_date" : creator.hire_date
    } for creator in employees_query.items], 
                   total=employees_query.total, 
                   current_page=employees_query.page,
                   per_page=employees_query.per_page)
    return result
@employees_blueprint.route('/employee/raw', methods=['GET'])
@cache.cached(timeout=50,query_string=True)
def get_employees_raw_paginate():
    args = request.args.to_dict()
    per_page= int(args.get('per_page'))
    last_id= int(args.get('last_id'))
    employees_query = Employee.query.filter(Employee.emp_no>=last_id).order_by(Employee.emp_no).limit(per_page).all()
    result = dict(data=[{
        "emp_no" : creator.emp_no,
        "birth_date" : creator.birth_date,
        "first_name" : creator.first_name,
        "last_name" : creator.last_name,
        "gender" : creator.gender,
        "hire_date" : creator.hire_date
    } for creator in employees_query])
    return result