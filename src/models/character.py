class Character:
    def __init__(self, name, age):
        self.name = name.capitalize()
        self.age = age
        self.health = 200
        self.max_health = 200
        self.inventory = []
        self.hunger = 100
        self.attack_power = 15
        self.defense = 5
        self.weapon = None
        self.armor = None

    def attack(self, target):
        damage = self.attack_power
        if self.weapon:
            damage += self.weapon.damage
        target.take_damage(damage)
        return print(f"{self.name} attacks {target.type} for {damage} damage!")

    def take_damage(self, damage):
        damage -= self.defense
        if damage < 0:
            damage = 0
        self.health -= damage
        if self.health < 0:
            self.health = 0
        return print(f"{self.name} takes {damage} damage! Health is now {self.health}/{self.max_health}.")

    def eat(self, food):
        if food in self.inventory:
            self.hunger += food.nutrition
            if self.hunger > 100:
                self.hunger = 100
            self.inventory.remove(food)
            return print(f"{self.name} eats {food.name}. Hunger is now {self.hunger}/100.")
        else:
            return print(f"{food.name} is not in inventory.")

    def lose_hunger(self, amount):
        self.hunger -= amount
        if self.hunger < 0:
            self.hunger = 0
        return print(f"{self.name} loses {amount} hunger. Hunger is now {self.hunger}/100.")