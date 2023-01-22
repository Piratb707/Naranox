import random

# Класс квестов
class Quest:
    def __init__(self, name, description, reward, completion_condition):
        self.name = name
        self.description = description
        self.reward = reward
        self.completion_condition = completion_condition

    def check_completion(self, player):
        return self.completion_condition(player)

# Класс персонажа
class Character:
    def __init__(self, name, level=1, hp=100, strength=10, agility=10, intelligence=10):
        self.name = name
        self.level = level
        self.hp = hp
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.xp = 0
        self.next_level_xp = 100
        self.inventory = {}
        self.quests = []

    # Повышение уровня 
    def level_up(self):
        self.level += 1
        self.hp += 10
        self.strength += 2
        self.agility += 2
        self.intelligence += 2
        self.next_level_xp *= 1.5
        print(f"{self.name} повысил свой уровень до {self.level}!")
    
    # Получение опыта
    def gain_xp(self, xp):
        self.xp += xp
        if self.xp >= self.next_level_xp:
            self.level_up()
            self.xp = 0
        else:
            print(f"{self.name} получено {xp} опыта. {self.next_level_xp - self.xp} Осталось опыта до следующего уровня.")

    # Получение повреждений 
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name} был побежден.")
        else:
            print(f"{self.name} получил {damage} единиц урона. {self.hp} Осталось здоровья.")

    # Функция атаки
    def attack(self, enemy):
        damage = self.strength // 2
        enemy.take_damage(damage)
        print(f"{self.name} атакован {enemy.name} на {damage} единиц урона.")

    # Функция получения квеста
    def accept_quest(self, quest):
        self.quests.append(quest)
        print(f"{self.name} принял задание {quest.name}")
        print(quest.description)

    # Функция проверки задания  
    def check_quests(self):
        for quest in self.quests:
            if quest.check_completion(self):
                print(f"{self.name} завершил задание {quest.name}")
                print(f"{self.name} получил {quest.reward}")
                self.quests.remove(quest)
    
    # Функция характеристик персонажа
    def stats(self):
        print(f"Имя: {self.name}")
        print(f"Уровень: {self.level}")
        print(f"Здоровье: {self.hp}")
        print(f"Сила: {self.strength}")
        print(f"Ловкость: {self.agility}")
        print(f"Интелект: {self.intelligence}")
        print(f"Опыт: {self.xp} / {self.next_level_xp}")
        print("Инвентарь: ", self.inventory)

# Функция создания персонажа (без класса)
def create_character():
    name = input("Как зовут вашего персонажа ")
    return Character(name)

# Пример квеста
def has_sword(player):
    return "меч" in player.inventory

sword_quest = Quest("Верни мой меч", "Верни мой меч , который украли гоблины.", 50, has_sword)

player = create_character()
player.stats()

# Пример геймплея 
enemy = Character("Гоблин", level=1, hp=50, strength=5, agility=5, intelligence=5)
print("Впереди гоблин!")

while enemy.hp > 0:
    player.attack(enemy)
    enemy.attack(player)
    player.stats()
    enemy.stats()

# Пример работы системы персонажа 
player.gain_xp(50)
print("Гоблин выронил меч , вы его подобрали.")
player.inventory["меч"] = "Ржавый меч"
player.stats()

# Пример квеста
player.accept_quest(sword_quest)
player.check_quests()