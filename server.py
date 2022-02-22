from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/repeat/<num>/times')
def repeat(num):
    return 'Hello' * int(num)

@app.route('/michael/jordan')
def mj():
    return 'Hello MJ'

@app.route('/free')
def free():
    return 'Hello free'

if __name__=='__main__':
    app.run(debug=True)