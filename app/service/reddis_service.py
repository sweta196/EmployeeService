from app.config.reddis_client import init_redis
from app.model.employee import Employee
from app.exception.employee_not_found import EmployeeNotFoundException
from app.repository.employee_repository import EmployeeRepository

redis_client = init_redis()
employee_repository = EmployeeRepository()


class ReddisService:

    def get_employee_from_cache(self, employee_id):
        employee = redis_client.hgetall(f"employee:{employee_id}")
        if employee:
            return {
                "id": int(employee['id']),
                "username": employee['username'],
                "department": employee['department'],
                "salary": float(employee['salary'])
            }
        return None

    def get_employee_from_db(self, employee_id):
        employee = Employee.query.get(employee_id)
        if employee:
            employee_dict = employee.to_dict()

            # Check for None values and handle them
            employee_dict = {k: v for k, v in employee_dict.items() if v is not None}
            print(employee_dict)

            # if len(employee_dict) != len(employee.to_dict()):
            #     print(f"Missing fields for employee {employee_id}, skipping Redis cache")

            redis_client.hmset(f"employee:{employee_id}", employee_dict)
            return employee_dict

    def get_employee(self, employee_id):
        employee = self.get_employee_from_cache(employee_id)
        if employee is not None:
            return employee
        return self.get_employee_from_db(employee_id)

    def get_employee_email_cache(self, employee_id):
        email = redis_client.get(f"employee:{employee_id}:email")
        if email:
            return {"email": email}
        return None

    def set_employee_email_cache(self, employee_id, email):
        redis_client.set(f"employee:{employee_id}:email", email)
