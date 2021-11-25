import requests

NAMES_URL = 'https://randomuser.me/api/?nat=us&inc=name&noinfo'

class NameGenerator():
    """ A class for generationg names """

    num_names = 10

    def __init__(self, min: int, max: int) -> None:
        self.min = min
        self.max = max

    def _validate_length(self, name: str) -> bool:
        return (len(name) >= self.min and len(name) <= self.max)

    def _fetch_names(self) -> list[str]:
        resp = requests.get(f'{NAMES_URL }&results={self.num_names}').json()
        # TODO: Add error handling for failed calls 
        return [name['name']['first'] for name in resp['results']]

    def get_name(self) -> str:
        valid_names = list(filter(self._validate_length, self._fetch_names()))
        while len(valid_names) == 0 :
            valid_names = list(filter(self._validate_length, self._fetch_names()))

        return valid_names[0].capitalize()
