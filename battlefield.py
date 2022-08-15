from dinosaur import Dinosaur
from robot import Robot
import random

class Battlefield:
    def __init__(self, robot, dinosaur, winner):
        robot = Robot('Dinosaur Killer 9000', random.randrange(100, 150), random.randrange(10-15))
        dinosaur = Dinosaur('Roarface', random.randrange(100, 150), random.randrange(10-15))
        winner = 'JJ'

    def run_game(self, robot, dinosaur, winner):
        print("Allright folks! Get your goofiest music on because we're battling robots and dinosaurs!")
        print(f"In this corner we have {robot.name} with health of {robot.health} and an attack power of {robot.active_weapon}!")
        print(f"And in this corner we have {dinosaur.name} with a health of {dinosaur.health} and an attack power of {dinosaur.attack_power}")
        while robot.health > 0 and dinosaur.health > 0:
            Battlefield.battle_phase
        if robot.health <= 0:
            winner = dinosaur.name
        else:
            winner = robot.name
        Battlefield.display_winner

    def battle_phase(self, robot, dinosaur):
        robot.attack(dinosaur)
        dinosaur.attack(robot)

    def display_winner(self, winner):
        print(f"And the winner is! {self.winner}!")