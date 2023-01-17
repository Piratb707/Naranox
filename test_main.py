import unittest
from main import Character

class TestCharacter(unittest.TestCase):
    def test_level_up(self):
        player = Character("John", level=1, hp=100, strength=10, agility=10, intelligence=10)
        player.gain_xp(150)
        self.assertEqual(player.level, 2)
        self.assertEqual(player.hp, 110)
        self.assertEqual(player.strength, 12)
        self.assertEqual(player.agility, 12)
        self.assertEqual(player.intelligence, 12)
        self.assertEqual(player.next_level_xp, 150)
        self.assertEqual(player.xp, 0)

    def test_gain_xp(self):
        player = Character("John", level=1, hp=100, strength=10, agility=10, intelligence=10)
        player.gain_xp(50)
        self.assertEqual(player.xp, 50)
        player.gain_xp(50)
        self.assertEqual(player.xp, 0)
        self.assertEqual(player.level, 2)

    def test_take_damage(self):
        player = Character("John", level=1, hp=100, strength=10, agility=10, intelligence=10)
        player.take_damage(50)
        self.assertEqual(player.hp, 50)
        player.take_damage(60)
        self.assertEqual(player.hp, -10)

    def test_attack(self):
        player = Character("John", level=1, hp=100, strength=10, agility=10, intelligence=10)
        enemy = Character("Enemy", level=1, hp=100, strength=10, agility=10, intelligence=10)
        player.attack(enemy)
        self.assertEqual(enemy.hp, 95)

    def test_stats(self):
        player = Character("John", level=1, hp=100, strength=10, agility=10, intelligence=10)
        player.stats()
        self.assertEqual(player.name, "John")
        self.assertEqual(player.level, 1)
        self.assertEqual(player.hp, 100)
        self.assertEqual(player.strength, 10)
        self.assertEqual(player.agility, 10)
        self.assertEqual(player.intelligence, 10)
        self.assertEqual(player.xp, 0)
        self.assertEqual(player.next_level_xp, 100)
        self.assertEqual(player.inventory, {})

if __name__ == '__main__':
    unittest.main()
