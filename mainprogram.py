import pandas as pd
import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from questionnaire import questions

# Input CSV file that has information abuot residences
df = pd.read_csv('uofcresidences.csv')

# Declare that we have not asked any questions yet and that the user has not given any answers yet
current_question = 0
answers = []

# Create a list for the choice buttons
choice_buttons = []

# Define a function for what happens when the user selects a choice
def button_pressed(c):
    global current_question
    answers.append(c)
    if current_question < len(questions) - 1:
        current_question += 1
        show_question()
    else:
        messagebox.showinfo()
        root.destroy()

# Define a function that shows the current question
def show_question():
    question_label.config(text=questions[current_question]["question"])
    choices = questions[current_question]["choices"]
    for button in choice_buttons:
        button.destroy()
    for i in range(len(choices)):
        button = ttk.Button(
        root,
        text=choices[i],
        command=lambda c=choices[i]: button_pressed(c)
        )
        button.pack(pady=5)
        choice_buttons.append(button)

# TODO: Define how the recommendation is calculated and compare the user's choices to the residences in the pandas dataframe
def recommendation():
    pass

# Create and Design the Main Window
root = tk.Tk()
root.title("University of Calgary Residence Recommender")
root.geometry("600x400")
style = Style(theme="flatly")

# Configure the font size for the choice buttons
style.configure("TButton", font=("Hellvetica", 22))

# Create and Design the Question Label
question_label = ttk.Label(
    root,
    anchor="center",
    font=("Hellvetica", 26),
    wraplength=500,
    padding=10
)
question_label.pack(
    padx=20, pady=20
)

# Show the first question
show_question()

# Start the main event loop
root.mainloop()
