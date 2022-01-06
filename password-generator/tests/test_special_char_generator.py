import unittest

from lib.generators import DEFAULT_SPEC_CHARS, SpecialCharGenerator


class TestSpecialCharGenerator(unittest.TestCase):
    """Test SpecialCharGenerator"""

    def test_get_special_character_from_default_list(self):
        """Test returns char in default list"""
        result = SpecialCharGenerator().get_special_character()
        self.assertIn(result, DEFAULT_SPEC_CHARS)

    def test_get_special_character_from_param_list(self):
        """Test returns char from passed in list"""
        chars = ["@", "#", "$"]
        result = SpecialCharGenerator(chars).get_special_character()
        self.assertIn(result, chars)


if __name__ == "__main__":
    unittest.main()
