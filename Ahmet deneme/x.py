import speech_recognition as sr
import pyttsx3
import requests

# Rasa bot API URL
RASA_API_URL = "http://localhost:5005/webhooks/rest/webhook"

# Sesli yanıt motoru
engine = pyttsx3.init()

# Ses kaydı alma fonksiyonu
def ses_kaydi():
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Konuşabilirsiniz...")
        recognizer.adjust_for_ambient_noise(mic)
        try:
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio, language="tr-TR")
            print("Siz:", text)
            return text
        except sr.UnknownValueError:
            print("Ses anlaşılamadı.")
            return None
        except sr.RequestError:
            print("Ses tanıma servisi çalışmıyor.")
            return None

# Yanıt alma fonksiyonu
def bot_cevap(text):
    response = requests.post(RASA_API_URL, json={"message": text})
    response_json = response.json()
    if response_json:
        return response_json[0]['text']
    return "Üzgünüm, bir şeyler yanlış gitti."

# Yanıtı sesli olarak söyleme fonksiyonu
def sesli_cevap(metin):
    engine.say(metin)
    engine.runAndWait()

# Ana döngü
while True:
    kullanici_ses = ses_kaydi()
    if kullanici_ses:
        cevap = bot_cevap(kullanici_ses)
        print("Yapay Zeka:", cevap)
        sesli_cevap(cevap)
