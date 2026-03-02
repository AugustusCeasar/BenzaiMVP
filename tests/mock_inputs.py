import pandas as pd
import numpy as np


class MockDataset:
    mock_names = ["dataset1", "dataset2", "dataset3"]
    mock_data = [pd.DataFrame({"A": np.array([1032, 4095]), "B": np.array([0.1, 0.6])}),
                 pd.DataFrame({"A": np.array([1237, 3456]), "C": np.array([1, 0])}),
                 pd.DataFrame({"A": np.array([5235, 9032]), "D": np.array([106, 94])})]
    dataset_dict: list[dict[str: str, str: str]]

    cannonical_schema_suggestion = "A B C D"
    # a consequence of our current handling is that spaces are now allowed in column names, might want to change

    cannonical_merge: pd.DataFrame

    def __init__(self):
        self.dataset_dict = [{"name": self.mock_names[i], "example": self.mock_data[i].to_string()}
                             for i in range(len(self.mock_names))]

        joint_dataset = self.mock_data[0]
        for dataset in self.mock_data[1:]:
            joint_dataset = joint_dataset.merge(dataset, how="outer")
        self.cannonical_merge = joint_dataset


def debug():
    mock = MockDataset()
    print(mock.dataset_dict)
    print(mock.cannonical_merge)


if __name__ == "__main__":
    debug()
