from nltk.chat.util import Chat, reflections

def chatBot():

    responses = [
        ['my name is (.*)', ['hi %1']],
        ['hello', ['hey there boss', 'hello sir']],
    ]
    chat = Chat(responses, reflections, )
    chat.converse()

