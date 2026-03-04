import requests


class PromptBuilder:
    fixed_text: str
    shot_separation_characters: str = ""
    final_text: str = ""


class SuggestSchemaPrompt(PromptBuilder):
    # TODO: this could use a second output that provides context for the schema choice
    shot_separation_characters = "--------"
    fixed_text = f"""{shot_separation_characters}
GOAL: Merge these 2 similar datasets
DATASET1NAME: Heart Rate Oscillations during Meditation
DATASET1EXAMPLE:
    col 1 col 2
row 1     0.5     0.1
row 2     0.6     0.2
DATASET2NAME: Pulse Amplitudes from electrodermal activity collected from healthy volunteer subjects at rest and under controlled sedation
DATSET2EXAMPLE:
    col 1 col 2 col3
row 1     0.1     0     0
row 2     0.7     0.8     1.1
SUGGESTED MERGED SCHEMA:
col1 col2 col3
{shot_separation_characters}
GOAL: Merge these 2 similar datasets
DATASET1NAME: Salzburg Intensive Care database (SICdb)
DATASTE1EXAMPLE:
    patientid heartrateavg
row 1     12312312     80
row 2     65473665     59
DATATSET2NAME: HiRID
DATASET2EXAMPLE:
    patientname heartratepeak
row 1     12312312     100
row 2     65473665     110
SUGGESTED MERGED SCHEMA:
patientid heartrateavg heartratepeak
{shot_separation_characters}
"""

    def __init__(self, goal: str, dataset_list: list[dict[str: str, str: str]]):
        self.final_text = self.fixed_text + f"GOAL: {goal}\n"
        for i, dataset in enumerate(dataset_list):
            self.final_text += f"DATASET{i}NAME: {dataset['name']}\nDATASTE{i}EXAMPLE: {dataset['example']}\n"
        self.final_text += "SUGGESTED MERGED SCHEMA:\n"



if __name__ == "__main__":
    req = requests.get("https://physionet.org/files/meditation/1.0.0/")
    print(req)
