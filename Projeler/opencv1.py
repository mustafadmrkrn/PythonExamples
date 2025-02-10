import cv2
import numpy as np
import time
import pyttsx3

# Nesne tanıma için model ve ağırlık dosyaları
prototxt_path = "MobileNetSSD_deploy.prototxt"
caffemodel_path = "MobileNetSSD_deploy.caffemodel"

# OpenCV'nin hazır nesne tanıma modelini yükleyelim
net = cv2.dnn.readNetFromCaffe(prototxt_path, caffemodel_path)

# Nesne isimleri
CLASSES = ["background", "airplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]

# Sesli okuma motoru
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Kamerayı aç
cap = cv2.VideoCapture(0)
last_speech_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            idx = int(detections[0, 0, i, 1])
            label = CLASSES[idx]
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
            cv2.putText(frame, label, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            
            if time.time() - last_speech_time > 2:
                speak(label)
                last_speech_time = time.time()
    
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
