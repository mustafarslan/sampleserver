from flask import Flask
from blueprints.user import user

app = Flask(__name__)

app.register_blueprint(user)


if __name__ == "__main__":
    app.run()