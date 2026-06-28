"""
Simple FAQ Chatbot System
--------------------------
AI Practical - Rule-Based Chatbot
Author : Niharika Acharya
Technique : Dictionary-based Pattern Matching
Language : Python 3
"""

# Knowledge base: maps a question (in lowercase) to its answer
FAQ: dict = {
    "hi": "Hello! How can I help you?",
    "hello": "Hello! How can I help you?",
    "hey": "Hello! How can I help you?",
    "what is your name": "My name is FAQ Bot.",
    "how are you": "I am doing great. Thank you for asking!",

    "what is computer": "Computer is an electronic machine that accepts raw data and gives meaningful information to the user.",
    "what is python": "Python is a popular programming language used for web development, AI, data science, and more.",
    "who created python": "Python was created by Guido van Rossum.",
    "what is ai": "AI stands for Artificial Intelligence. It enables machines to perform tasks that normally require human intelligence.",
    "what is machine learning": "Machine Learning is a branch of AI that allows systems to learn from data.",
    "what is deep learning": "Deep Learning is a subset of Machine Learning that uses neural networks with multiple layers.",
    "what is spam email": "Spam emails are unwanted messages sent in bulk, often for advertising or scams.",
    "how to detect spam emails": "Spam emails can be detected using AI and Machine Learning algorithms such as Naive Bayes and Neural Networks.",
    "what is github": "GitHub is a platform used to store, manage, and share code repositories.",
    "what is git": "Git is a version control system used to track changes in code.",
    "what is html": "HTML stands for HyperText Markup Language and is used to create web pages.",
    "what is css": "CSS stands for Cascading Style Sheets and is used to style web pages.",
    "what is javascript": "JavaScript is a programming language used to make web pages interactive.",
    "what is database": "A database is an organized collection of data that can be easily accessed and managed.",
    "what is sql": "SQL stands for Structured Query Language and is used to interact with databases.",
    "what is cloud computing": "Cloud computing provides computing services such as storage and servers over the internet.",
    "what is cyber security": "Cybersecurity is the practice of protecting systems, networks, and data from digital attacks.",
    "what is an operating system": "An operating system manages computer hardware and software resources.",
    "what is linux": "Linux is a free and open-source operating system.",
    "what is windows": "Windows is an operating system developed by Microsoft.",
    "what is chatbot": "A chatbot is a software application that simulates human conversation.",
    "what is internet": "The Internet is a global network connecting millions of computers worldwide.",
    "thank you": "You're welcome!",
}


def get_response(user_input: str) -> str:
    """
    Look up a response for the given user input.

    Args:
        user_input: The raw text typed by the user.

    Returns:
        The matching answer from the FAQ dictionary, or a default
        fallback message if no match is found.
    """
    cleaned_input = user_input.lower().strip()

    if cleaned_input in FAQ:
        return FAQ[cleaned_input]

    return "Sorry, I don't understand that question."


def print_welcome_message() -> None:
    """Print the chatbot's welcome banner."""
    print("===================================")
    print("     Welcome to FAQ Chatbot")
    print("Type 'bye' to exit the chatbot.")
    print("===================================")


def main() -> None:
    """Program entry point - runs the chatbot loop."""
    print_welcome_message()

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break

        response = get_response(user_input)
        print("Bot:", response)


if __name__ == "__main__":
    main()
