import openai
from openai import OpenAI
from io import BytesIO

# Set OpenAI API key
client = OpenAI(api_key='YOUR_KEY_HERE')

def transcrip_audio(audio_bytes):
    audio_file = BytesIO(audio_bytes)
    audio_file.name = "temp_audio_file.wav"
    translation = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
    )
    print(translation.text)
    ans = str(translation.text)
    return ans

def transalte_to_eng(text):
    translation = client.chat.completions.create(
        model="gpt-3.5-turbo-0613",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a translator for conversations and I need you to review and improve text transmitted from any language into English. If any words are found to be missing or incorrect or does not fit the context of the sentence, please correct it accordingly. Remember, your role is to translate, and the only thing you need to do is translate into English, nothing else, do not change the original sentence if not necessary."
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )
    print(translation.choices[0].message.content)
    return translation.choices[0].message.content


def end2end_translation(audio_bytes):
    audio_file = BytesIO(audio_bytes)
    audio_file.name = "temp_audio_file.wav"
    translation = client.audio.translations.create(
        model="whisper-1", 
        file=audio_file
    )
    print(translation.text)
    ans = str(translation.text)
    return ans