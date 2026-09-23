from random import choice
from models.event import events
from models.enemy import enemies, Enemy
from menus.menu import show_enemy_info
from systems.combat import start_combat

def explore(character):
    event = choice(events)
    print(f"{event.name}: {event.description}")
    if event.type == "enemy":
        enemy = choice(enemies)
        new_enemy = Enemy(enemy["type"], enemy["max_health"], enemy["attack_power"], enemy["defense"])
        show_enemy_info(new_enemy)
        fight = start_combat(character, new_enemy)
        if fight == False:
            return None
            

    elif event.type == "food":
        # Here I would implement food collection logic
        return print("Food collection system is not implemented yet.")
    else:
        print('Nothing happened')