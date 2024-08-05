from flask import Flask, request, jsonify

from Employee.config.connect_db import execute_query
from Employee.service.update_user import update_user

app = Flask(__name__)


@app.route("/welcome", methods=["GET"])
def welcome():
    return "Hi , welcome to Employee application"


@app.route("/validate-user/<user_name>/<password>", methods=["GET"])
def validate_user(user_name, password):
    return execute_query(user_name, password)


@app.route('/update_employee/<user_name>', methods=['PUT'])
def update_employee(user_name):
    data = request.json
    department = data.get('department')
    email = data.get('email')
    phone = data.get('phone')
    result = update_user(user_name, department, email, phone)

    if "error" in result:
        return "Error occurred while updating record!"
    else:
        return jsonify({"message": result})


if __name__ == '__main__':
    app.run(debug=True)
