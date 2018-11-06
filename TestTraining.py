# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 15:14:38 2018

@author: Khanh Bui
"""

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os



#chatbot = ChatBot('Ron Obvious')
#
## If error
## chatbot.storage.drop()
#
## Create a new trainer for the chatbot
#trainer = ChatterBotCorpusTrainer(chatbot)
#
## Train the chatbot based on the english corpus
#trainer.train("chatterbot.corpus.movie")
#
## Get a response to an input statement
#chatbot.get_response("Hello, how are you today?")



##########################################
bot = ChatBot('NapK')
bot.set_trainer(ChatterBotCorpusTrainer)

bot.train("chatterbot.corpus.movie")

name = input("NapK: what's your name?\n")

while True:
    request = input(name + ':')
    response = bot.get_response(request)
    print('NapK:', response, '\n')
    



#from chatterbot.trainers import ChatterBotCorpusTrainer
#
## Create a new trainer for the chatbot
#trainer = ChatterBotCorpusTrainer(chatbot)
#
## Train based on the english corpus
#trainer.train("chatterbot.corpus.english")
#
## Train based on english greetings corpus
#trainer.train("chatterbot.corpus.english.greetings")
#
## Train based on the english conversations corpus
#trainer.train("chatterbot.corpus.english.conversations")