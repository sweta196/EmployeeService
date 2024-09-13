from flask import Flask, Blueprint

app = Flask(__name__)

welcome_bp = Blueprint('welcome', __name__, url_prefix='/welcome')


@welcome_bp.route("/welcome", methods=["GET"])
def welcome():
    return "Hi , welcome to app application"


@welcome_bp.route("/healthcheck", methods=["GET"])
def health_check():
    return "Up"

