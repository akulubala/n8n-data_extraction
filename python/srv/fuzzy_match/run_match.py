import json
from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('distiluse-base-multilingual-cased-v1')


def run_match(targets: list[dict], choices: list[dict]) -> dict:
    result = []
    notifications_check_list = []
    for i, target in enumerate(targets):
        
        target_embedding = model.encode(
            target['product'], convert_to_tensor=True)
        
        choice_names = [choice['品名'] for choice in choices]
        choices_embeddings = model.encode(choice_names, convert_to_tensor=True)

        similarities = util.pytorch_cos_sim(
            target_embedding, choices_embeddings)

        best_index = similarities.argmax().item()
        best_match = choices[best_index]
        result.append({
            "product_id": best_match['品號'],
            "matched_name": best_match['品名'],
            'original_input': target['product'],
            'quantity': target['quantity'],
            'match_score': f"{similarities[0][best_index].item():.4f}",
        })
        if similarities[0][best_index].item() < 0.5:
            notifications_check_list.append({
                "product_id": best_match['品號'],
                "matched_name": best_match['品名'],
                'original_input': target['product'],
                'quantity': target['quantity'],
                'match_score': f"{similarities[0][best_index].item():.4f}",
            })
    return {
        "fuzzy_match_result": result,
        "lower_score_result": notifications_check_list
    }
