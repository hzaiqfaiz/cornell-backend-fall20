import json

from db import db
from flask import Flask

db_filename = "auth.db"
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.create_all()


def extract_token(request):
    pass


@app.route("/")
def hello_world():
    return json.dumps({"message": "Hello, World!"})


@app.route("/register/", methods=["POST"])
def register_account():
    pass


@app.route("/login/", methods=["POST"])
def login():
    pass


@app.route("/session/", methods=["POST"])
def update_session():
    pass


@app.route("/secret/", methods=["GET"])
def secret_message():
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
