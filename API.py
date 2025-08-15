import cv2
from ultralytics import YOLO
import requests

BOT_TOKEN = "8482668051:AAEkFa3c0-GT0yS0oZ3Jb9BGDUOQyVlRvSw"
CHAT_ID = "1277089214"  

def send_telegram_photo(image):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    _, buffer = cv2.imencode(".jpg", image)
    files = {"photo": ("image.jpg", buffer.tobytes())}
    data = {"chat_id": CHAT_ID, "caption": "⚠ Weapon detected!"}
    requests.post(url, data=data, files=files)

###############################################################################
cap = cv2.VideoCapture(0) # Your laptop camera
###############################################################################
rtsp_url = "rtsp://username:password@ip:port/live" # your sesurveillance camera
cap = cv2.VideoCapture(rtsp_url, cv2.CAP_FFMPEG)
###############################################################################

model = YOLO("E:/Weabon detection/best.pt")
weapon_detected = False

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to read camera feed")
        continue 

    results = model(frame, conf=0.5)
    detected_weapon_now = False

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            class_name = model.names[cls_id]
            conf_score = float(box.conf[0])

            if class_name.lower() == "weapon" and conf_score >= 0.5:
                detected_weapon_now = True
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.putText(frame, f"{class_name} {conf_score:.2f}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

                if not weapon_detected:
                    send_telegram_photo(frame)
                    weapon_detected = True

    if not detected_weapon_now:
        weapon_detected = False

    cv2.imshow("Camera Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
