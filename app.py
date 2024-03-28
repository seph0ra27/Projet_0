from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Configuration key
openai.api_key = 'CLE_API_OPENAI'

# chemin home
@app.route('/')
def home():
    return render_template('index.html')

# chemin messages
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_message']

    # OpenAI gpt-3.5 réponse
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_message,
        max_tokens=100
    )

    return jsonify({'response': response.choices[0].text.strip()})

if __name__ == '__main__':
    app.run(debug=True)

