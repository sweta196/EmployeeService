from sqlalchemy import create_engine, text
import logging


def update_user(user_name, department, email, phone):
    DATABASE_URL = 'postgresql://postgres:admin@localhost/PythonConnect'
    query = """
           UPDATE Public."Employees"
           SET "Department" = :department,
               "Email" = :email,
               "Phone Number" = :phone
           WHERE "Username" = :user_name;
       """
    params = {
        'department': department,
        'email': email,
        'phone': phone,
        'user_name': user_name
    }

    engine = create_engine(DATABASE_URL)

    print(query)

    with engine.connect() as connection:
        transaction = connection.begin()
        try:
            connection.execute(text(query), params)
            transaction.commit()
            return f"record updated successfully for {user_name}"
        except Exception as e:
            transaction.rollback()
            logging.error(f"Error inserting user details: {e}")
            return {"error": str(e)}


#Inline test
# if __name__ == '__main__':
#     # Test data
#     user_name = 'jdoe'
#     department = 'Commerce'
#     email = 'johndoe@example.com'
#     phone = '555-1234'
#
#     # Call the function
#     result = update_user(user_name, department, email, phone)
#
#     # Print the result
#     print(result)
