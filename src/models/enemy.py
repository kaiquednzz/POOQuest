class Enemy:
    def __init__(self, type, max_health, attack_power, defense):
        self.type = type
        self.max_health = max_health
        self.health = self.max_health
        self.attack_power = attack_power
        self.defense = defense

    def attack(self, target):
        damage = self.attack_power
        target.take_damage(damage)
        return print(f"{self.type} attacks {target.name} for {damage} damage!")

    def take_damage(self, damage):
        damage -= self.defense
        if damage < 0:
            damage = 0
        self.health -= damage
        if self.health < 0:
            self.health = 0
        return print(f"{self.type} takes {damage} damage! Health is now {self.health}/{self.max_health}.")


enemies = [
    {
        "type": "Zombie",
        "max_health": 100,
        "attack_power": 10,
        "defense": 5
    },
    {
        "type": "Skeleton",
        "max_health": 125,
        "attack_power": 15,
        "defense": 10
    },
    {
        "type": "Spider",
        "max_health": 75,
        "attack_power": 8,
        "defense": 5        
    },
    {
        "type": "Enderman",
        "max_health": 200,
        "attack_power": 25,
        "defense": 15
    }
]