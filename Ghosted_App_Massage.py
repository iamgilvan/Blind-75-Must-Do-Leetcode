class Message:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_read = False

    def read_message(self):
        self.is_read = True
        return self.content

class GhostedMessagingApp:
    def __init__(self):
        self.messages = {}

    def send_message(self, sender, receiver, content):
        message = Message(sender, receiver, content)
        if receiver not in self.messages:
            self.messages[receiver] = []
        self.messages[receiver].append(message)

    def read_messages(self, receiver):
        if receiver not in self.messages:
            return "No messages"

        unread_messages = [msg.read_message() for msg in self.messages[receiver] if not msg.is_read]

        # Remove "ghosted" messages after reading
        self.messages[receiver] = [msg for msg in self.messages[receiver] if not msg.is_read]

        return unread_messages if unread_messages else "No new messages"

# Usage:
app = GhostedMessagingApp()
app.send_message("Alice", "Bob", "Hello, Bob!")
app.send_message("Alice", "Bob", "Are you there?")

# Bob reading the messages
print(app.read_messages("Bob"))  # Output: ["Hello, Bob!", "Are you there?"]
print(app.read_messages("Bob"))  # Output: No new messages
