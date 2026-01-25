from flask import Flask
from controllers.create import create
from controllers.read import read
from controllers.update import update
from controllers.delete import delete
import os

app = Flask(__name__)

app.register_blueprint(create)
app.register_blueprint(read)
app.register_blueprint(update)
app.register_blueprint(delete)


if __name__=='__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=False)