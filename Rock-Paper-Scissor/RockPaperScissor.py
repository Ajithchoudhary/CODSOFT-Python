import random

print("Welcome to Rock, Paper, Scissors!")

while True:
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        print("You win!")
    else:
        print("You lose!")
    
    if input("Play again? (yes/no): ").lower() != 'yes':
        print("Thanks for playing!")
        break
