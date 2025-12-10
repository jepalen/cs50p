import pyttsx3

def get_voice(title, time, instructions):
    newVoiceRate = 145
    engine = pyttsx3.init()
    engine.setProperty('rate',newVoiceRate)
    engine.say(title)
    engine.say(time)
    engine.say(instructions)
    engine.save_to_file(title, f'{title}.mp3')
    engine.runAndWait()
