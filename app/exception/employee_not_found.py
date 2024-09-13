class EmployeeNotFoundException(Exception):
    def __init__(self, username):
        self.username = username
        self.message = f"Employee with username {username} not found."
        super().__init__(self.message)
