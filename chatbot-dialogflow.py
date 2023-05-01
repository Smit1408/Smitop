import os
import google.cloud.dialogflow_v2 as dialogflow
import google.auth
import google.auth.transport.requests
import tkinter as tk

# Set environment variable for credentials file path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./agent-name-wvvvpd-a1ffe962fcc8 (copy).json"

# Define the project ID
project_id = "agent-name-wvvvpd"

# Create a Dialogflow session client
session_client = dialogflow.SessionsClient()

# Create the main window
root = tk.Tk()
root.title("Chatbot")

# Create the chatbox
chatbox = tk.Text(root, width=50, height=10)
chatbox.pack(padx=10, pady=10)

# Create the input field
input_field = tk.Entry(root, width=50)
input_field.pack(padx=10, pady=10)

# Define the callback function for the "Send" button
def send_message():
    # Get the user input text
    user_text = input_field.get()

    # Create a Dialogflow session ID
    session_id = f"chatbot_session_{hash(str(user_text))}"

    # Create a query input
    text_input = dialogflow.types.TextInput(text=user_text, language_code='en')
    query_input = dialogflow.types.QueryInput(text=text_input)

    # Send the query to Dialogflow and get the response
    session = session_client.session_path(project_id, session_id)
    response = session_client.detect_intent(session=session, query_input=query_input)

    # Get the response text from Dialogflow
    bot_text = response.query_result.fulfillment_text

    # Display the user input and bot response in the chatbox
    chatbox.insert(tk.END, f"You: {user_text}\n")
    chatbox.insert(tk.END, f"Chatbot: {bot_text}\n")
    chatbox.insert(tk.END, "-"*50 + "\n")

    # Clear the input field
    input_field.delete(0, tk.END)

# Create the "Send" button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# Start the GUI main loop
root.mainloop()

