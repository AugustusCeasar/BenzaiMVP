from flask import Flask


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "api is currently running"


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
