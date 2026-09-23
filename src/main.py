from models.character import Character
from menus.menu import show_main_menu, show_game_menu, create_character, show_character_menu
from utils import confirm_exit
from systems.exploration import explore

user_choice = show_main_menu()

if user_choice == "1":
    character = create_character()
    if character is None:
        user_choice = show_main_menu()

    else: #character created successfully
        while True:
            user_choice = show_game_menu()
            if user_choice == 1:
                show_character_menu(character)

            elif user_choice == 2:
                explore(character)

            elif user_choice == 5:
                if confirm_exit():
                    break

elif user_choice == "2":
    print("Load game functionality is not implemented yet.")
    user_choice = show_main_menu()
    
elif user_choice == "3":
    if confirm_exit():
        print("Exiting the game.")

    else:
        user_choice = show_main_menu()