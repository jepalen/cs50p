#cow and text to speech 
import cowsay
import pyttsx3

engine = pyttsx3.init()
message = input("Message: ")
cowsay.cow(message)
engine.say(message)
engine.runAndWait()
