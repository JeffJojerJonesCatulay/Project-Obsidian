from chat_Bot_Draft.chatBot import chatBot
from obsidian_Input_Output import obsidianSpeak as OS, obsidianGreetings as OG, obsidianTakeUserInput as OTUI
from obsidian_Main_Controls import obsidianTakeCommand as OTC
import datetime


def main(input):
    msg1 = "Project..Obsidian..., initializing..., Identify Authorization Code..."
    print("Initializing...")
    OS.speak(msg1)
    now = datetime.datetime.now()
    date_time = now.strftime("%b %d %Y %I:%M %p")
    logTime = str(date_time)
    log = "obsidian_Log_Files\log.dat"
    f = open(log, "a")
    f.write("\n" + logTime + "\nObsidian: " + msg1 + "\n\n")
    f.close()
    logIn = OTUI.takeUserInput()

    def validate(errorMsg):
        if logIn == "blue":
            OG.obsidianGreetings()
            OTC.takeCommand()
            exit()
        elif logIn == "terminate":
            OS.speak("Terminating Now...")
            exit()
        else:
            OS.speak(errorMsg)

    if input == 1:
        errorMsg1 = "Invalid Authorization Code.....,one more try before Termination..."
        validate(errorMsg1)
        log = "obsidian_Log_Files\log.dat"
        f = open(log, "a")
        f.write("Obsidian: " + errorMsg1 + "\n\n")
        f.close()
        main(0)
    else:
        errorMsg2 = "Invalid Authorization Code,...Terminating Now..."
        validate(errorMsg2)
        log = "obsidian_Log_Files\log.dat"
        f = open(log, "a")
        f.write("Obsidian: " + errorMsg2 + "\n\n")
        f.close()
        exit()


# OTC.takeCommand()
# interface()
main(1)
# chatBot()
