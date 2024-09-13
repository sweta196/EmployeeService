from app.exception.employee_not_found import EmployeeNotFoundException
from app.factory.db_factory import db
from app.model.employee import Employee


class EmployeeRepository:

    def get_by_username(self, username):
        try:
            employee = Employee.query.filter_by(username=username).first()
            if employee:
                return employee
        except EmployeeNotFoundException as e:
            raise e

    def get_by_id(self, emp_id):
        try:
            employee = Employee.query.filter_by(id=emp_id).first()
            if employee:
                return employee
        except EmployeeNotFoundException as e:
            raise e
        except Exception as e:
            raise e

    def save(self, employee):
        try:
            db.session.add(employee)
            db.session.commit()
        except Exception as e:
            raise e

    def delete(self, emp_id):
        try:
            employee = self.get_by_id(emp_id)
            if employee:
                db.session.delete(employee)
                db.session.commit()
            else:
                raise ValueError(f"Employee with username '{emp_id}' not found")
        except Exception as e:
            raise e

    def update_password(self, username, new_password):
        try:
            employee = self.get_by_username(username)
            if employee:
                employee.password = new_password
                db.session.commit()
            else:
                raise EmployeeNotFoundException(username)
        except Exception as e:
            raise e

    def update_email(self, employee_id, new_email):
        try:
            employee = self.get_by_id(employee_id)
            if employee:
                employee.email = new_email
                db.session.commit()
            else:
                raise EmployeeNotFoundException(employee_id)
        except Exception as e:
            print(e)
