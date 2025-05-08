import random

lottery_games_info = {
    "Power Ball": {"highest": 69, "count": 5},
    "Mega Million": {"highest": 70, "count": 5},
    "Lucky Day Lotto": {"highest": 45, "count": 5},
    "Lotto": {"highest": 52, "count": 6},
}

def generate_lottery_numbers(highest, count):
    """Generates a sorted list of unique random lottery numbers."""
    return sorted(random.sample(range(1, highest + 1), count))

def display_menu():
    """Displays the lottery game menu."""
    print("\nChoose a lottery game:")
    for i, game in enumerate(lottery_games_info.keys()):
        print(f"{i + 1}. {game}")
    print("9. Quit")

def process_selection(choice):
    """Processes the user's menu selection."""
    if choice.isdigit():
        choice_num = int(choice)
        if 1 <= choice_num <= len(lottery_games_info):
            game_name = list(lottery_games_info.keys())[choice_num - 1]
            game_data = lottery_games_info[game_name]
            numbers = generate_lottery_numbers(game_data["highest"], game_data["count"])
            print(f"{game_name}: {', '.join(map(str, numbers))}")
            input("Hit enter key to return to menu")
            run_lottery_program()
        elif choice_num == 9:
            print("Exiting program.")
        else:
            print("Invalid menu selection.")
            run_lottery_program()
    else:
        print("Invalid input. Please enter a number from the menu.")
        run_lottery_program()

def run_lottery_program():
    """Runs the main lottery program."""
    display_menu()
    selection = input("Enter your choice: ")
    process_selection(selection)

if __name__ == "__main__":
    run_lottery_program()
