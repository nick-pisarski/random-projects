import unittest

from lib.generators.num_str_generator import NumberStringGenerator


class TestNumberStringGenerator(unittest.TestCase):
    """Tests NumberStringGenerator"""

    def setUp(self):
        self.generator = NumberStringGenerator()

    def test_get_num_str(self):
        """Test get_number_str"""
        for l in range(0, 10):
            with self.subTest(l=l):
                result = self.generator.get_number_str(l)
                self.assertEqual(len(result), l)


if __name__ == "__main__":
    unittest.main()
