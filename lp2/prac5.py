def chatbot(first_time=True):
    if first_time:
        print("Welcome to Customer Support Chatbot!")
        print("You can ask about products, prices, orders, delivery, returns, and payment methods.")
        print("Type bye to exit.\n")

    user = input("You: ").lower().strip()

    if user == "bye":
        print("Bot: Thank you for visiting. Have a great day!")
    elif user == "hi" or user == "hello" or user == "hey":
        print("Bot: Hello! How can I help you today?\n")
        chatbot(False)
    elif "product" in user:
        print("Bot: We have mobiles, laptops, and headphones available.\n")
        chatbot(False)
    elif "price" in user:
        print("Bot: Prices in INR - mobiles from Rs. 10,000, laptops from Rs. 35,000, and headphones from Rs. 1,500.\n")
        chatbot(False)
    elif "order" in user:
        print("Bot: Please provide your order ID to check status.\n")
        chatbot(False)
    elif "delivery" in user:
        print("Bot: Delivery usually takes 3 to 5 business days.\n")
        chatbot(False)
    elif "return" in user:
        print("Bot: Products can be returned within 7 days of delivery.\n")
        chatbot(False)
    elif "payment" in user:
        print("Bot: We support UPI, Debit Card, Credit Card, and Net Banking.\n")
        chatbot(False)
    else:
        print("Bot: Sorry, I didn't understand.\n")
        chatbot(False)


if __name__ == "__main__":
    chatbot()