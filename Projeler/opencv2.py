import cv2
import torch
import time
import os
from gtts import gTTS
from ultralytics import YOLO

# YOLO modelini yükle (pre-trained COCO modeli kullanıyoruz)
model = YOLO("yolov8n.pt")  # YOLOv8 nano modeli

# Sesli çıktı fonksiyonu
def speak(text):
    tts = gTTS(text=text, lang='tr')
    filename = "output.mp3"
    tts.save(filename)
    os.system(f"mpg321 {filename}")  # Raspberry Pi için uygun ses oynatıcı

# Kamera başlat
cap = cv2.VideoCapture(0)

# Nesnelerin son duyurulma zamanını takip et
last_speak_time = {}
SPEAK_DELAY = 3  # Aynı nesne için tekrar bildirim süresi (saniye)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Model ile nesne tespiti yap
    results = model(frame)
    detected_objects = set()
    
    for result in results:
        for box in result.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            detected_objects.add(label)
    
    # Sesli bildirim
    current_time = time.time()
    for obj in detected_objects:
        if obj not in last_speak_time or (current_time - last_speak_time[obj]) > SPEAK_DELAY:
            speak(f"{obj} tespit edildi.")
            last_speak_time[obj] = current_time
    
    # Görüntüyü göster
    cv2.imshow("Smart Glasses Vision", frame)
    
    # Çıkış için 'q' tuşuna bas
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()