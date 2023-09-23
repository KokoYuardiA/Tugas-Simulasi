import tkinter as tk

class PublishSubscribeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Publish-Subscribe Demo")

        self.message_label = tk.Label(root, text="Pesan yang diterima:")
        self.message_label.pack()

        self.message_listbox = tk.Listbox(root, height=5, width=40)
        self.message_listbox.pack()

        self.subscribe_button = tk.Button(root, text="Subscribe", command=self.subscribe)
        self.subscribe_button.pack()

        self.publish_label = tk.Label(root, text="Pesan yang akan Dikirim:")
        self.publish_label.pack()

        self.message_entry = tk.Entry(root)
        self.message_entry.pack()

        self.publish_button = tk.Button(root, text="Publish", command=self.publish)
        self.publish_button.pack()

        self.subscribers = []

    def subscribe(self):
        self.subscribers.append(self.message_listbox)

    def publish(self):
        message = self.message_entry.get()
        for subscriber in self.subscribers:
            subscriber.insert(tk.END, message)

if __name__ == "__main__":
    root = tk.Tk()
    app = PublishSubscribeApp(root)
    root.mainloop()
