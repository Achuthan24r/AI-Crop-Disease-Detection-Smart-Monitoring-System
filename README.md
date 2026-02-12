Project Structure
AI-Crop-System/
│
├── app.py                # Flask AI backend
├── crop_model.h5         # Trained TensorFlow model
├── dashboard.html        # Web dashboard
├── esp32_code.ino        # Sensor automation code
├── requirements.txt
└── README.md

⚙ Installation Guide
1️⃣ Clone the Repository
git clone https://github.com/yourusername/AI-Crop-System.git
cd AI-Crop-System

2️⃣ Install Dependencies
pip install tensorflow flask numpy pillow


Or create a requirements.txt:

tensorflow
flask
numpy
pillow


Then run:

pip install -r requirements.txt

3️⃣ Run the AI Backend
python app.py


Server runs on:

http://localhost:5000

4️⃣ Open Dashboard

Open:

dashboard.html


Upload a leaf image → Click Detect → View result.

🔌 ESP32 Smart Irrigation Code

Upload the provided esp32_code.ino to your ESP32 board using Arduino IDE.

Soil moisture is monitored and:

Pump turns ON if soil is dry

Pump turns OFF if soil is wet

🧠 AI Model Information

The model classifies:

Healthy Leaf

Leaf Spot

Rust

Blight

Input Size: 224x224
Framework: TensorFlow / Keras

You can train the model using:

Teachable Machine

PlantVillage Dataset

Custom Dataset

📈 Future Improvements

📱 Android App Integration

☁ Cloud Hosting (AWS / Firebase)

📊 Farmer Analytics Dashboard

📍 GPS-based Field Monitoring

📩 SMS Alerts

🛰 Drone Image Integration

🎯 Applications

Smart Farming

Agricultural Research

AgriTech Startups

Final Year Engineering Project

Hackathons

🏆 Why This Project is Powerful

✅ Combines AI + IoT
✅ Real-world impact
✅ Startup scalable
✅ Full-stack integration
✅ Industry-ready concept

👨‍💻 Developed By

Achuthan Rameshkumar
Full Stack & IoT Developer
Smart Agriculture Innovator 🌾# AI-Crop-Disease-Detection-Smart-Monitoring-System
