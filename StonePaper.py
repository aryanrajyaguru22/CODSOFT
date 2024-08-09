import tkinter as tk
from tkinter import messagebox
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
        return "user"
    else:
        return "computer"

def update_result(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = determine_winner(user_choice, computer_choice)

    if result == "user":
        user_score += 1
        result_text.set(f"You win! Computer chose {computer_choice}.")
    elif result == "computer":
        computer_score += 1
        result_text.set(f"You lose! Computer chose {computer_choice}.")
    else:
        result_text.set(f"It's a draw! Both chose {computer_choice}.")

    user_score_text.set(f"User Score: {user_score}")
    computer_score_text.set(f"Computer Score: {computer_score}")

root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("400x400")
root.config(bg="#F0F0F0")

user_score = 0
computer_score = 0

title = tk.Label(root, text="Rock, Paper, Scissors", font=("Helvetica", 24), bg="#F0F0F0")
title.pack(pady=20)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Helvetica", 18), bg="#F0F0F0")
result_label.pack(pady=20)

user_score_text = tk.StringVar(value="User Score: 0")
user_score_label = tk.Label(root, textvariable=user_score_text, font=("Helvetica", 16), bg="#F0F0F0")
user_score_label.pack(pady=10)

computer_score_text = tk.StringVar(value="Computer Score: 0")
computer_score_label = tk.Label(root, textvariable=computer_score_text, font=("Helvetica", 16), bg="#F0F0F0")
computer_score_label.pack(pady=10)

button_frame = tk.Frame(root, bg="#F0F0F0")
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", font=("Helvetica", 16), command=lambda: update_result("rock"),
                        width=10, bg="#FFC107", fg="white")
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", font=("Helvetica", 16), command=lambda: update_result("paper"),
                         width=10, bg="#4CAF50", fg="white")
paper_button.grid(row=0, column=1, padx=0)

scissors_button = tk.Button(button_frame, text="Scissors", font=("Helvetica", 16),
                            command=lambda: update_result("scissors"), width=10, bg="#2196F3", fg="white")
scissors_button.grid(row=0, column=2, padx=10)

root.mainloop()