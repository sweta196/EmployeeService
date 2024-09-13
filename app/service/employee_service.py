from sqlalchemy import text
import logging
from app.config.connect_db import connect_db
from app.exception.employee_not_found import EmployeeNotFoundException
from app.repository.employee_repository import EmployeeRepository
from app.schema.schema import EmployeeSchema
from app.service.reddis_service import ReddisService

employee_repository = EmployeeRepository()
redis_service = ReddisService()


class Employee_Service:

    def __init__(self):
        pass

    def add_employee(self, data):
        try:
            employee_schema = EmployeeSchema()
            employee = employee_schema.load(data)
            employee_repository.save(employee)
            return "Success"
        except Exception as e:
            raise e

    def update_employee(self, user_name, department, email, phone):
        query = """
               UPDATE Public."Employees"
               SET "Department" = :department,
                   "Email" = :email,
                   "Phone Number" = :phone
               WHERE "Username" = :user_name;
           """
        params = {
            'department': department,
            'email': email,
            'phone': phone,
            'user_name': user_name
        }

        engine = connect_db()

        with engine.connect() as connection:
            transaction = connection.begin()
            try:
                connection.execute(text(query), params)
                transaction.commit()
                return f"record updated successfully for {user_name}"
            except Exception as e:
                transaction.rollback()
                logging.error(f"Error inserting user details: {e}")
                return {"error": str(e)}

    def get_employee(self, emp_id):
        try:
            return employee_repository.get_by_id(emp_id)
        except Exception as e:
            raise e

    def authenticate_employee(self, user_name, password):
        try:
            employee = employee_repository.get_by_username(user_name)
            print(employee.password)
            if employee.password == password:
                return True
        except Exception as e:
            raise e

    def delete_employee(self, emp_id):
        try:
            employee_repository.delete(emp_id)
            return f"Successfully deleted {emp_id} from database"
        except EmployeeNotFoundException as e:
            raise e
        except Exception as e:
            raise e

    def update_employee_password(self, username, password):
        try:
            EmployeeRepository.update_password(username, password)
            return f"Successfully updated password for {username}"
        except EmployeeNotFoundException as e:
            raise e

    def update_employee_email(self, employee_id, email):
        employee = employee_repository.update_email(employee_id, email)
        if employee:
            # Update the cache
            self.redis_service.set_employee_cache(employee_id, email)
            return employee.to_dict()
        else:
            return None

    def get_employee_details(self, employee_id):
        employee_cache = redis_service.get_employee_cache(employee_id)
        if employee_cache:
            return employee_cache

        employee = employee_repository.get_employee_by_id(emp_id)
        if employee:
            redis_service.set_employee_cache(employee.id, employee.email)
            return employee.to_dict()

        return None
