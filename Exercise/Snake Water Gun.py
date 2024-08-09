import random


def get_user_choice():
    user_choice = input("Choose Your Option('Snake', 'Water', 'Gun') : ").lower()
    while user_choice not in ['snake', 'water', 'gun']:
        print("Plz Choose A valid Option....")
        user_choice = input("Choose Your Option('Snake', 'Water', 'Gun') : ").lower()
    return user_choice


def winner(user_choice, computer_choice):
    if (computer_choice == user_choice):
        return 'draw'
    elif ((user_choice == 'snake' and computer_choice == 'water')
          or (user_choice == 'gun' and computer_choice == 'snake')
          or (user_choice == 'water' and computer_choice == 'gun')):
        return 'you Win'
    else:
        return 'Computer Win'


def snake_water_gun_game():
    print('<<<<<<<<<<Welcome>>>>>>>>>>>>')
    user_choice = get_user_choice()
    computer_choice = random.choice(['Snake', 'Water', 'Gun']).lower()
    print(f"You chose {user_choice}. Computer chose {computer_choice}.")
    result = winner(user_choice, computer_choice)
    print(result)


if __name__ == '__main__':
    snake_water_gun_game()
