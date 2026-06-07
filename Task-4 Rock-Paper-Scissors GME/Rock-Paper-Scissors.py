import random

print("===== Rock Paper Scissors Game =====")

user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

while True:

    print("\nChoose one:")
    print("Rock")
    print("Paper")
    print("Scissors")

    user_choice = input("Enter your choice: ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please select Rock, Paper, or Scissors.")
        continue

    computer_choice = random.choice(choices)

    print("\nYour Choice:", user_choice.capitalize())
    print("Computer Choice:", computer_choice.capitalize())

    # Winner Logic
    if user_choice == computer_choice:
        print("Result: It's a Tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("Result: You Win!")
        user_score += 1

    else:
        print("Result: Computer Wins!")
        computer_score += 1

    # Score Board
    print("\n===== Score Board =====")
    print("Your Score:", user_score)
    print("Computer Score:", computer_score)

    # Play Again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\n===== Final Score =====")
        print("Your Score:", user_score)
        print("Computer Score:", computer_score)

        if user_score > computer_score:
            print("Overall Winner: You")
        elif computer_score > user_score:
            print("Overall Winner: Computer")
        else:
            print("Overall Result: Tie")

        print("\nThanks for playing!")
        break