from bottle import Bottle, run

app = Bottle()


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8080)
