from dinosaur import Dinosaur
from robot import Robot
import random

class Battlefield:
    def __init__(self):
        health = random.randrange(99, 151)
        attack = random.randrange(9, 16)
        self.robot = Robot('Dinosaur Killer 9000', random.randrange(99, 151), 1)
        self.dinosaur = Dinosaur('Roarface', random.randrange(99, 151), random.randrange(9, 28))
        self.winner = 'JJ'

    def run_game(self):
        print("Allright folks! Get your goofiest music on because we're battling robots and dinosaurs!")
        print(f"In this corner we have {self.robot.name} with health of {self.robot.health} and an attack power of {self.robot.active_weapon}!")
        print(f"And in this corner we have {self.dinosaur.name} with a health of {self.dinosaur.health} and an attack power of {self.dinosaur.attack_power}")
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.battle_phase()
        if self.robot.health <= 0 and self.dinosaur.health > 0:
            self.winner = self.dinosaur.name
        elif self.robot.health > 0 and self.dinosaur.health <= 0:
            self.winner = self.robot.name
        else:
            print("Holy crap they knocked each other out!")
        self.display_winner()

    def battle_phase(self):
        self.robot.attack(self.dinosaur)
        self.dinosaur.attack(self.robot)

    def display_winner(self):
        print(f"And the winner is: {self.winner}!")