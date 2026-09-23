from menus.menu import show_combat_menu

def start_combat(character, enemy):
    if character.health <= 0:
        print('You are dead!')
        return False

    elif enemy.health <= 0:
        print('The enemy is dead!')
        return False

    else:
        while True:
            if enemy.health > 0:
                choice = show_combat_menu()
                if choice == 1:
                    character.attack(enemy)
                    if enemy.health <= 0:
                        return "victory"

                    enemy.attack(character)
                    if character.health <= 0:
                        return "defeat"