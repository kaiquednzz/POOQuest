from models.character import Character

def show_main_menu():
    print("""
        ╔══════════════════════════════════════════════╗
        ║                                              ║
        ║                  POOQUEST                    ║
        ║                                              ║
        ╠══════════════════════════════════════════════╣
        ║                                              ║
        ║       [1]  Create Character                  ║
        ║       [2]  Load Game                         ║
        ║       [3]  Exit                              ║
        ║                                              ║
        ╚══════════════════════════════════════════════╝
        """)

    while True:
        user_choice = input("Enter your choice: ")

        if user_choice not in ["1", "2", "3"]:
            print("Invalid choice. Please try again.")
            continue
        break
        
    
    return user_choice

def create_character():
    counter = 0
    while True:
        name = input("Enter your character's name: ").strip().capitalize()
        if not name:
            print("Name cannot be empty. Please try again.")
            counter += 1
            if counter >= 3:
                print("Too many attempts. Returning to main menu.")
                return None
            continue

        age = int(input("Enter your character's age: "))
        if age < 0:
            print("Age cannot be negative. Please try again.")
            counter += 1
            if counter >= 3:
                print("Too many attempts. Returning to main menu.")
                return None
            continue
        break

    character = Character(name, age)
    print(f"Character {character.name} created!")
    return character


def show_game_menu():
    print("""
        ╔══════════════════════════════════════════════╗
        ║                                              ║
        ║                  POOQUEST                    ║
        ║                                              ║
        ╠══════════════════════════════════════════════╣
        ║                                              ║
        ║       [1]  Character                         ║
        ║       [2]  Explore                           ║
        ║       [3]  Inventory                         ║
        ║       [4]  Save Game                         ║
        ║       [5]  Exit                              ║
        ║                                              ║
        ╚══════════════════════════════════════════════╝
        """)

    while True:
        user_choice = input("Enter your choice: ")

        if user_choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice. Please try again.")
            continue
        break

    return user_choice