import json

from sentence_transformers import SentenceTransformer

import numpy as np
import faiss

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


index_singleton = None


def get_semantic_index(embedding_data, singleton_refresh=False):
    global index_singleton
    if index_singleton is None or singleton_refresh:
        index_singleton = faiss.IndexFlatL2(len(embedding_data[0]["embedding"]))

        for item in embedding_data:
            index_singleton.add(np.array([item["embedding"]]))

    return index_singleton


def get_k_nearest_neighbors(query, semantic_index, k=5, model_name=None):
    model = SentenceTransformer(model_name or DEFAULT_SENCENCE_ENCODING_MODEL)

    query_embeddings = model.encode_query(query)

    distance, indices = semantic_index.search(np.expand_dims(query_embeddings, axis=0), k=k)

    return distance, indices


def debug():
    embeddings_direct = get_embeddings(save_fn="data/name_encoding.json")
    print(embeddings_direct)
    embeddings_loaded = load_data("data/name_encoding.json")
    print(embeddings_loaded)
    test_index = get_semantic_index(embeddings_direct)
    D, I = get_k_nearest_neighbors(query="my research goal is to study heartrate variations in icu patients",
                                   semantic_index=test_index)
    print(D)
    print(I)


if __name__ == "__main__":
    debug()
