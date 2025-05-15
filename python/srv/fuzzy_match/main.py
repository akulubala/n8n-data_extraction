from fuzzy_match import fuzzy_match
from fastapi import FastAPI

app = FastAPI()


@app.post("/matching")
def matching(original:list[dict[str, str]], source: list[dict[str, str]]):
    """
    Fuzzy match the original list of dictionaries with the source list of dictionaries.
    :param original: The original list of dictionaries.
    :param source: The source list of dictionaries.
    :return: A list of dictionaries with the fuzzy matched results.
    """
    return fuzzy_match(original, source)
