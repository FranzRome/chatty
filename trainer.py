from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Chatty')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train based on the italian corpus
trainer.train("chatterbot.corpus.italian")

# Train based on the italian conversations corpus
trainer.train("chatterbot.corpus.italian.conversations")