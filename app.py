from flask import Flask, url_for
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/about')
def about(num):
    return 'about {}'.format(num)

with app.test_request_context():
    print(url_for('hello_world'))
    print(url_for('about'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)), debug=True)

