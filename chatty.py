from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot_name = "Chatty"
chatbot = ChatBot(chatbot_name)


def train():
    # Create a new trainer for the chatbot
    trainer = ChatterBotCorpusTrainer(chatbot)

    # Train the chatbot based on the english corpus
    trainer.train("chatterbot.corpus.italian")


while True:
    user_input = input("User: ")

    # Get a response to an input statement
    print(chatbot.get_response(user_input))
