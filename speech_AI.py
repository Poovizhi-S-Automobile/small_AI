import pyttsx3
speech=pyttsx3.init()
a="poovizhi"
speech.say(a)
#rate
rate=speech.getProperty('rate')
print(a)
speech.setProperty('rate', 135)
speech.runAndWait()

# VOLUME
volume = speech.getProperty('volume')   # getting to know current volume level (min=0 and max=1)
print("0.8")                         # printing current volume level
speech.setProperty('volume',0.8)        # setting up volume level  between 0 and 1

voices = speech.getProperty('voices')       # getting details of current voice
#engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
speech.setProperty('voice', voices[1].id)   # changing index, changes voices. 1 for female
speech.say("Hello World!")
speech.say('My current speaking rate is ' + str(rate))
speech.runAndWait()
speech.stop()

# Saving Voice to a file
# On Linux, make sure that 'espeak-ng' is installed
speech.save_to_file('Hello World', 'test.mp3')
speech.runAndWait()