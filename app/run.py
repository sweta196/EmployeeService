from app.controller.employee_controller import employee_bp
from app.controller.welcome import welcome_bp
from app.factory.app_factory import create_app
# from app.controller.kafka_controller import kafka_bp

app = create_app()

app.register_blueprint(employee_bp)
app.register_blueprint(welcome_bp)
# app.register_blueprint(kafka_bp)

if __name__ == '__main__':
    # port = app.config['PORT']
    # debug = app.config['DEBUG']
    app.run(debug=True)
