import random

class Character:
    def __init__(self, name, char_class, health, strength):
        self.name = name
        self.char_class = char_class
        self.health = health
        self.strength = strength
        self.score = 0

    def is_alive(self):
        return self.health > 0

    def attack(self, enemy):
        damage = random.randint(1, self.strength)
        enemy.health -= damage
        return damage

    def gain_health(self, amount):
        self.health += amount
        print(f"You gained {amount} health. Your current health is {self.health}.")

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

def explore(character):
    locations = [
        "a dark forest",
        "an abandoned village",
        "a misty swamp",
        "a sunny meadow",
        "a haunted castle",
        "a snowy mountain pass",
        "a sandy desert",
        "a bustling city market",
        "a serene lakeside",
        "a windy cliffside",
        "a hidden cave",
        "an enchanted garden",
        "a rocky canyon",
        "a dense jungle",
        "an ancient temple",
        "a quiet beach"
    ]

    print(f"{character.name} is exploring...")
    location = random.choice(locations)
    print(f"You have arrived at {location}.")

    if random.random() < 0.5:
        encounter(character)
    else:
        print("The area is peaceful.")

def encounter(character):
    enemies = [
        Enemy("Goblin", 30, 10),
        Enemy("Troll", 50, 15),
        Enemy("Bandit", 40, 12),
        Enemy("Orc", 60, 20),
        Enemy("Dark Mage", 50, 25),
        Enemy("Wolf", 35, 15),
        Enemy("Dragon", 100, 30),
        Enemy("Pikachu", 90, 90),
        Enemy("Herobrine", 100, 30),
        Enemy("Griffin", 100, 30),
        Enemy("Mammoth", 50, 30),
        Enemy("Tiger", 30, 30),
        Enemy("mosquito", 90, 30),
        Enemy("Idiot", 100, 30),
        Enemy("Serial killer", 80, 20),
        Enemy("clown", 100, 10),
        Enemy("noob", 10, 10),
        Enemy("hacker", 10, 70),
    ]

    enemy = random.choice(enemies)
    print(f"A wild {enemy.name} appears!")

    while character.is_alive() and enemy.is_alive():
        action = input("Do you want to (A)ttack or (R)un? ").lower()
        if action == 'a':
            damage = character.attack(enemy)
            print(f"You attacked the {enemy.name} for {damage} damage.")
            if enemy.is_alive():
                enemy_damage = enemy.attack(character)
                print(f"The {enemy.name} attacked you for {enemy_damage} damage.")
            else:
                character.score += 10
                if random.random() < 0.3:  # 30% chance to gain health
                    health_gain = random.randint(5, 15)
                    character.gain_health(health_gain)
        elif action == 'r':
            if random.random() < 0.5:
                print("You managed to escape!")
                return
            else:
                print("You couldn't escape!")
                enemy_damage = enemy.attack(character)
                print(f"The {enemy.name} attacked you for {enemy_damage} damage.")
        else:
            print("Invalid action. Choose again.")

    if character.is_alive():
        print(f"You defeated the {enemy.name}!")
    else:
        print("You have been defeated...")

def main():
    print("Welcome to the Text Adventure Game!")
    print("You are a brave adventurer exploring the world."
      "Your goal is to defeat enemies and gain experience.")
    print("You can choose from 3 classes: Warrior, Mage, and Rogue.")
    print("Each class has different stats and abilities.")
    print("You will have 30% chance to gain more health after defeating an enemy.")
    print("Good luck!")
    character = character_creation()
    while character.is_alive():
        explore(character)
    print(f"Game Over. Your final score is: {character.score}")

if __name__ == "__main__":
    main()
