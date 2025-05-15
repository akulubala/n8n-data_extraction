from pydantic import BaseModel
from typing import Optional, Dict, Any

class MatchResponse(BaseModel):
    fuzzy_match_list: list[dict]
    lower_score_list: list[dict]