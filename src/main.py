from models.character import Character
from menus.menu import show_main_menu, show_game_menu, create_character

user_choice = show_main_menu()

if user_choice == "1":
    character = create_character()
    if character is None:
        user_choice = show_main_menu()

    else:
        while True:
            user_choice = show_game_menu()
            if user_choice == "5":
                print("Exiting the game.")
                break

elif user_choice == "2":
    print("Load Game feature is not implemented yet.")
elif user_choice == "3":
    print("Exiting the game.")