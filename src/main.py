from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Kevin Baskin!'
@app.route('/clgi')
    return 'go to clgi.org'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
