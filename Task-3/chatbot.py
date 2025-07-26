from nltk.chat.util import Chat, reflections

# Chat patterns to respond to any kind of input
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today?", "Hi there!"]
    ],
    [
        r"(.*)your name(.*)",
        ["I'm CodTech AI, your assistant."]
    ],
    [
        r"(.*) help (.*)",
        ["Sure, I'm here to help. What do you need?"]
    ],
    [
        r"(.*)\?",
        ["That's an interesting question. Tell me more.", "I'll look into that.", "Great question!"]
    ],
    [
        r"quit",
        ["Goodbye! Have a nice day."]
    ],
    [
        r"(.*)",
        ["I'm not sure how to respond to that yet, but I'm learning.", "Could you rephrase that?", "Interesting..."]
    ],
]

def main():
    print("=" * 60)
    print("🤖 CodTech NLTK Chatbot")
    print("💬 Ask me anything. Type 'quit' to exit.")
    print("=" * 60)
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

if __name__ == "__main__":
    main()
