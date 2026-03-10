from src.recorder import record_audio
from src.transcriber import transcribe_audio
from src.chatgpt_client import ask_chatgpt
from src.tts import generate_audio

def main():

    audio_file = record_audio()

    text = transcribe_audio(audio_file)

    response = ask_chatgpt(text)

    generate_audio(response)

if __name__ == "__main__":
    main()