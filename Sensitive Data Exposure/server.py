from flask import Flask

app = Flask(__name__)

# This is insecure! Do not use in production!
api_key = "your_secret_api_key"

@app.route('/')
def home():
    return "Welcome to the API!"

@app.route('/data')
def fetch_data():
    if api_key == "your_secret_api_key":
        return "API key is valid. Here's your sensitive data."
    else:
        return "Invalid API key."

if __name__ == '__main__':
    app.run(debug=True)
