from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    a = 12
    b = 2231
    c = a + b
    return str(c)


if __name__ == "__main__":
    app.run(
        debug=True,
        host='0.0.0.0',
        port=3031
    )