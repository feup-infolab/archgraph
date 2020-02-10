from flask import Flask


app = Flask(__name__)


@app.route("/create")
def create():
    return "create"


@app.route("/<uid>/update")
def update(uid):
    return "update %s" % uid


@app.route("/<uid>/delete")
def delete(uid):
    return "delete %s" % uid


@app.route("/<uid>")
def view(uid):
    return "view %s" % uid


if __name__ == "__main__":
    app.run()
