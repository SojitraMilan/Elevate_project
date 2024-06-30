import tkinter as tk
from tkinter import scrolledtext

# Function to handle sending the user input to the chatbot
def send_message():
    user_message = user_entry.get()
    if user_message.strip():
        chat_history.configure(state=tk.NORMAL)
        chat_history.insert(tk.END, "You: " + user_message + "\n")
        chat_history.configure(state=tk.DISABLED)
        chat_history.yview(tk.END)  # Scroll to the end of the chat history

        # Generate chatbot response
        response = get_bot_response(user_message)
        chat_history.configure(state=tk.NORMAL)
        chat_history.insert(tk.END, "Bot: " + response + "\n")
        chat_history.configure(state=tk.DISABLED)
        chat_history.yview(tk.END)  # Scroll to the end of the chat history

        # Clear the user input
        user_entry.delete(0, tk.END)

# Function to generate a response based on the user input
def get_bot_response(user_message):
    # Basic response rules (this can be enhanced with more complex logic or NLP)
    user_message = user_message.lower()
    if "hello" in user_message or "hi" in user_message:
        return "Hello! How can I help you today?"
    elif "how are you" in user_message:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "name" in user_message:
        return "I am a chatbot. What's your name?"
    
    elif "weather" in user_message:
        return "I can't check the weather right now, but you can ask me other questions."
    elif "bye" in user_message:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that. Can you ask something else?"

# Create the main application window
window = tk.Tk()
window.title("Chatbot")
window.geometry("500x600")
window.resizable(False, False)

# Chat history display (using a scrolled text area)
chat_history = scrolledtext.ScrolledText(window, wrap=tk.WORD, state=tk.DISABLED)
chat_history.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Frame to hold the user input field and send button
input_frame = tk.Frame(window)
input_frame.pack(pady=10, padx=10, fill=tk.X)

# User input entry
user_entry = tk.Entry(input_frame, font=("Arial", 14))
user_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)

# Send button
send_button = tk.Button(input_frame, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT)

# Bind the Enter key to send the message
window.bind('<Return>', lambda event: send_message())

# Start the Tkinter event loop
window.mainloop()
