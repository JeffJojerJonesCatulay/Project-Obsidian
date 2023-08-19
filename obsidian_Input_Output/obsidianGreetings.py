import datetime
from obsidian_Input_Output import obsidianSpeak as OS


def obsidianGreetings():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        msg1 = "Access Granted...Good Morning. How may I help you"
        OS.speak(msg1)
        log = "obsidian_Log_Files\log.dat"
        f = open(log, "a")
        f.write("Obsidian: " + msg1 + "\n\n")
        f.close()
    elif hour >= 12 and hour < 18:
        msg2 = "Access Granted...Good Afternoon. How may I help you"
        OS.speak(msg2)
        log = "obsidian_Log_Files\log.dat"
        f = open(log, "a")
        f.write("Obsidian: " + msg2 + "\n\n")
        f.close()
    else:
        msg3 = "Access Granted...Good Evening. How may I help you"
        OS.speak(msg3)
        log = "obsidian_Log_Files\log.dat"
        f = open(log, "a")
        f.write("Obsidian: " + msg3 + "\n\n")
        f.close()

