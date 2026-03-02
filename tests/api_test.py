from backend.utils import separate_suggestion_into_column_list

import pytest
from tests.mock_inputs import MockDataset
from pytest_custom_outputs import c_assert


SKIP_TIME_INTENSIVE_TESTS = False


def test_api_live(client):
    response = client.get("/")
    assert response.status_code == 200


def test_schema_suggestion_endpoint_format(client):
    if SKIP_TIME_INTENSIVE_TESTS:
        pytest.skip("Skipping time intensive tests")
    mock = MockDataset()
    response = client.post("/schema_suggestion", json={"dataset_list": mock.dataset_dict})
    assert response.status_code == 200 and response

    response_json = response.get_json()
    assert "suggestion" in response_json

    suggestion = response_json["suggestion"]
    recieved_columns = separate_suggestion_into_column_list(suggestion)
    cannonical_columns = separate_suggestion_into_column_list(mock.cannonical_schema_suggestion)
    if len(recieved_columns) != len(cannonical_columns):
        c_assert("low_grade", f"current model suggested {len(recieved_columns)} columns, "
                              f"ideal would have been {len(cannonical_columns)}")
    else:
        c_assert("acceptable_grade")


def test_transformation_code(client):
    if SKIP_TIME_INTENSIVE_TESTS:
        pytest.skip("Skipping time intensive tests")
    mock = MockDataset()

    response = client.post("/transformation_code", json={"dataset_list": mock.dataset_dict,
                                                         "suggestion": mock.cannonical_schema_suggestion})
    assert response.status_code == 200

    response_json = response.get_json()
    assert response_json is not None
    assert "column_new_names" in response_json
    assert "deleted_columns" in response_json
    c_assert("unrefined_test", "this response will be expected to have more fields as development continues, "
                               "current tests only cover column renaming and deleting")

    # validity test
    modified_dataframes = []
    for i, original_dataframe in enumerate(mock.mock_data):
        c_df = original_dataframe

        if mock.mock_names[i] in response_json["deleted_columns"] \
                and len(response_json["deleted_columns"][mock.mock_names[i]])>0:
            c_deleted_columns = response_json["deleted_columns"][mock.mock_names[i]]
            c_df = c_df.drop(columns=c_deleted_columns)

        if mock.mock_names[i] in response_json["column_new_names"] \
                and len(response_json["column_new_names"][mock.mock_names[i]]) > 0:
            c_new_column_names = response_json["column_new_names"][mock.mock_names[i]]
            c_df = c_df.rename(c_new_column_names)

        modified_dataframes.append(c_df)

    final_df = modified_dataframes[0]
    for df in modified_dataframes[1:]:
        final_df = final_df.merge(df, how="outer")

    if final_df.shape != mock.cannonical_merge.shape:
        c_assert("low_grade", f"Suggested code transformation has different output shape than expected. "
                              f"Got {final_df.shape}, wanted {mock.cannonical_merge.shape}."
                              f"\nOutput data: {final_df.to_string()}")
    else:
        c_assert("acceptable_grade")




