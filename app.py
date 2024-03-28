from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Configure OpenAI API
openai.api_key = 'VOTRE_CLE_API_OPENAI'

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for receiving messages and generating responses
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_message']

    # Call OpenAI GPT-3.5 API to generate response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_message,
        max_tokens=100
    )

    return jsonify({'response': response.choices[0].text.strip()})

if __name__ == '__main__':
    app.run(debug=True)

