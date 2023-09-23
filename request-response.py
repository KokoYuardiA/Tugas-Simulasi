import tkinter as tk
import requests

def send_request():
    # Code to send request to server
    response = requests.get("http://127.0.0.1:5000")
    response_label.config(text=response.text)

root = tk.Tk()
root.title("Request-Response Model")

# Create GUI elements
request_button = tk.Button(root, text="Send Request", command=send_request)
response_label = tk.Label(root, text="Waiting for response...")

# Add GUI elements to window
request_button.pack()
response_label.pack()

root.mainloop()