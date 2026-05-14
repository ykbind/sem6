import tkinter as tk
from tkinter import scrolledtext

root = tk.Tk()
root.title("Hospital Expert System")
root.geometry("500x400")

questions = [
    "Do you have fever?",
    "Do you have cough?",
    "Do you have chest pain?",
    "Do you have any injury or fracture?",
    "Do you have stomach pain?"
]

answers = {}
current_question = 0

# Display area
display = scrolledtext.ScrolledText(root, height=15, width=50, state=tk.DISABLED)
display.pack(padx=10, pady=10)

# Input field
entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=5)

def send_message():
    global current_question
    user_input = entry.get().strip().lower()
    entry.delete(0, tk.END)
    
    if not user_input:
        return
    
    if user_input not in ["yes", "no"]:
        display.config(state=tk.NORMAL)
        display.insert(tk.END, "Error: Please enter 'yes' or 'no'\n\n")
        display.config(state=tk.DISABLED)
        display.see(tk.END)
        return
    
    # Display question and answer
    display.config(state=tk.NORMAL)
    display.insert(tk.END, "Q: " + questions[current_question] + "\n")
    display.insert(tk.END, "A: " + user_input + "\n\n")
    
    answers[current_question] = user_input
    current_question += 1
    
    if current_question < len(questions):
        display.insert(tk.END, "Next: " + questions[current_question] + "\n\n")
    else:
        show_result()
    
    display.config(state=tk.DISABLED)
    display.see(tk.END)

def show_result():
    fever = answers.get(0, "no")
    cough = answers.get(1, "no")
    chest_pain = answers.get(2, "no")
    injury = answers.get(3, "no")
    stomach_pain = answers.get(4, "no")
    
    display.config(state=tk.NORMAL)
    display.insert(tk.END, "--- Diagnosis Suggestion ---\n")
    
    if fever == "yes" and cough == "yes":
        diagnosis = "You may have a viral infection or flu.\nSuggested Department: General Medicine"
    elif chest_pain == "yes":
        diagnosis = "You may need a heart check-up.\nSuggested Department: Cardiology"
    elif injury == "yes":
        diagnosis = "You may require bone or injury treatment.\nSuggested Department: Orthopedics"
    elif stomach_pain == "yes":
        diagnosis = "You may have digestive issues.\nSuggested Department: Gastroenterology"
    else:
        diagnosis = "Please consult a General Physician for further diagnosis."
    
    display.insert(tk.END, diagnosis + "\n")
    display.config(state=tk.DISABLED)
    display.see(tk.END)
    entry.config(state=tk.DISABLED)

# Send button
btn = tk.Button(root, text="Send", command=send_message)
btn.pack(pady=5)

entry.bind("<Return>", lambda e: send_message())

# Welcome message
display.config(state=tk.NORMAL)
display.insert(tk.END, "Welcome to Hospital Expert System!\nAnswer the following questions with 'yes' or 'no'.\n\n")
display.insert(tk.END, "First: " + questions[0] + "\n\n")
display.config(state=tk.DISABLED)

root.mainloop()