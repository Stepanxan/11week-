from create_table import database, connection


class Car():

    def __init__(self, models, number, speed, user, graduation):
        self.models = models
        self.number = number
        self.speed = speed
        self.user = user
        self.graduation = graduation

    @staticmethod
    def getdata():
        query_get_all = """SELECT * FROM car;"""
        cursor = connection.cursor()
        cursor.execute(query_get_all)
        response = cursor.fetchall()
        return response

    def save(self):
        try:
            query = f"""INSERT INTO car
                   (models, number, speed, user, graduation)
                   VALUES ('{self.models}', '{self.number}', '{self.speed}', '{self.user}', '{self.graduation}');"""
            database(connection=connection, query=query)
        except Exception as error:
            print(f"Error {error}")