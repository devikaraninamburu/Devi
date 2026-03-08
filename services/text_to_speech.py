from gtts import gTTS

def generate_voice(text):

    tts = gTTS(text=text)

    file = "response.mp3"

    tts.save(file)

    return file
