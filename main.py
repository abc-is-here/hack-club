import random

class Character:
    def __init__(self, name, char_class, health, strength):
        self.name = name
        self.char_class = char_class
        self.health = health
        self.strength = strength

    def is_alive(self):
        return self.health > 0

    def attack(self, enemy):
        damage = random.randint(1, self.strength)
        enemy.health -= damage
        return damage

class Enemy:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def is_alive(self):
        return self.health > 0

    def attack(self, character):
        damage = random.randint(1, self.strength)
        character.health -= damage
        return damage

def character_creation():
    name = input("Enter your character's name: ")
    char_class = input("Choose your class (Warrior/Mage/Rogue): ").capitalize()

    if char_class == "Warrior":
        health = 100
        strength = 15
    elif char_class == "Mage":
        health = 60
        strength = 25
    elif char_class == "Rogue":
        health = 80
        strength = 20
    else:
        print("Invalid class! Defaulting to Warrior.")
        health = 100
        strength = 15
        char_class = "Warrior"

    return Character(name, char_class, health, strength)
