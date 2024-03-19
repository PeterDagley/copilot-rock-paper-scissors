# Write a rock, paper scissors game using the CoPilot AI
# import random module
import random

# Define main function that defines all the logic
def main():
    # Define a list of choices
    choices = ["rock", "paper", "scissors"]
    # Define a variable to keep track of the user's score
    user_score = 0
    # Define a variable to keep track of the computer's score
    computer_score = 0
    # Define a variable to keep track of the number of rounds
    rounds = 0
    # Define a while loop that continues until the user decides to quit
    while True:
        # Increment the number of rounds
        rounds += 1
        # Print the current round number
        print(f"Round {rounds}")
        # Ask the user to make a choice
        user_choice = input("Enter rock, paper, or scissors: ")
        # Generate a random choice for the computer
        computer_choice = random.choice(choices)
        # Print the computer's choice
        print(f"Computer chose {computer_choice}")
        # Check if the user and computer made the same choice
        if user_choice == computer_choice:
            # Print that it's a tie
            print("It's a tie!")
        # Check if the user chose rock
        elif user_choice == "rock":
            # Check if the computer chose scissors
            if computer_choice == "scissors":
                # Print that the user wins
                print("You win!")
                # Increment the user's score
                user_score += 1
            # Otherwise
            else:
                # Print that the computer wins
                print("Computer wins!")
                # Increment the computer's score
                computer_score += 1
        # Check if the user chose paper
        elif user_choice == "paper":
            # Check if the computer chose rock
            if computer_choice == "rock":
                # Print that the user wins
                print("You win!")
                # Increment the user's score
                user_score += 1
            # Otherwise
            else:
                # Print that the computer wins
                print("Computer wins!")
                # Increment the computer's score
                computer_score += 1
        # Check if the user chose scissors
        elif user_choice == "scissors":
            # Check if the computer chose paper
            if computer_choice == "paper":
                # Print that the user wins
                print("You win!")
                # Increment the user's score
                user_score += 1
            # Otherwise
                
if __name__ == "__main__":
    main()