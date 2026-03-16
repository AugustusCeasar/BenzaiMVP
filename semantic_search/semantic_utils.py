import json

from sentence_transformers import SentenceTransformer

DEFAULT_SENCENCE_ENCODING_MODEL = "sentence-transformers/embeddinggemma-300m-medical"


def get_embeddings(in_fn="data/dataset_names.txt", save_fn=None, model_name=None):
    model = SentenceTransformer(model_name or DEFAULT_SENCENCE_ENCODING_MODEL)

    lines = []
    with open(in_fn) as f:
        while len(lines) == 0 or lines[-1]:
            lines.append(f.readline())

    query_embeddings = model.encode_query(lines[:-1])

    json_data = []
    for i in range(len(query_embeddings)):
        split_dataset_text = lines[i].split(":", 1)
        name = split_dataset_text[0]
        description = split_dataset_text[1] if len(split_dataset_text) > 1 else ""
        json_data.append({"name": name, "description": description, "embedding": query_embeddings[i].tolist()})

    if save_fn:
        with open(save_fn, 'w') as f:
            json.dump(json_data, f)

    return json_data


def load_data(fn):
    with open(fn, "r") as f:
        data = json.load(f)
    return data


def debug():
    embeddings_direct = get_embeddings(save_fn="data/name_encoding.json")
    print(embeddings_direct)
    embeddings_loaded = load_data("data/name_encoding.json")
    print(embeddings_loaded)


if __name__ == "__main__":
    debug()
