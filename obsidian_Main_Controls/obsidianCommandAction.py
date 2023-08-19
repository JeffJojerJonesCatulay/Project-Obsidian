import webbrowser
import wikipedia
import os
import random
import datetime
from obsidian_Input_Output import obsidianSpeak as OS, obsidianTakeUserInput as OTUI

def openCommand(userInput):
    try:
        openCommand = {}
        oc = "dat_Databases\openCommandDatabase.dat"
        with open(oc, "r") as file:
            for line in file:
                key, value = line.strip().split(",")
                openCommand[key] = value

        for key, value in openCommand.items():
            tags = key
            if tags in userInput:
                res = [val for key, val in openCommand.items() if tags in key]
                valueDictionary = str(res)
                result = valueDictionary.replace('[', '').replace(']', '').replace("'", '')
                msg = ("Opening %s..." % tags)
                websites(msg, result)
                log = "obsidian_Log_Files\log.dat"
                f = open(log, "a")
                f.write("Obsidian: " + msg + "\n" + "\nObsidian: " + result +"\n\n")
                f.close()
                break
    except Exception as e:
        errorMsg = "I have a problem..sorry.."
        OS.speak(errorMsg)
        log = "obsidian_Log_Files\log.dat"
        f = open(log, "a")
        f.write("Obsidian: " + errorMsg + "\n\n")
        f.close()

def name():
    try:
        msg1 = 'I am OBSIDIAN...'
        msg2 = 'How about you...'
        OS.speak(msg1)
        OS.speak(msg2)
        name = OTUI.takeUserInput()
        nameOutput = str(name)
        final = nameOutput.replace('i am', '').replace('my name is', '')
        if 'jeff' in final:
            msg3 = "you're my boss, my creator..."
            OS.speak(msg3)
            log = "obsidian_Log_Files\log.dat"
            f = open(log, "a")
            f.write("Obsidian: " + msg3 + "\n\n")
            f.close()
        else:
            msg4 = "You're not my boss but..."
            msg5 = "Very nice to meet you"
            OS.speak(msg4)
            OS.speak(msg5 + final)
            log = "obsidian_Log_Files\log.dat"
            f = open(log, "a")
            f.write("Obsidian: " + msg4 + "\nObsidian: " + msg5 + ", " + final +  "\n\n")
            f.close()
    except Exception as e:
        errorMsg1 = "Sorry... im having a problem"
        errorMsg2 = "but, nice to meet you"
        OS.speak(errorMsg1)
        OS.speak(errorMsg2)
        log = "obsidian_Log_Files\log.dat"
        f = open(log, "a")
        f.write("Obsidian: " + errorMsg1 + "\nObsidian: " + errorMsg2 + "\n\n")
        f.close()

def age():
    birth_date = datetime.date(2020, 7, 20)
    now =datetime.datetime.now()
    end_date = datetime.datetime.date(now)
    gap = end_date - birth_date
    age = str(gap.days)
    msg1 = "I live " + age + " days from my creation"
    print(msg1)
    OS.speak(msg1)
    log = "obsidian_Log_Files\log.dat"
    f = open(log, "a")
    f.write("Obsidian: " + msg1 + "\n\n")
    f.close()

def wikipediaSearch(input):
    try:
        userInput = input
        msg1 = 'Searching Wikipedia...'
        OS.speak(msg1)
        print(msg1)
        query = userInput.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        OS.speak(result)
        log = "obsidian_Log_Files\log.dat"
        f = open(log, "a")
        f.write("Obsidian: " + msg1 + "\nObsidian: " + result + "\n\n")
        f.close()
    except Exception as e:
        errorMsg = "Error searching wikipedia..."
        OS.speak(errorMsg)
        log = "obsidian_Log_Files\log.dat"
        f = open(log, "a")
        f.write("Obsidian: " + errorMsg + "\n\n")
        f.close()


def websites(message, fileDir):
    try:
        OS.speak(message)
        print(message)
        webbrowser.open(fileDir)
    except Exception as e:
        errorMsg = "Website not found..."
        OS.speak(errorMsg)


def googleSearch(userInput):
    try:
        query = userInput
        from googlesearch import search
        # msg1 = "...Here are some links for your search..."
        # OS.speak(msg1)
        # print(msg1)
        # for i in search(query, tld="co.in", num=10, stop=10, pause=2):
        #     print(i)
        OS.speak(search(query, num_results=100))
        log = "obsidian_Log_Files\log.dat"
        f = open(log, "a")
        f.write("Obsidian: " + "\nObsidian: "  + "\n\n")
        f.close()
    except Exception as e:
        errorMsg = "Sorry error search..."
        OS.speak(errorMsg)
        log = "obsidian_Log_Files\log.dat"
        f = open(log, "a")
        f.write("Obsidian: " + "\nObsidian: " + "\n\n")
        f.close()


def computerFiles(message, fileDir):
    try:
        OS.speak(message)
        print(message)
        os.startfile(os.path.join(fileDir))
    except Exception as e:
        errorMsg = "file not found..."
        OS.speak(errorMsg)


def playMusic():
    try:
        msg1 = "Playing Music..."
        msg2 = "I will terminate now, so you can listen to your music..."
        n = random.randint(0, 100)  # random song selection
        OS.speak(msg1)
        print(msg1)
        song_dir = "D:\\Music"
        songs = os.listdir(song_dir)
        os.startfile(os.path.join(song_dir, songs[n]))
        OS.speak(msg2)
        log = "obsidian_Log_Files\log.dat"
        f = open(log, "a")
        f.write("Obsidian: " + msg1 + "\nObsidian: " + msg2 + "\n\n")
        f.close()
        exit()
    except Exception as e:
        errorMsg = "Directory not found..."
        OS.speak(errorMsg)
        log = "obsidian_Log_Files\log.dat"
        f = open(log, "a")
        f.write("Obsidian: " + errorMsg + "\n\n")
        f.close()


def time():
    msg1 = "date and time:"
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    now = datetime.datetime.now()  # current date and time
    date_time = now.strftime("%b %d %Y %I:%M %p")
    logTime = str(date_time)
    print(msg1, logTime)
    OS.speak("it's " + strTime)
    log = "obsidian_Log_Files\log.dat"
    f = open(log, "a")
    f.write("Obsidian: " + msg1 + "\nObsidian:" + logTime + "\n\n")
    f.close()