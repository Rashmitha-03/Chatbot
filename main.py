import tkinter as tk
from tkinter import scrolledtext
import random

class SimpleChatbot:
    def __init__(self):
        self.responses = {
            "hello": ["Hi there!", "Hello!", "Hey!"],
            "how_are_you": ["I'm good, thank you!", "I'm doing well, how about you?"],
            "bye": ["Goodbye!", "See you later!", "Bye!"],
            "options": ["1. Technology", "2. Sports", "3. Movies"],
            "technology": ["I love talking about technology!", "What specific tech topic are you interested in?"],
            "sports": ["Sports are exciting! What's your favorite sport?", "Tell me about your favorite sports team."],
            "movies": ["Movies are great! What's your favorite movie genre?", "Have you seen any good movies lately?"]
            # Add more patterns and responses as needed
        }

    def process_user_input(self, user_input):
        user_input = user_input.lower()
        if "hello" in user_input:
            return random.choice(self.responses["hello"])
        elif "how are you" in user_input:
            return random.choice(self.responses["how_are_you"])
        elif "bye" in user_input:
            return random.choice(self.responses["bye"])
        elif "1" in user_input:
            return random.choice(self.responses["technology"])
        elif "2" in user_input:
            return random.choice(self.responses["sports"])
        elif "3" in user_input:
            return random.choice(self.responses["movies"])
        else:
            return "I'm not sure how to respond to that."

class ChatbotGUI:
    def __init__(self, master, chatbot):
        self.master = master
        self.chatbot = chatbot
        master.title("Chatbot GUI")

        # Create a scrolled text widget for the chat history
        self.chat_history = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10)
        self.chat_history.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Create buttons for predefined options
        self.create_option_buttons()

    def create_option_buttons(self):
        options = ["Technology", "Sports", "Movies"]
        for i, option in enumerate(options):
            button = tk.Button(self.master, text=option, command=lambda o=option: self.send_option(o))
            button.grid(row=i + 1, column=0, columnspan=2, padx=10, pady=5)

    def send_option(self, option):
        self.display_message(f"User selected: {option}")
        bot_response = self.chatbot.process_user_input(option)
        self.display_message(bot_response)

    def display_message(self, message):
        # Insert the message into the chat history
        self.chat_history.insert(tk.END, message + "\n")
        # Auto-scroll to the bottom
        self.chat_history.yview(tk.END)

if __name__ == "__main__":
    chatbot = SimpleChatbot()

    root = tk.Tk()
    app = ChatbotGUI(root, chatbot)
    root.mainloop()
