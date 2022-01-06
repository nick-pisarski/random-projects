import logging
from os import path

import requests

log = logging.getLogger(path.basename(__file__))
NAMES_URL = "https://randomuser.me/api/?nat=us&inc=name&noinfo"


class NameGenerator:
    """A class for generationg names"""

    num_names = 50

    def __init__(self, min: int, max: int) -> None:
        self.min = min
        self.max = max

    def _validate_length(self, name: str) -> bool:
        return len(name) >= self.min and len(name) <= self.max

    def _fetch_names(self) -> list[str]:
        log.info(f"calling {NAMES_URL}")
        try:
            resp = requests.get(f"{NAMES_URL }&results={self.num_names}").json()
        except:
            log.exception(f"Failed to call {NAMES_URL}")
            raise Exception("Names call failed")

        return [name["name"]["first"] for name in resp["results"]]

    def get_names(self, name_count: int = 5) -> list[str]:
        valid_names = list(filter(self._validate_length, self._fetch_names()))
        while len(valid_names) < name_count:
            valid_names = list(filter(self._validate_length, self._fetch_names()))

        return [name.capitalize() for name in valid_names][:name_count]
