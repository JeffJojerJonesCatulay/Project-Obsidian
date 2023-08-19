from obsidian_Input_Output import obsidianSpeak as OS, obsidianTakeUserInput as OTUI
from obsidian_Main_Controls import obsidianQuestionResponse as OQR, obsidianCommandAction as OCA

def takeCommand():

    terminate = False  # termination process
    while not terminate:
        userInput = OTUI.takeUserInput().lower()
        if 'open' in userInput:
            OCA.openCommand(userInput)
        elif 'wikipedia' in userInput:
            OCA.wikipediaSearch(userInput)
        elif 'play music' in userInput:
            OCA.playMusic()
        elif 'in google' in userInput:
            OCA.googleSearch(userInput)
        elif 'the time' in userInput:
            OCA.time()
        elif 'your name' in userInput:
            OCA.name()
        elif 'your age' in userInput:
            OCA.age()
        elif 'how old' in userInput:
            OCA.age()
        elif 'terminate' in userInput:
            OS.speak("Terminating Now...")
            exit()
        else:
            OQR.questionResponse(userInput)

