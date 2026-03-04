from flask import Flask, abort, request, jsonify

from backend.inference import inference_datasetexaple_to_schema_suggestion

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "api is currently running"


@app.route("/schema_suggestion", methods=["POST"])
def inference_schema_suggestion_endpoint():
    json_input = request.get_json()
    if json_input is None or "dataset_list" not in json_input:
        abort(400, "Required format is: {'dataset_list': [ {'datasetname': <String>, "
                   "'datasetexample': <any format valid for entry into pandas.read_json>}, ... (max 10 entries)] }")

    dataset_examples = json_input["dataset_list"]

    suggestion = inference_datasetexaple_to_schema_suggestion("Merge these 2 similar datasets", dataset_examples)

    return jsonify({"suggestion": suggestion})


@app.route("/transformation_code", methods=["POST"])
def inference_transformation_code_endpoint():
    return "not implemented", 500


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
