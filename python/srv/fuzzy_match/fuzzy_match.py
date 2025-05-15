from thefuzz import fuzz

def fuzzy_match(original: list[dict[str, str]], source: list[dict[str, str]]) -> list[dict[str, str]]:

    word1 = "Apple MacBook Air M2"
    word2 = "mac air laptop"
    similarity = fuzz.ratio(word1.lower(), word2.lower())

    return similarity
