def start_combat(character, enemy):
    if character.health <= 0:
        print('You are dead!')
        return False

    elif enemy.health <= 0:
        print('The enemy is dead!')
        return False

    else:
        while True:
            character.attack(enemy)
            if enemy.health <= 0:
                print('The enemy is dead!')
                return "victory"

            else:
                enemy.attack(character)
                if character.health <= 0:
                    print('You are dead!')
                    return "defeat"