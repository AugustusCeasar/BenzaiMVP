from typing import Tuple, List

from backend.system_prompts import SuggestSchemaPrompt
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

DEFAULT_MODEL = "EleutherAI/pile-t5-xxl"


def inference_datasetexaple_to_schema_suggestion(goal: str, dataset_list: list[dict[str: str, str: str]]) -> str:
    prompt = SuggestSchemaPrompt(goal, dataset_list)
    # print(prompt.final_text)

    output, _ = inference_generic(prompt.final_text)

    return truncate_to_end_of_shot(output, prompt.shot_separation_characters)


def inference_generic(prompt: str, model_path: str = None) -> Tuple[str, List[int]]:
    if not model_path:
        model_path = DEFAULT_MODEL

    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

    inputs = tokenizer(prompt, return_tensors="pt")
    inputs = inputs.to(model.device)

    generated_ids = model.generate(**inputs, max_new_tokens=256, do_sample=False)
    output_text = tokenizer.decode(generated_ids[0])
    return output_text, generated_ids


def truncate_to_end_of_shot(text: str, shot_separation_characters: str):
    return text.split(shot_separation_characters, 1)[0]


def debug_inference():
    suggestion = inference_datasetexaple_to_schema_suggestion(
        "Merge these 2 similar datasets",
        [{"name": "a", "example": "nothing at all"},
         {"name": "b", "example": "something but not much"}])
    print(suggestion)


if __name__ == "__main__":
    debug_inference()
