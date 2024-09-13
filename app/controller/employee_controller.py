import time
from flask import request, jsonify, Blueprint, make_response
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, create_refresh_token
from app.exception.employee_not_found import EmployeeNotFoundException
from app.service.employee_service import Employee_Service
from app.service.reddis_service import ReddisService
from app.exception.LoginFailedException import LoginFailedException

employee_bp = Blueprint('employee', __name__, url_prefix='/employee')

employee_service = Employee_Service()
reddis_service = ReddisService()


@employee_bp.route("/get-employee-details/<user_name>/<password>", methods=["GET"])
def get_employee_details(user_name, password):
    try:
        return employee_service.fetch_employee_details(user_name, password)
    except Exception as e:
        raise e


@employee_bp.route("/create", methods=["POST"])
def create():
    try:
        data = request.get_json()
        return employee_service.add_employee(data)
    except Exception as e:
        raise e


@employee_bp.route("/validate-employee/<user_name>/<password>", methods=["GET"])
def validate_employee(user_name, password):
    try:

        employee = employee_service.authenticate_employee(user_name, password)
        if employee:
            access_token = create_access_token(identity=user_name)
            refresh_token = create_refresh_token(identity=user_name)

        return jsonify(access_token=access_token, refresh_token=refresh_token)
    except LoginFailedException as e:
        raise e("Login Failed", 401)
    except Exception as e:
        response = make_response(jsonify({"error": str(e)}), 500)
        response.headers["X-Custom-Header"] = str(e)
        return response


@employee_bp.route('/update/<employee_name>', methods=['PUT'])
def update(employee_name):
    data = request.json
    department = data.get('department')
    email = data.get('email')
    phone = data.get('phone')
    result = employee_service.update_employee(employee_name, department, email, phone)

    if "error" in result:
        return "Error occurred while updating record!"
    else:
        return {"message": result}


@employee_bp.route("/delete/<emp_id>", methods=["DELETE"])
def delete(emp_id):
    return employee_service.delete_employee(emp_id)


@employee_bp.route("/refresh", methods=["GET"])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    return jsonify(access_token=access_token)


@employee_bp.route("/get/<emp_id>", methods=["GET"])
# @jwt_required()
def get_by_id(emp_id):
    # current_user = get_jwt_identity()
    # print(current_user)
    # if current_user:
    time.sleep(1)
    employee = employee_service.get_employee_details(emp_id)
    if employee:
        return make_response(employee.to_dict(), 200)
    return make_response('Employee not found', 404)
    # return make_response("Authentication failed", 401)


@employee_bp.route("/update-password/<username>", methods=["PATCH"])
def update_employee_password(username):
    try:
        data = request.json
        new_password = data.get('new_password')

        if not new_password:
            return jsonify({'message': 'New password is required'}), 400

        employee_service.update_employee_password(username, new_password)
        return jsonify("Employee updated", "success"), 200
    except EmployeeNotFoundException as e:
        return e.message, 404
    except Exception as e:
        response = make_response(jsonify({"error": str(e)}), 500)
        response.headers["X-Custom-Header"] = str(e)
        return response


@employee_bp.route('/get-information/<int:employee_id>', methods=['GET'])
def fetch_employee(employee_id):
    employee = reddis_service.get_employee(employee_id)
    if employee:
        return jsonify(employee)
    return jsonify({"error": "Employee not found"}), 404


@employee_bp.route('/get-id/<int:employee_id>', methods=['GET'])
def get_employee_data(employee_id):
    employee = employee_service.get_employee_details(employee_id)
    if employee:
        return jsonify(employee), 200
    return jsonify({"error": "Employee not found"}), 404


@employee_bp.route('/update-email/<int:employee_id>', methods=['PATCH'])
def update_employee_email(employee_id):
    try:
        data = request.json
        email = data.get('email')
        if not email:
            return jsonify({'message': 'New email is required'}), 400

        employee_service.update_employee_email(employee_id, email)
        return jsonify("Employee updated", "success"), 200

    except EmployeeNotFoundException as e:
        return e.message, 404
    except Exception as e:
        response = make_response(jsonify({"error": str(e)}), 500)
        return response
