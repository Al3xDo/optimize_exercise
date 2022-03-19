# project/api/v1/users.py

from ast import arg
from flask import Blueprint, request
from flask_sqlalchemy import Pagination
from project.models.employees import Employee


employees_blueprint = Blueprint('employees', __name__)

@employees_blueprint.route('/employee/<emp_id>', methods=['GET'])
def get_employee_by_id(emp_id: int):
    creator = Employee.get(emp_id)
    return {
        "emp_no" : creator.emp_no,
        "birth_date" : creator.birth_date,
        "first_name" : creator.first_name,
        "last_name" : creator.last_name,
        "gender" : creator.gender,
        "hire_date" : creator.hire_date
    }
@employees_blueprint.route('/employee', methods=['GET'])
def get_employees():
    args = request.args.to_dict()
    page= int(args.get('page'))
    employees_query = Employee.query.paginate(page=page, error_out=False, max_per_page=15)
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