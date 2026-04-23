# 🏥 MediPulse AI

**MediPulse AI** is a futuristic, full-stack emergency triage dashboard designed for rapid health analysis and medical navigation.

## 🚀 Key Features
* **FlashCheck AI:** Powered by the **Gemini API**, the system analyzes natural language symptom descriptions and classifies severity (Critical, Moderate, or Mild).
* **Adaptive UI:** The interface dynamically changes its color theme and "emergency state" based on the AI's diagnosis.
* **Zero-Cost Hospital Locator:** Integrated **GPS-linked map** using Leaflet.js and OpenStreetMap to find nearby medical facilities with no API fees.
* **Biometric HUD:** Real-time EKG wave animations and a simulated BPM monitor for a high-tech medical experience.

## 🛠 Tech Stack
* **Backend:** Python (Flask)
* **Intelligence:** **Gemini API** (Generative AI)
* **Frontend:** HTML5, CSS3, JavaScript (ES6+)
* **Mapping:** OpenStreetMap & Overpass API

## ⚙️ Quick Start
1. **Clone & Install:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/MediPulse-AI.git
   pip install flask google-generativeai
   ```
2. **Configure:** * Get your key from [Google AI Studio](https://aistudio.google.com/).
   * Add your **Gemini API Key** in `app.py`.
3. **Run:**
   ```bash
   python app.py
   ```

## 🎯 Social Impact
This tool focuses on **User Experience (UX)** and **Immediate Actionability**, providing users with instant severity analysis and clear directions to the nearest hospital when every second counts.
