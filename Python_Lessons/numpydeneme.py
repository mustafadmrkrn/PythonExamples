import wave
import numpy as np
import pyttsx3
import deepspeech
import asyncio
import torch
from transformers import AlbertForQuestionAnswering, AlbertTokenizer
from rasa.core.agent import Agent

# DeepSpeech Model Yolu
DS_MODEL = "deepspeech-0.9.3-models.pbmm"
DS_SCORER = "deepspeech-0.9.3-models.scorer"

# ALBERT Modeli
tokenizer = AlbertTokenizer.from_pretrained("albert-base-v2")
albert_model = AlbertForQuestionAnswering.from_pretrained("albert-base-v2")

# pyttsx3 Sesli Yanıt
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# DeepSpeech: Sesi yazıya çevir
def transcribe_audio(audio_path):
    model = deepspeech.Model(DS_MODEL)
    model.enableExternalScorer(DS_SCORER)

    with wave.open(audio_path, 'rb') as wf:
        frames = wf.readframes(wf.getnframes())
        audio = np.frombuffer(frames, dtype=np.int16)
        result = model.stt(audio)
        return result

# ALBERT ile yanıt üret (örnek amaçlı basit context ile)
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
    agent = Agent.load("models/")  # Eğitilmiş RASA modeli gerektirir
    responses = await agent.handle_text(text)
    return responses[0]['text'] if responses else "Anlayamadım."

# Ana fonksiyon
def run_assistant(audio_path):
    print("Sesi metne çeviriyor...")
    user_input = transcribe_audio(audio_path)
    print(f"Kullanıcı dedi ki: {user_input}")

    # Önce RASA ile deneyelim
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

# Örnek test
if _name_ == "_main_":
    run_assistant("test.wav")  # test.wav = kullanıcının sesi