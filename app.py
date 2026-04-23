import os
import json
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- AI CONFIGURATION ---
# Get your API Key from https://aistudio.google.com/
GEMINI_API_KEY = "AIzaSyB1D42eN1QKETyTuCVY5TGXYsmhq-lgr4c" 
genai.configure(api_key=GEMINI_API_KEY)

# Use gemini-1.5-flash for speed and lower latency
model = genai.GenerativeModel('gemini-2.5-flash')

@app.route('/')
def index():
    # Renders your kittu.html file
    return render_template('kittu.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.json
        user_input = data.get('symptoms', '')
        user_name = data.get('name', 'User')

        if not user_input:
            return jsonify({"error": "No symptoms provided"}), 400

        # This "System Prompt" forces the AI to behave like a triage engine
        # and strictly return JSON for your frontend to parse easily.
        prompt = f"""
        Act as a professional medical triage system. 
        Analyze these symptoms: "{user_input}" for the patient named "{user_name}".
        
        Return ONLY a JSON object with the following structure:
        {{
            "severity": "Critical", "Moderate", or "Mild",
            "class": "sev-critical", "sev-moderate", or "sev-mild",
            "title": "A short status title",
            "message": "A personalized message for {user_name}",
            "causes": "2-3 potential causes based on the input",
            "meds": "Generic medicine classes and a safety warning"
        }}
        Do not include any markdown formatting like ```json or text outside the brackets.
        """

        response = model.generate_content(prompt)
        
        # Clean the response text just in case Gemini adds markdown backticks
        clean_json = response.text.strip().replace('```json', '').replace('```', '')
        
        # Convert string to Python dictionary
        result_data = json.loads(clean_json)

        return jsonify(result_data)

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({
            "severity": "Unknown",
            "class": "sev-moderate",
            "title": "Analysis Error",
            "message": "The AI engine is currently busy. Please try again or seek professional help.",
            "causes": "Technical glitch.",
            "meds": "N/A"
        }), 500

if __name__ == '__main__':
    app.run(debug=True)