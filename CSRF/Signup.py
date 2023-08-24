from flask import Flask, render_template_string, request, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template_string('''
        <h1>Victim's Signup Server</h1>
        <form action="{{ url_for('perform_action') }}" method="POST">
            <input type="hidden" name="action" value="change_password">
            <button type="submit">Change Password</button>
        </form>
    ''')

@app.route('/perform_action', methods=['POST'])
def perform_action():
    action = request.form['action']
    # Perform the action (e.g., change password) here
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
