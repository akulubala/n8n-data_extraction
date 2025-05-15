from pydantic import BaseModel
from typing import Optional, Dict, Any

class MatchRequest(BaseModel):
    targets: list[dict]
    choices: list[dict]