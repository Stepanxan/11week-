from mysql import connector


def create_db_connection(host_name, user_name, user_password, db_name):
    connect = None
    try:
        connect= connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Exception as err:
        print(f"Error: '{err}'")

    return connect
connection = create_db_connection("localhost", "root", "19982804", "testbase")

def database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Exception as err:
        print(f"Error: '{err}'")
try:
    create_database_query = "CREATE DATABASE testbase"
    database(connection, create_database_query)
except Exception as err:
    print(f"Error: '{err}'")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Exception as err:
        print(f"Error: '{err}'")

create_users_table = """
CREATE TABLE users (
    user_id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(20) NOT NULL,
    password VARCHAR(20) NOT NULL,
    first_name TEXT,
    last_name TEXT,
    address VARCHAR(20),
    PRIMARY KEY (users_id)
    );
    """
create_car_table = """
CREATE TABLE car (
    car_id INT NOT NULL AUTO_INCREMENT,
    models TEXT, 
    number INT NOT NULL,
    speed INT NOT NULL,
    user VARCHAR(20),
    graduation INT NOT NULL,
    PRIMARY KEY (car_id)
    );
    """

connection = create_db_connection("localhost", "root", "19982804", "testbase")
execute_query(connection, create_users_table)
execute_query(connection, create_car_table)
