import json

from db import db
from flask import Flask

# define db filename
db_filename = "todo.db"
app = Flask(__name__)

# setup config
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_filename}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

# initialize app
db.init_app(app)
with app.app_context():
    db.create_all()


# generalized response formats
def success_response(data, code=200):
    return json.dumps({"success": True, "data": data}), code


def failure_response(message, code=404):
    return json.dumps({"success": False, "error": message}), code


# -- TASK ROUTES ------------------------------------------------------


@app.route("/")
@app.route("/tasks/")
def get_tasks():
    pass


@app.route("/tasks/", methods=["POST"])
def create_task():
    pass


@app.route("/tasks/<int:task_id>/")
def get_task(task_id):
    pass


@app.route("/tasks/<int:task_id>/", methods=["POST"])
def update_task(task_id):
    pass


@app.route("/tasks/<int:task_id>/", methods=["DELETE"])
def delete_task(task_id):
    pass


# -- SUBTASK ROUTES ---------------------------------------------------


@app.route("/tasks/<int:task_id>/subtasks/", methods=["POST"])
def create_subtask(task_id):
    pass


# -- CATEGORY ROUTES --------------------------------------------------


@app.route("/tasks/<int:task_id>/category/", methods=["POST"])
def assign_category(task_id):
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
