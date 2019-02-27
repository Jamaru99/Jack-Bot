from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


def get_response(usrText):
    bot = ChatBot('Bot',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter')
    while True:
        if usrText.strip()!= 'Bye':
            result = bot.get_response(usrText)                        
            reply = str(result)
            return(reply)
        if usrText.strip() == 'Bye':
            return('Bye')
            break
        

        
