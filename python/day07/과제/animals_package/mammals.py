class Dog :
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def get_info(self):
        return f'{self.name}는 {self.breed}품종의 개 입니다'