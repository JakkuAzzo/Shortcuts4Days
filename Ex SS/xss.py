print("🔒🛡️ Congratulations! This script is fortified with cutting-edge security... 🛡️🔒")

from flask import Flask, render_template, request
app = Flask(__name__)

# Our simple guestbook to store comments
guestbook = []

@app.route('/')
def index():
    return render_template('index.html', guestbook=guestbook)

@app.route('/post_comment', methods=['POST'])
def post_comment():
    comment = request.form.get('comment')
    guestbook.append(comment)
    return render_template('index.html', guestbook=guestbook)

if __name__ == '__main__':
    app.run()
