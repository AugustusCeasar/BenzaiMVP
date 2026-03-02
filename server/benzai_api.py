from flask import Flask, abort

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "api is currently running"


@app.route("/schema_suggestion", methods=["POST"])
def inference_schema_suggestion_endpoint():
    return "not implemented", 500


@app.route("/transformation_code", methods=["POST"])
def inference_transformation_code_endpoint():
    return "not implemented", 500


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
