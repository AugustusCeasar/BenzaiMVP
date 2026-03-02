import json

import requests
import pandas


def debug_suggestion():
    df1 = pandas.DataFrame(
        [[0.1, 0.2], [0.3, 0.4]],
        index=["row 1", "row 2"],
        columns=["col 1", "col 2"],
    )
    df2 = pandas.DataFrame(
        [[0.5, 0.6], [0.7, 0.8]],
        index=["a", "b"],
        columns=["c", "d"],
    )

    data = [
        {'datasetname': 'data one',
         'datasetexample': df1.to_string()
        },
        {'datasetname': 'data two',
         'datasetexample': df2.to_string()
        },
    ]

    response = requests.post("http://127.0.0.1:5000/schema_suggestion", json=data)
    print(response.status_code)
    print(response.json())


def main():
    debug_suggestion()


if __name__ == "__main__":
    main()


