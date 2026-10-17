import tkinter as tk
from tkinter import scrolledtext
import random

class HospitalChatbot:
    def __init__(self):
        self.responses = {
            "hello": ["Hello! How can I help you today?", "Hi there! What brings you to the hospital chatbot?"],
            "appointment": ["Sure, let's schedule an appointment. Please provide your preferred date and time.",
                            "Great! When would you like to come in for an appointment?"],
            "test_results": ["To check your test results, please provide your patient ID or the date of your test.",
                             "Sure, I can help you with that. What's your patient ID or the date of your test?"],
            "medical_questions": ["Feel free to ask any medical questions you have, and I'll do my best to help.",
                                  "I'm here to answer your medical questions. What would you like to know?"],
            "goodbye": ["Thank you for using the hospital chatbot. Take care!", "Goodbye! If you have more questions, feel free to ask."]
            # Add more patterns and responses as needed
        }

    def process_user_input(self, user_input):
        user_input = user_input.lower()
        if "hello" in user_input:
            return random.choice(self.responses["hello"])
        elif "appointment" in user_input:
            return random.choice(self.responses["appointment"])
        elif "test results" in user_input:
            return random.choice(self.responses["test_results"])
        elif "medical questions" in user_input:
            return random.choice(self.responses["medical_questions"])
        elif "bye" in user_input:
            return random.choice(self.responses["goodbye"])
        else:
            return "I'm sorry, I didn't understand. Please choose one of the available options."

class HospitalChatbotGUI:
    def __init__(self, master, hospital_chatbot):
        self.master = master
        self.hospital_chatbot = hospital_chatbot
        master.title("Hospital Chatbot")

        # Create a scrolled text widget for the chat history
        self.chat_history = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10)
        self.chat_history.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Create buttons for predefined options
        self.create_option_buttons()

    def create_option_buttons(self):
        options = ["Hello", "Make an Appointment", "Check Test Results", "Ask Medical Questions", "Goodbye"]
        for i, option in enumerate(options):
            button = tk.Button(self.master, text=option, command=lambda o=option: self.send_option(o))
            button.grid(row=i + 1, column=0, columnspan=2, padx=10, pady=5)

    def send_option(self, option):
        self.display_message(f"User selected: {option}")
        bot_response = self.hospital_chatbot.process_user_input(option)
        self.display_message(bot_response)

    def display_message(self, message):
        # Insert the message into the chat history
        self.chat_history.insert(tk.END, message + "\n")
        # Auto-scroll to the bottom
        self.chat_history.yview(tk.END)

if __name__ == "__main__":
    hospital_chatbot = HospitalChatbot()

    root = tk.Tk()
    app = HospitalChatbotGUI(root, hospital_chatbot)
    root.mainloop()
