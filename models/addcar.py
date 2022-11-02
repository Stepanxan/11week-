import json


class Car():
    file = "car.json"

    def __init__(self, models, number, speed, user, graduation):
        self.models = models
        self.number = number
        self.speed = speed
        self.user = user
        self.graduation = graduation

    def _generate_dict(self):
        return {
            'models': self.models,
            'number': self.number,
            'speed': self.speed,
            'user': self.user,
            'graduation': self.graduation
        }

    def get_file_data(str, file_name):
        file = open("database/" + file_name, 'r')
        data = json.loads(file.read())
        file.close()
        return data

    def save_to_file(self, data):
        data = json.dumps(data)
        file = open('database/' + self.file, "w")
        file.write(data)
        file.close()

    def save(self):
        car_in_dict_format = self._generate_dict()
        car = self.get_file_data(self.file)
        car.append(car_in_dict_format)
        self.save_to_file(car)


