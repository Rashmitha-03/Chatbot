# Simple Chatbot GUI

This project is a simple chatbot application built using Python and Tkinter. It creates a desktop chat window where the user can interact with the bot through predefined topic buttons such as Technology, Sports, and Movies.

## Features
- Graphical chat interface
- Scrollable chat history
- Quick topic selection buttons
- Basic keyword-based chatbot responses
- Beginner-friendly project for learning Python GUI development

## Requirements
- Python 3.x
- Tkinter (usually included with Python)

## How to Run
Open your terminal in the project folder and run:

```bash
python main.py
```

## Project Description
The chatbot uses a simple response dictionary and matches user input to common phrases like:
- hello
- how are you
- bye
- technology
- sports
- movies

If the input is not recognized, the bot returns:
> I'm not sure how to respond to that.

The application includes:
- a `SimpleChatbot` class that handles the logic
- a `ChatbotGUI` class that creates the graphical interface

## Example Interaction
```text
User selects: Technology
Bot: I love talking about technology!

User selects: Sports
Bot: Sports are exciting! What's your favorite sport?

User selects: Bye
Bot: Goodbye!
```

## File Structure
- `main.py` — contains the chatbot logic and GUI

## Possible Improvements
- Add a text box for typing custom messages
- Expand the response database
- Add more chatbot topics
- Save chat history to a file
- Implement more advanced AI/NLP logic

## Notes
This is a basic project intended for learning and experimentation. It is easy to extend and customize for more complex chatbot behavior.

---

If you want, I can also give you:
- a more professional GitHub-style README,
- a shorter README for a school project,
- or a full README written in a nicer portfolio format.
