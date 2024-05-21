from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from module.audio_processing import record_audio
from module.translation import transcrip_audio, transalte_to_eng, end2end_translation
from module.text_to_speech import convert_text_to_speech

app = FastAPI()

@app.get("/")
async def get():
    with open("index.html") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        audio_data = await websocket.receive_bytes()
        
        # Process the audio data
        # transcript = transcrip_audio(audio_data)
        # translated_text = transalte_to_eng(transcript)
        translated_text = end2end_translation(audio_data)
        synthesized_audio = convert_text_to_speech(translated_text)

        await websocket.send_text(translated_text)
        await websocket.send_bytes(synthesized_audio)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
