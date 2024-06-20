import random

def get_feedback(secret, guess):
    correct_position = 0
    correct_digit = 0
    secret_count = {}
    guess_count = {}
    
    for s, g in zip(secret, guess):
        if s == g:
            correct_position += 1
        else:
            secret_count[s] = secret_count.get(s, 0) + 1
            guess_count[g] = guess_count.get(g, 0) + 1
            
    for digit in guess_count:
        if digit in secret_count:
            correct_digit += min(secret_count[digit], guess_count[digit])
    
    return correct_position, correct_digit

def play_game(secret):
    attempts = 0
    while True:
        guess = input("Enter your guess: ")
        attempts += 1
        if guess == secret:
            print(f"Correct! You guessed the number in {attempts} tries.")
            return attempts
        correct_position, correct_digit = get_feedback(secret, guess)
        print(f"Correct position: {correct_position}, Correct digit but wrong position: {correct_digit}")

def main():
    num_digits = int(input("Enter the number of digits for the game: "))
    
    # Player 1 sets the number
    print("Player 1, set your number:")
    secret1 = input("Enter the secret number: ")
    
    # Player 2 guesses
    print("Player 2, it's your turn to guess.")
    attempts2 = play_game(secret1)
    
    # Player 2 sets the number
    print("Player 2, set your number:")
    secret2 = input("Enter the secret number: ")
    
    # Player 1 guesses
    print("Player 1, it's your turn to guess.")
    attempts1 = play_game(secret2)
    
    # Determine the winner
    if attempts1 < attempts2:
        print("Player 1 wins and is crowned Mastermind!")
    elif attempts2 < attempts1:
        print("Player 2 wins and is crowned Mastermind!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
