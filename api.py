from flask import Flask

from Views.view_assemblies import assemblies
from Views.view_parts import parts
from Views.view_products import products

app = Flask(__name__)

app.register_blueprint(parts)
app.register_blueprint(assemblies)
app.register_blueprint(products)

@app.route('/')
def hello():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
