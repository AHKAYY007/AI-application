import openai
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Set OpenAI API Key
openai.api_key = ""

# Define chatbot route
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Generate response using OpenAI GPT
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",   # Use "gpt-3.5-turbo" for lower-cost options
            messages=[
                {"role": "system", "content": "You are an HR assistant. Help employees with HR-related queries."},
                {"role": "user", "content": user_input},
            ],
        )
        # Extract and return the response
        chatbot_reply = response['choices'][0]['message']['content']
        return jsonify({"response": chatbot_reply})

    except openai.error.OpenAIError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
