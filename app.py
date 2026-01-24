from flask import Flask
from controllers.create import create
from controllers.read import read
from controllers.update import update
from controllers.delete import delete

app = Flask(__name__)

app.register_blueprint(create)
app.register_blueprint(read)
app.register_blueprint(update)
app.register_blueprint(delete)


if __name__=='__main__':
    app.run(debug=True)