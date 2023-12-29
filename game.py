import tkinter as tk
import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

def on_choice(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

def play_again():
    result_label.config(text="")
    rock_button["state"] = paper_button["state"] = scissors_button["state"] = "normal"

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Create buttons for rock, paper, and scissors
rock_button = tk.Button(root, text="Rock", command=lambda: on_choice("rock"))
rock_button.grid(row=0, column=0, padx=10, pady=10)

paper_button = tk.Button(root, text="Paper", command=lambda: on_choice("paper"))
paper_button.grid(row=0, column=1, padx=10, pady=10)

scissors_button = tk.Button(root, text="Scissors", command=lambda: on_choice("scissors"))
scissors_button.grid(row=0, column=2, padx=10, pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.grid(row=1, column=0, columnspan=3, pady=10)

# Create a button to play again
play_again_button = tk.Button(root, text="Play Again", command=play_again)
play_again_button.grid(row=2, column=0, columnspan=3, pady=10)

# Run the Tkinter event loop
root.mainloop()

