from obsidian_Input_Output import obsidianSpeak as OS


def questionResponse(input):
    try:
        responses = {}
        rd = "dat_Databases\\responseDatabase.dat"
        with open(rd, "r") as file:
            for line in file:
                key, value = line.strip().split(",")
                responses[key] = value

        userInput = input
        error = True
        for key, value in responses.items():
            tags = key
            if tags in userInput:
                res = [val for key, val in responses.items() if tags in key]
                result = str(res)
                OS.speak(result)
                error = False
                log = "obsidian_Log_Files\log.dat"
                f = open(log, "a")
                f.write("Obsidian: " + result + "\n\n")
                f.close()
        if error:
            errorMsg1 = "Sorry... i don't understand..."
            OS.speak(errorMsg1)
            log = "obsidian_Log_Files\log.dat"
            f = open(log, "a")
            f.write("Obsidian: " + errorMsg1 + "\n\n")
            f.close()

    except Exception as e:
        errorMsg2 = "Sorry... i don't understand..."
        OS.speak(errorMsg2)
        log = "obsidian_Log_Files\log.dat"
        f = open(log, "a")
        f.write("Obsidian: " + errorMsg2 + "\n\n")
        f.close()

