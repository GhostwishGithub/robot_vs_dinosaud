class Robot:
    def __init__(self, name, health, active_weapon):
        self.name = name
        self.health = health
        self.active_weapon = active_weapon

    def attack(self, dinosaur):
        dinosaur.health = dinosaur.health - self.active_weapon