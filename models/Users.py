from create_table import database, connection

class Users():

    def __init__(self, email, password, first_name, last_name, address):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    @staticmethod
    def getdata():
        query_get_all = """SELECT * FROM users;"""
        cursor = connection.cursor()
        cursor.execute(query_get_all)
        response = cursor.fetchall()
        return response

    def save(self):
        try:
            query = f"""INSERT INTO users
                   (email, password, first_name, last_name, address)
                   VALUES ('{self.email}', '{self.password}', '{self.first_name}', '{self.last_name}', '{self.address}');"""
            database(connection=connection, query=query)
        except Exception as error:
            print(f"Error {error}")
