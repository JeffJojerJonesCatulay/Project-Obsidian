import speech_recognition as sr
import datetime


def takeUserInput():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        input_val = r.recognize_google(audio, language='en-us')
        print(f"user said: {input_val}\n")

    except Exception as e:
        print("Error")
        input_val = None
        exit()

    # mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"
    # sample_rate = 48000
    # chunk_size = 2048
    #
    # r = sr.Recognizer()
    #
    # mic_list = sr.Microphone.list_microphone_names()
    #
    # for i, microphone_name in enumerate(mic_list):
    #     if microphone_name == mic_name:
    #         device_id = i
    #
    # with sr.Microphone(sample_rate=sample_rate,
    #                    chunk_size=chunk_size) as source:
    #     r.adjust_for_ambient_noise(source)
    #     print("Listening...")
    #     audio = r.listen(source)
    #
    # try:
    #     input_val = r.recognize_google(audio)
    #     print(f"user said: {input_val}\n")
    #
    # except sr.UnknownValueError:
    #     print("Google Speech Recognition could not understand audio")
    #
    # except sr.RequestError as e:
    #     print("Error")

    now = datetime.datetime.now()
    date_time = now.strftime("%b %d %Y %I:%M %p")
    logTime = str(date_time)
    log = "obsidian_Log_Files\log.dat"
    f = open(log, "a")
    f.write(logTime + "\nuser said: " + input_val + "\n")
    f.close()
    return input_val
