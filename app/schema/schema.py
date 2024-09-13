from app.factory.marshmallow_factory import ma
from app.model.employee import Employee


class EmployeeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Employee
        load_instance = True
