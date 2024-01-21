import speech_recognition as sr

from constants import commands

def setCommand(command, value):
    try:
        command.acquire()
        command.value = value
        command.release()
    except:
        command.release()

def startSpeechRecognition(command):
    recognizer = sr.Recognizer()
    while True:
        try:
            audio = capture_voice_input(recognizer)
            text = convert_voice_to_text(audio, recognizer)

            print(text)

            if "volume" in text.lower():
                setCommand(command, commands['Volume'])
            if "stop" in text.lower():
                setCommand(command, commands['Idle'])
        except:
            pass

def capture_voice_input(recognizer):
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, phrase_time_limit=2)
    return audio

def convert_voice_to_text(audio, recognizer):
    try:
        text = recognizer.recognize_google(audio)
    except sr.UnknownValueError as e:
        text = ""
    except sr.RequestError as e:
        text = ""
    return text
