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
                    enemy_action = enemy.enemy_choice()
                    if enemy_action == "defend":
                        enemy.defend()

                    character.attack(enemy)
                    if enemy.health <= 0:
                        return "victory"

                    if enemy_action == "attack":
                        enemy.attack(character)
                        if character.health <= 0:
                            return "defeat"

                    character.defending = False
                    enemy.defending = False

                elif choice == 2:
                    character.defend()
                    if enemy.health <= 0:  # possible future reflection effect
                        return "victory"

                    enemy_action = enemy.enemy_choice()
                    if enemy_action == "attack":
                        enemy.attack(character)
                        if character.health <= 0:
                            return "defeat"

                    elif enemy_action == "defend":
                        enemy.defend()

                    character.defending = False
                    enemy.defending = False