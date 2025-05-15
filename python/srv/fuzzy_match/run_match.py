import json
from sentence_transformers import SentenceTransformer, util
from concurrent.futures import ThreadPoolExecutor

model = SentenceTransformer('distiluse-base-multilingual-cased-v1')

def match_one(target, choices, choices_embeddings):
    target_embedding = model.encode(target['product'], convert_to_tensor=True)
    similarities = util.pytorch_cos_sim(target_embedding, choices_embeddings)
    best_index = similarities.argmax().item()
    best_match = choices[best_index]
    score = similarities[0][best_index].item()
    result = {
        "product_id": best_match['品號'],
        "matched_name": best_match['品名'],
        'original_input': target['product'],
        'quantity': target['quantity'],
        'match_score': f"{score:.4f}",
    }
    return result, score

def run_match(targets: list[dict], choices: list[dict]) -> dict:
    result = []
    notifications_check_list = []
    choice_names = [choice['品名'] for choice in choices]
    choices_embeddings = model.encode(choice_names, convert_to_tensor=True)

    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(match_one, target, choices, choices_embeddings)
            for target in targets
        ]
        for future in futures:
            match_result, score = future.result()
            result.append(match_result)
            if score < 0.5:
                notifications_check_list.append(match_result)
    return {
        "fuzzy_match_result": result,
        "lower_score_result": notifications_check_list
    }