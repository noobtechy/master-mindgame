import random

num = random.randrange(1000, 10000)

def check_guess(num, guess):
    count = 0
    correct = ['X'] * 4
    for i in range(4):
        if num[i] == guess[i]:
            count += 1
            correct[i] = guess[i]
    return count, correct


def play_game():
    print("Welcome to the Number Guessing Game! yhoho  ")
    num_str = str(num)
    attempts = 0
    max_attempts = 5
    
    while attempts < max_attempts:
        guess = input("Guess the 4-digit number: ")
        
        if len(guess) != 4 or not guess.isdigit():
            print("Invalid input. Please enter a 4-digit number.")
            continue

        attempts += 1
        correct_count, correct_digits = check_guess(num_str, guess)

        if correct_count == 4:
            print(f"Congratulations! You guessed the number {num_str} in {attempts} tries! You're a Mastermind!")
            break
        else:
            print(f"Not quite the number. But you did get {correct_count} digit(s) correct!")
            print("Correct digits so far:", ''.join(correct_digits))
            print()

    if attempts == max_attempts:
        print(f"Sorry, you've used all {max_attempts} attempts. You failed to guess the number. The correct number was {num_str}.")

if __name__ == "__main__":
    play_game()