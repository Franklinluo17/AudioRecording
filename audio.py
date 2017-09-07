import pyaudio
import wave
import sndhdr
import speech_recognition as sr
import unicodedata
"""
needed to write to wav file
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"""

#create recognizer instance
def readAudio():
	r = sr.Recognizer()
	#read in audio file from microphone
	with sr.Microphone() as source:
		print("recording")
		audio = r.listen(source)
	#convert unicode string to string
	audioString = unicodedata.normalize('NFKD',r.recognize_google(audio)).encode('ascii','ignore')
	#print string to user
	try:
		print("You said: " + r.recognize_google(audio))
		return audioString
	except LookupError:
		print("Your speech was not recognizable")
readAudio()