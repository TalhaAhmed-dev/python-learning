class ChatBot:
    def __init__(self, system_prompt):
        self.system_prompt = system_prompt
        self.history = []

    def send_message(self, message):
        self.history.append(f"User: {message}")

        response = f"I received your message: {message}"

        self.history.append(f"Bot: {response}")

        return response


bot = ChatBot("You are a helpful assistant.")

print(bot.system_prompt)

reply = bot.send_message("Hello")
print(reply)

reply = bot.send_message("How are you?")
print(reply)

print("\nChat History:")
for item in bot.history:
    print(item)