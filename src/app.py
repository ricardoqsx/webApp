from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/add')
def add():
    return 'add contact'

@app.route('/del')
def delete():
    return 'delete contact'

@app.route('/edit')
def edit():
    return 'edit contact'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=80, debug = True)