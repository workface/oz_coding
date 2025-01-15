class Eagle :
    def __init__(self, name, food):
        self.name = name
        self.food = food
    def get_info(self):
        return f'{self.name}는 {self.food}를 먹는 독수리 입니다'