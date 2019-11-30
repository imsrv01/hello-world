from flask import Flask, url_for, session, redirect, request, escape, render_template
from flask_jsonpify import jsonify
import os, requests, json
app = Flask(__name__)

@app.route('/bb')
def hello_world():
    return 'Hello, World!'

@app.route('/about')
def about(num):
    return 'about {}'.format(num)

@app.route('/names')
def names():
    return jsonify(name="a", lastname="b")

@app.route('/test')
def test():
    response = requests.get('https://kubed-ixrvw4olfa-ue.a.run.app/status')
    print('API resonse - ', response)
    #print(response.text)
    status = response.json()['status']
    #status = 'hello'
    return 'service completed with status {}'.format(status)

@app.route('/display')
def display():
    response = requests.get("http://127.0.0.1:8080/names")
    response = response.json()
    name = response['name']
    #response = json.loads(response)
    return render_template('index.html', name=name)

@app.route('/show')
def show():
    response = json.loads(display())
    #response = tuple([{"name":"aa"}, {"name":"bb"}])
    #response=["Pikachu", "Charizard", "Squirtle", "Jigglypuff",  "Bulbasaur", "Gengar", "Charmander", "Mew", "Lugia", "Gyarados"] 
    return render_template('index.html', len=len(response), response = response)

with app.test_request_context():
    print(url_for('hello_world'))
    print(url_for('about'))


app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)), debug=True)

