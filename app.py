from flask import Flask

from Views.parts.parts_view import parts
# from Views.parts.assemblies_view import assemblies

app = Flask(__name__)

app.register_blueprint(parts)
# app.register_blueprint(assemblies)

@app.route('/')
def hello():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
