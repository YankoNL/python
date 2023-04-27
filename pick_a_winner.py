import tkinter as tk
import random


def pick_winner():
    # Get user inputs
    try:
        min_num = int(min_entry.get())
        max_num = int(max_entry.get())
    except ValueError:
        winner_label.config(text="Error!\nPlease use integers only.",
                            font=("Helvetica", 14), fg="#333333")
        return

    # Check for valid input values
    if min_num <= 0 or max_num <= 0:
        winner_label.config(text="Error!\nPlease use positive integers.",
                            font=("Helvetica", 14), fg="#333333")
        return
    elif min_num >= max_num:
        winner_label.config(text="Error!\nFirst integer must be\nless than the second integer",
                            font=("Helvetica", 14), fg="#333333")
        return

    # Generate random number between min and max
    winner = random.randint(min_num, max_num)

    # Update label to display winner
    winner_label.config(text=f"The winner is: {winner}", fg="#1E9400", font=("Helvetica", 16, "bold"))


# Create the GUI window
window = tk.Tk()
window.title("Pick a Winner")
window.geometry("400x400")
window.resizable(False, False)

# Create labels and entries for min and max inputs
min_label = tk.Label(window, text="Start integer:", font=("Helvetica", 14), fg="#333333")
min_label.grid(row=0, column=0, padx=5, pady=5)

min_entry = tk.Entry(window, font=("Helvetica", 16))
min_entry.grid(row=0, column=1, padx=5, pady=5)

max_label = tk.Label(window, text="End integer:", font=("Helvetica", 14), fg="#333333")
max_label.grid(row=1, column=0, padx=5, pady=5)

max_entry = tk.Entry(window, font=("Helvetica", 16))
max_entry.grid(row=1, column=1, padx=5, pady=5)

# Create button to pick winner
winner_button = tk.Button(window, text="Generate a winner", command=pick_winner, padx=20, pady=10, bg="#FFC107",
                          fg="#333333", font=("Helvetica", 16, "bold"), relief="groove")
winner_button.grid(row=2, column=0, columnspan=2, pady=10)

# Create label to display winner
winner_label = tk.Label(window, text="", height=4)
winner_label.grid(row=3, column=0, columnspan=3, pady=10)

# Author label
min_label = tk.Label(window, text="Made by YankoNL", font=("Helvetica", 10))
min_label.grid(row=4, column=0, columnspan=2, pady=1)

# Center all elements
for i in range(4):
    window.grid_rowconfigure(i, weight=1)

for i in range(2):
    window.grid_columnconfigure(i, weight=1)

# Run the GUI window
window.mainloop()
