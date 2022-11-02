from create_table import *

class Users():

    def __init__(self, email, password, first_name, last_name, address):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def _generate_dict(self):
        return {
            'email': self.email,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'address': self.address
        }


    def save(self):
        try:
            connection = create_db_connection(**self.con_string)
            connection.begin()
            with connection.cursor() as cursor:
                execute_query = """INSERT INTO users
                   (email, password, first_name, last_name, addresss)
                   VALUES (%s, %s, %s, %s, %s)"""
                cursor.execute(execute_query)
        finally:
            self.cursor.execute()
