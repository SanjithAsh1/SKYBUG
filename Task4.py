import tkinter as tk
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")

        self.user_score = 0
        self.computer_score = 0

        self.choices = ['rock', 'paper', 'scissors']

        self.user_choice_var = tk.StringVar()
        self.computer_choice_var = tk.StringVar()
        self.winner_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # User choice frame
        user_choice_frame = tk.Frame(self.root)
        user_choice_frame.pack(pady=10)

        for choice in self.choices:
            tk.Radiobutton(user_choice_frame, text=choice.capitalize(), variable=self.user_choice_var, value=choice).pack(side=tk.LEFT)

        # Computer choice label
        tk.Label(self.root, textvariable=self.computer_choice_var, font=("Helvetica", 16)).pack(pady=10)

        # Play button
        play_button = tk.Button(self.root, text="Play", command=self.play)
        play_button.pack(pady=10)

        # Result label
        tk.Label(self.root, textvariable=self.winner_var, font=("Helvetica", 16)).pack(pady=10)

        # Score labels
        tk.Label(self.root, text=f"User score: {self.user_score}", font=("Helvetica", 16)).pack(pady=10)
        tk.Label(self.root, text=f"Computer score: {self.computer_score}", font=("Helvetica", 16)).pack(pady=10)

    def play(self):
        # Get user choice
        user_choice = self.user_choice_var.get()

        # Generate computer choice
        computer_choice = random.choice(self.choices)

        # Display computer choice
        self.computer_choice_var.set(computer_choice.capitalize())

        # Determine winner
        if user_choice == computer_choice:
            winner = "tie"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            winner = "user"
        else:
            winner = "computer"

        # Display result
        if winner == "user":
            self.winner_var.set("User wins!")
            self.user_score += 1
        elif winner == "computer":
            self.winner_var.set("Computer wins!")
            self.computer_score += 1
        else:
            self.winner_var.set("It's a tie!")

root = tk.Tk()
app = RockPaperScissorsApp(root)
root.mainloop()