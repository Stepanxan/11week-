from models.addcar import Car
from models.Users import Users
from create_table import *
import json

class Controller():
    file = 'users.json'

    def add_run(self):
        while True:
            print("1. Add New Users\n"
                  + "2. Get All Users\n"
                  + "3. Get All Car\n"
                  + "4. Search\n"
                  + "5. Update User By Id\n"
                  + "6. Add CAR\n"
                  + "7. Conection database"
                  )
            choose = int(input("Type your choose: "))
            self.controller(menu_flag=choose)

    def controller(self, menu_flag):
        if menu_flag == 1:
            self.user_add()
        if menu_flag == 2:
            self.get_all_users()
        if menu_flag == 3:
            self.get_all_car()
        if menu_flag == 4:
            what_to_search = input('By Which Parametr you want to search: ')
            search_str = input('Search: ')
            self.search_by(search_str, what_to_search)
        if menu_flag == 5:
            self.update_user()
        if menu_flag == 6:
            self.add_car()
        if menu_flag == 7:
            host_name = input('Enter host: ')
            user_name = input('Enter user name: ')
            user_password = input('Enter password: ')
            db_name = input('Enter database name: ')
            create_db_connection(host_name, user_name, user_password, db_name)


    @classmethod
    def user_add(self):
        email = str(input("email: "))
        password = input("password: ")
        first_name = str(input("first_name: "))
        last_name = str(input("last_name: "))
        address = str(input("address: "))
        users = Users(email, password, first_name, last_name, address)
        users.save()


    @classmethod
    def get_all_users(cls):
        response = Users.getdata()
        print(response)

    @classmethod
    def get_all_car(cls):
        response = Car.getdata()
        print(response)

    @classmethod
    def search_by(search_str, what_to_search):
        with open('database/users.json', 'r') as file:
            users = json.loads(file.read())
            for user in users:
                if str(user[what_to_search]).lower() == str(search_str).lower():
                    print("Email #" + str(user['email']))
                    print("Password: " + user['password'])
                    print("First_name: " + user['first_name'])
                    print("Last_name: " + user['last_name'])
                    print("Address: " + user['address'])

    @classmethod
    def update_user(cls):
        file = open('database/users.json', 'r')
        users = json.loads(file.read())
        file.close()
        email = input("Email: ")
        password = input("Password: ")
        first_name = input("First_name: ")
        last_name = input("Last_name: ")
        address = input("Address: ")
        for user in users:
            if user['email'] == email:
                user['password'] = password
                user['first_name'] = first_name
                user['last_name'] = last_name
                user['address'] = address
    @classmethod
    def add_car(self):
        models = str(input("models: "))
        number = str(input("number: "))
        speed = input("speed: ")
        user = str(input("user: "))
        graduation = str(input("graduation: "))
        car = Car(models, number, speed, user, graduation)
        car.save()


