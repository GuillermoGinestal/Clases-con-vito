class Dea:
    def __init__(self, x, y, dea_id):
        self.x = x
        self.y = y
        self.dea_id = dea_id
    
    def get_distancia(self, user_x , user_y):
        c_1 = abs(user_x) + abs(self.x)**2
        c_2 = abs(user_y) + abs(self.y)**2
        return (c_1 + c_2)**0.5

class User:
    def __init__(self, name,x,y):
        self.name = name
        self.x = x
        self.y = y
