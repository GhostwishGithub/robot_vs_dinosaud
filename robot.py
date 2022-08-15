import random
class Robot:
    def __init__(self, name, health, active_weapon):
        self.name = name
        self.health = health
        self.active_weapon = self.choose_your_weapon()

    def attack(self, dinosaur):
        dinosaur.health = dinosaur.health - self.active_weapon

    def choose_your_weapon(self):
        user_choice = input('''
        Allright, pick the robot's weapon via the corresponding number
        1. Fists of Steel
        2. Sword of Justice
        3. Blastatron 9000
        4. Tire Iron
        
        What's it gonna be? :''')
        if user_choice == '1':
            return random.randrange(9, 16)
        elif user_choice == '2':
            return random.randrange(15, 22)
        elif user_choice == '3':
            return random.randrange(21, 28)
        elif user_choice == '4':
            return 9001
        else:
            print("Try again.")
            return self.choose_your_weapon()