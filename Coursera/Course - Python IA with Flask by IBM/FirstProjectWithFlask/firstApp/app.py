from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello world</h1>"


if __name__ == '__main__':
    app.run('127.0.0.1', port=5555, debug=True)
