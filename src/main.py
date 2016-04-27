from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Ok now let us get the stock ticker working!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
