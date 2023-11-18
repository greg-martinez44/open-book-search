"""Page object to represent return from web request"""
from typing import Optional

class Page:

    def __init__(self, body: Optional[str] = None) -> None:
        self._body = body
