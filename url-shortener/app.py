import hashlib
import json
from flask import Flask, redirect, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

try:
    with open('urls.json', 'r') as file:
        urls = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    urls = {}

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        data = request.json
        url = data.get('url')
        if url is None:
            return {'error': 'No url provided'}, 400
        key = hashlib.sha256(url.encode()).hexdigest()[:10]
        urls[key] = url
        with open('urls.json', 'w') as file:
            json.dump(urls, file)
        return {'original_url': url, 'shortened_url': f'{request.host_url}{key}'}
    else:
        return 'URL shortener', 200

@app.route('/<key>')
def redirect_to_url(key):
    url = urls.get(key)
    if url is not None:
        return redirect(url)
    else:
        return "URL not found", 404
    
if __name__ == '__main__':
    app.run()