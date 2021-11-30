import logging
import unittest
from os import path
from unittest.mock import Mock, patch

import requests
from lib.generators import NAMES_URL, NameGenerator

log = logging.getLogger(path.basename(__file__))


class TestNameGenerator(unittest.TestCase):
    """Test NameGenerator"""

    def setUp(self):
        self.generator = NameGenerator(5, 7)

    def test_validate_length_of_valid_name(self):
        name = "nick12"
        result = self.generator._validate_length(name)
        self.assertTrue(result)

    def test_valdate_length_of_invalid_name(self):
        for name in ["nick", "nick1234"]:
            with self.subTest(msg=f"testing {name}", name=name):
                result = self.generator._validate_length(name)
                self.assertFalse(result)

    @patch.object(requests, "get")
    @patch.object(log, "info")
    def test__fetch_names_parses_results(self, mock_requests_get, mock_logger):
        mock_data = {
            "results": [
                {"name": {"title": "Ms", "first": "Cathy", "last": "Dixon"}},
                {"name": {"title": "Mr", "first": "Benjamin", "last": "Morrison"}},
            ]
        }

        mock_requests_get.return_value.json = Mock(return_value=mock_data)
        result = self.generator._fetch_names()
        expected = ["Cathy", "Benjamin"]

        self.assertListEqual(result, expected)
        self.assertEqual(mock_requests_get.call_count, 1)
        mock_logger.assert_called_once_with(f"calling {NAMES_URL}")

    @unittest.skip("need to write")
    def test__fetch_names_logs_an_error(self):
        pass

    @patch.object(NameGenerator, "_fetch_names")
    def test_get_name(self, mock_fetch_names):
        mock_fetch_names.return_value = ["Cathy"]
        result = self.generator.get_names()

        self.assertEqual(result, "Cathy")
        self.assertEqual(mock_fetch_names.call_count, 1)

    @patch.object(NameGenerator, "_fetch_names")
    def test_get_name_gets_more_names(self, mock_fetch_names):
        mock_fetch_names.side_effect = [["Jim"], ["Benjamin"], ["Marcus"]]
        result = self.generator.get_names()

        self.assertEqual(result, "Marcus")
        self.assertEqual(mock_fetch_names.call_count, 3)


if __name__ == "__main__":
    unittest.main()
