from gtts import gTTS

def generate_audio(text, filename="audio/response_audio.mp3"):

    tts = gTTS(text=text, lang="pt")

    tts.save(filename)

    return filename