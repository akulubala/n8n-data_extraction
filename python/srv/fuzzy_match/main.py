from run_match import run_match
from fastapi import FastAPI
from models.match_response import MatchResponse
from models.match_request import MatchRequest

app = FastAPI()


@app.post("/matching", response_model=None)
def matching(data: MatchRequest) -> MatchResponse:
    """
    Fuzzy match the original list of dictionaries with the source list of dictionaries.
    :param data: MatchRequest object containing the original list and source list
    :return: MatchResponse object containing the fuzzy match result and lower score result
    """
    return run_match(data.targets, data.choices)
