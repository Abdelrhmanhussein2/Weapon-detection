# 🔫 Weapon Detection System using Computer Vision & Deep Learning  

## 📌 Project Overview  
This project implements a **real-time weapon detection system** using **Computer Vision** and **Deep Learning**.  
The system monitors a CCTV camera feed, detects weapons, and instantly sends alerts with snapshots to the user via a **Telegram Bot**.  
The goal is to explore AI applications in **safety & security**.  

---

## ✨ Features  
- 🎥 Real-time detection from surveillance cameras  
- 📩 Instant notifications with snapshots through **Telegram**  
- 🔍 Multiple deep learning models tested for accuracy and speed  
- 🧹 Preprocessing pipeline for better data quality  

---

## 🛠 Tech Stack  
- **Python**  
- **OpenCV** – Video capture & preprocessing  
- **YOLO / CNN Models** – Object detection  
- **Telegram Bot API** – Instant alerts  

---

## 🧪 Preprocessing Techniques  
To improve detection accuracy, several preprocessing steps were applied:  
- ⚡ **CLAHE**: Enhanced contrast in low-light images  
- 🗑️ **Data Cleaning**: Removed irrelevant / corrupted samples  
- 🌫️ **Blurring**: Reduced noise and stabilized frames  

---

## 🚀 How It Works  
1. **Camera** → Capture frames in real-time  
2. **Detection** → Run object detection model (YOLO/CNN)  
3. **Alert** → Generate weapon alert if detected  
4. **Telegram Bot** → Send snapshot & alert to the user  

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

