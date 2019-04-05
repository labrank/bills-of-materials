from flask import Flask

from Views.parts.parts_view import parts

app = Flask(__name__)

app.register_blueprint(parts)

@app.route('/')
def hello():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
