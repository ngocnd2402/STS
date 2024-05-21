import speech_recognition as sr

def record_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak into the microphone...")
        audio_data = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        print("Audio captured.")
        audio_bytes = audio_data.get_wav_data()
        return audio_bytes
