from random import sample

DEFAULT_SPEC_CHARS = ["!", "@", "#", "$", "%", "^", "&", "*"]


class SpecialCharGenerator:
    def __init__(self, characters: list[str] = DEFAULT_SPEC_CHARS) -> None:
        self.characters = characters

    def get_special_character(self):
        return sample(self.characters, 1)[0]
