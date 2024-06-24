import random

def get_user_choice():
    while True:
        user_input = input("Enter choice (rock, paper, scissors): ").lower()
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        print("Invalid choice. Please choose again.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("\n*********************************")
    print("Welcome to Rock, Paper, Scissors!")
    print("*********************************\n")
    
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}\n")
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
