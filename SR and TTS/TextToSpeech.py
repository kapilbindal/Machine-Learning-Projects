
## Pyttsx text to speech
import pyttsx3
engine = pyttsx3.init()
engine.say('Hello')
engine.runAndWait()

## gTTS text to speech
from gtts import gTTS
import os
tts = gTTS(text='Hello', lang='en')
tts.save('hello.mp3')

## Microsoft speech engine
import win32com.client as wincl
speak = wincl.Dispatch('SAPI.SpVoice')
speak.Speak('Hello World')
