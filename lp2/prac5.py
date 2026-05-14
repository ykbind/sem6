import tkinter as tk
from tkinter import scrolledtext

root = tk.Tk()
root.title("Chatbot")
root.geometry("500x400")

# Display area
display = scrolledtext.ScrolledText(root, height=15, width=50, state=tk.DISABLED)
display.pack(padx=10, pady=10)

# Input field
entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=5)

def send_message():
    user_input = entry.get().strip()
    entry.delete(0, tk.END)
    
    if not user_input:
        return
    
    # Display user message
    display.config(state=tk.NORMAL)
    display.insert(tk.END, "You: " + user_input + "\n")
    
    # Get bot response
    user = user_input.lower()
    if user == "bye":
        response = "Thank you for visiting. Have a great day!"
    elif user in ["hi", "hello", "hey"]:
        response = "Hello! How can I help you today?"
    elif "product" in user:
        response = "We have mobiles, laptops, and headphones available."
    elif "price" in user:
        response = "Prices in INR - mobiles from Rs. 10,000, laptops from Rs. 35,000, and headphones from Rs. 1,500."
    elif "order" in user:
        response = "Please provide your order ID to check status."
    elif "delivery" in user:
        response = "Delivery usually takes 3 to 5 business days."
    elif "return" in user:
        response = "Products can be returned within 7 days of delivery."
    elif "payment" in user:
        response = "We support UPI, Debit Card, Credit Card, and Net Banking."
    else:
        response = "Sorry, I didn't understand."
    
    display.insert(tk.END, "Bot: " + response + "\n\n")
    display.config(state=tk.DISABLED)
    display.see(tk.END)

# Send button
btn = tk.Button(root, text="Send", command=send_message)
btn.pack(pady=5)

entry.bind("<Return>", lambda e: send_message())

# Welcome message
display.config(state=tk.NORMAL)
display.insert(tk.END, "Bot: Welcome to Customer Support Chatbot! Ask about products, prices, orders, delivery, returns, and payment methods. Type 'bye' to exit.\n\n")
display.config(state=tk.DISABLED)

root.mainloop()