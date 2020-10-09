from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'cake shop api 1.0'


if __name__ == '__main__':
    app.debug = True
    app.run()
