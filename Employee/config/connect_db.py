from sqlalchemy import create_engine, text


# Define your PostgreSQL connection string

def execute_query(user_name, password):
    DATABASE_URL = 'postgresql://postgres:admin@localhost/PythonConnect'

    query = """
        SELECT * FROM "Employees" WHERE "Username" = :username AND "Password" = :password;
    """
    params = {
        'username': user_name,
        'password': password
    }

    engine = create_engine(DATABASE_URL)

    # Obtain a connection from the engine
    with engine.connect() as connection:
        result = connection.execute(text(query), params)
        # Convert result rows to dictionaries
        rows = [dict(zip(result.keys(), row)) for row in result]
        if len(rows) == 0:
            return "Login Failed"
        return rows

# Define your query and parameters
