import random

player_score = 0
computer_score = 0
round_count = 0

def game():
    global player_score, computer_score, round_count

    print("Welcome to Rock, Paper, Scissors!")
    print("Enter 'rock', 'paper', or 'scissors' to play.")

    valid_choices = ['rock', 'paper', 'scissors']
    user_choice = input("Enter your choice: ")
    user_choice = user_choice.lower()

    while user_choice not in valid_choices:
        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
        user_choice = input("Enter your choice: ")
        if user_choice in valid_choices:
            break

    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    print(f"Computer chose {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
        player_score += 1
    else:
        print("You lose!")
        computer_score += 1

    round_count += 1

    play_again = input("Do you want to play again? (yes/no): ")
    play_again = play_again.lower()

    while play_again not in ['yes', 'no']:
        print("Invalid input. Please enter 'yes' or 'no'.")
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again in ['yes', 'no']:
            break

    if play_again == 'yes':
        game()
    else:
        print(f"Player {player_score} - {computer_score} Computer")
        print(f"Rounds played: {round_count}")
        print("Thanks for playing!")

if __name__ == "__main__":
    game()
