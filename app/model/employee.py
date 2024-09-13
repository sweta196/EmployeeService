from datetime import datetime

from app.factory.db_factory import db


class Employee(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    phone_number = db.Column(db.String(20))
    hire_date = db.Column(db.Date, default=datetime.utcnow)
    department = db.Column(db.String(100))
    position = db.Column(db.String(100))
    salary = db.Column(db.Float)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone_number': self.phone_number,
            'hire_date': self.hire_date.strftime('%Y-%m-%d') if self.hire_date else None,
            'department': self.department,
            'position': self.position,
            'salary': self.salary
        }



    def __repr__(self):
        return f'<Employee {self.first_name} {self.last_name}>'
