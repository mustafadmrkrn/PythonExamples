import whisper
import pyttsx3
import asyncio
import torch
from transformers import AlbertForQuestionAnswering, AlbertTokenizer
from rasa.core.agent import Agent

# Whisper modeli yükleniyor
whisper_model = whisper.load_model("base")

# ALBERT modeli
tokenizer = AlbertTokenizer.from_pretrained("albert-base-v2")
albert_model = AlbertForQuestionAnswering.from_pretrained("albert-base-v2")

# pyttsx3: Sesli yanıt verme
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Whisper: Sesi metne çevir
def transcribe_audio(audio_path):
    result = whisper_model.transcribe(audio_path, language="tr")
    return result["text"]

# ALBERT ile yanıt üret (örnek context ile)
def albert_answer(question, context="Bu sistem yapay zeka destekli bir asistandır."):
    inputs = tokenizer(question, context, return_tensors="pt")
    outputs = albert_model(**inputs)
    start_idx = torch.argmax(outputs.start_logits)
    end_idx = torch.argmax(outputs.end_logits) + 1
    tokens = inputs["input_ids"][0][start_idx:end_idx]
    answer = tokenizer.decode(tokens)
    return answer

# RASA: Diyalog yönetimi
async def rasa_response(text):
    agent = Agent.load("models/")  # Eğitilmiş bir RASA modeli gerektirir
    responses = await agent.handle_text(text)
    return responses[0]['text'] if responses else "Anlayamadım."

# Ana asistan fonksiyonu
def run_assistant(audio_path):
    print("Sesi metne çeviriyor...")
    user_input = transcribe_audio(audio_path)
    print(f"Kullanıcı dedi ki: {user_input}")

    try:
        rasa_reply = asyncio.run(rasa_response(user_input))
    except:
        rasa_reply = None

    if not rasa_reply or rasa_reply == "Anlayamadım.":
        print("RASA yanıt veremedi, ALBERT ile devam ediliyor...")
        response = albert_answer(user_input)
    else:
        response = rasa_reply

    print("Asistan:", response)
    speak(response)

# Test
if __name__ == "__main__":
    run_assistant("test.wav")
