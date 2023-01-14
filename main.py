import random

class Player:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
        self.gold = 0
        self.level = 1
        self.exp = 0
        
    def attack(self, enemy):
        damage = self.power
        enemy.health -= damage
        print(f'{self.name} наносит {damage} урона {enemy.name}')
        if enemy.health <= 0:
            print(f'{enemy.name} погибает')
    def level_up(self):
        self.level += 1
        self.power += 10
        print(f'{self.name} повышает уровень до {self.level}!')

def gain_exp(player, exp):
    player.exp += exp
    if player.exp >= 100:
        player.exp -= 100
        player.level_up()

player = Player("Игрок", 100, 20)

while True:
    print("1. Идти в путь")
    print("2. Проверить состояние")
    choice = input("Ваш ход: ")
    if choice == "1":
        exp = random.randint(10, 20)
        print(f'Вы получаете {exp} опыта')
        gain_exp(player, exp)
    elif choice == "2":
        print(f'Здоровье: {player.health}, Золото: {player.gold}, Уровень: {player.level}, Опыт: {player.exp}')
    else:
        print("Неверный выбор")
