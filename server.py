from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend

OPENAI_API_KEY = "your_openai_api_key"  # Replace with actual API key
openai.api_key = OPENAI_API_KEY

@app.route("/", methods=["GET"])
def home():
    return "Flask server is running!"

@app.route("/api/recommend", methods=["POST"])
def recommend():
    try:
        data = request.get_json()
        print("📥 Received data:", data)

        if not data or "interest" not in data:
            return jsonify({"error": "❌ Missing 'interest' field"}), 400

        interest = data["interest"].strip()
        print("🔍 Interest received:", interest)

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": f"Give personalized skill development recommendations for {interest}"}]
        )

        recommendations = response["choices"][0]["message"]["content"]
        print("✅ Recommendations:", recommendations)

        return jsonify({"recommendations": recommendations})

    except openai.error.OpenAIError as e:
        print("❌ OpenAI API Error:", str(e))
        return jsonify({"error": "OpenAI API error. Check API key and quota."}), 500

    except Exception as e:
        print("❌ Server error:", str(e))
        return jsonify({"error": f"Internal Server Error: {str(e)}"}), 500

if __name__ == "__main__":
    print("🚀 Flask server starting...")
    app.run(debug=True, host="127.0.0.1", port=5000)
