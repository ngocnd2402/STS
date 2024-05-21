import openai
from openai import OpenAI
from io import BytesIO


client = OpenAI(api_key='YOUR_API_KEY')

# def convert_text_to_speech(text):
#     sound_file = BytesIO()
#     tts = gTTS(text, lang='en')
#     tts.write_to_fp(sound_file)
#     sound_file.seek(0)  # Reset buffer position
#     return sound_file

def convert_text_to_speech(text):
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )
    response_content = response.content
    sound_file = BytesIO(response_content)
    sound_file.seek(0)
    return sound_file