from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_URL = 'https://api-inference.huggingface.co/models/gpt2'
API_TOKEN = 'your_huggingface_api_token'

headers = {
    'Authorization': f'Bearer {API_TOKEN}'
}

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

    if response.status_code != 200:
        return jsonify({'error': 'Failed to generate text'}), response.status_code

    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
