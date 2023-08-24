from flask import Flask, request

app = Flask(__name__)

@app.route('/attack', methods=['GET'])
def attack():
    return f"Attacker's server triggered action: {request.args.get('action')}"

if __name__ == '__main__':
    app.run(debug=True, port=5001)
