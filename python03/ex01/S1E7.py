from S1E9 import Character

class Baratheon(Character):
    def __init__(self, first_name, is_alive = True):
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'
    def die(self):
        self.is_alive = False
    

class Lannister(Character):
    def __init__(self, first_name, is_alive = True):
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'
    def die(self):
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive = True):
        return(cls(first_name, is_alive))
