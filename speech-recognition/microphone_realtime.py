#!/usr/bin/env python3

# NOTE: PyAudio is required because it uses the Microphone class

import speech_recognition as sr

# Obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    command = ""
    # Terminate the speech recognition loop when the stop command is given
    while(command != "stop"):
        print("Give Command")
        audio = r.listen(source)

        # Recognize speech using Google Speech Recognition
        try:
            command = r.recognize_google(audio)
            print("Your command is: " + command)
        except sr.UnknownValueError:
            print("I could not understand your command.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
